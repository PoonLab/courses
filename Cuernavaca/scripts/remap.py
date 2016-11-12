import re
import sys
import tempfile
import os

tempdir = tempfile.gettempdir()
cigar_re = re.compile('[0-9]+[MIDNSHPX=]')  # CIGAR token
indel_re = re.compile('[+-][0-9]+')

def is_first_read(flag):
    """
    Interpret bitwise flag from SAM field.
    Returns True or False indicating whether the read is the first read in a pair.
    """
    IS_FIRST_SEGMENT = 0x40
    return (int(flag) & IS_FIRST_SEGMENT) != 0

def sam_to_pileup (handle):
    """
    Convert a SAM-style CSV file into samtools pileup-like format in memory.
    Process inline by region.  Also return numbers of reads mapped to each region.
    :param sam_csv: Product of prelim_map.py or iterative remapping.
    :return: dictionary by region, keying dictionaries of concatenated bases by position
    """
    pileup = {}
    counts = {}
    for rcount, row in enumerate(handle):
        if row.startswith('@'):
            continue
        qname, flag, refname, rpos, mapq, cigar, rnext, pnext, tlen, seq, qual = row.split('\t')[:11]
        if cigar == '*':
            continue  # unmapped read

        if refname not in pileup:
            pileup.update({refname: {}})
        if refname not in counts:
            counts.update({refname: 0})


        # update mapped read counts
        counts[refname] += 1

        is_first = is_first_read(flag)

        pos = 0  # position in sequence
        refpos = int(rpos) # position in reference

        tokens = cigar_re.findall(cigar)

        if tokens[0].endswith('S'):
            # skip left soft clip
            pos = int(tokens[0][:-1])
            tokens.pop(0)  # remove this first token

        if not tokens[0].endswith('M'):
            # the leftmost token must end with M
            print 'ERROR: CIGAR token after soft clip must be match interval'
            sys.exit()

        # record start of read
        if refpos not in pileup[refname]:
            # keys 's' = sequence, 'q' = quality string
            pileup[refname].update({refpos: {'s': '', 'q': ''}})
        pileup[refname][refpos]['s'] += '^' + chr(int(mapq)+33)

        for token in tokens:
            length = int(token[:-1])
            if token.endswith('M'):
                # match
                for i in range(length):
                    if refpos not in pileup[refname]: pileup[refname].update({refpos: {'s': '', 'q': ''}})
                    pileup[refname][refpos]['s'] += seq[pos] if is_first else seq[pos].lower()
                    pileup[refname][refpos]['q'] += qual[pos]
                    pos += 1
                    refpos += 1

            elif token.endswith('D'):
                # deletion relative to reference
                pileup[refname][refpos-1]['s'] += '-' + str(length) + ('N' if is_first else 'n')*length

                # append deletion placeholders downstream
                for i in range(refpos, refpos+length):
                    if i not in pileup[refname]: pileup[refname].update({i: {'s': '', 'q': ''}})
                    pileup[refname][i]['s'] += '*'

                refpos += length

            elif token.endswith('I'):
                # insertion relative to reference
                # FIXME: pileup does not record quality scores of inserted bases
                insert = seq[pos:(pos+length)]
                pileup[refname][refpos-1]['s'] += '+' + str(length) + (insert if is_first else insert.lower())
                pos += length

            elif token.endswith('S'):
                # soft clip
                break

            else:
                print 'ERROR: Unknown token in CIGAR string', token
                sys.exit()

        # record end of read
        pileup[refname][refpos-1]['s'] += '$'

    return pileup, counts



def pileup_to_conseq (pileup, qCutoff):
    """
    Generate a consensus sequence from a samtools pileup file.
    Each line in a pileup file corresponds to a nucleotide position in the
     reference.
    Tokens are interpreted as follows:
    ^               start of read
    $               end of read
    +[1-9]+[ACGT]+  insertion relative to ref of length \1 and substring \2
    -[1-9]+N+  deletion relative to ref of length \1 and substring \2
    *               placeholder for deleted base

    FIXME: this cannot handle combinations of insertions (e.g., 1I3M2I)
    because a pileup loses all linkage information.  For now we have to
    restrict all insertions to those divisible by 3 to enforce a reading
    frame.
    """
    conseqs = {}
    to_skip = 0
    last_pos = 0

    for ref, records in pileup.iteritems():
        conseq = ''
        keys = records.keys()
        keys.sort()

        for pos in keys:
            astr = records[pos]['s']
            qstr = records[pos]['q']

            if to_skip > 0:
                to_skip -= 1
                continue

            if (pos - last_pos) > 1:
                conseq += 'N' * (pos - last_pos - 1)
            last_pos = pos
            alist = []  # alist stores all bases at a given coordinate
            i = 0       # Current index for astr
            j = 0       # Current index for qstr

            while i < len(astr):
                if astr[i] == '^':
                    q = ord(qstr[j])-33
                    base = astr[i+2] if q >= qCutoff else 'N'
                    alist.append(base.upper())
                    i += 3
                    j += 1
                elif astr[i] in '*':
                    alist.append('-')
                    i += 1
                elif astr[i] == '$':
                    i += 1
                elif i < len(astr)-1 and astr[i+1] in '+-':
                    # i-th base is followed by an indel indicator
                    m = indel_re.match(astr[i+1:])
                    indel_len = int(m.group().strip('+-'))
                    left = i+1 + len(m.group())
                    insertion = astr[left:(left+indel_len)]
                    q = ord(qstr[j])-33
                    base = astr[i].upper() if q >= qCutoff else 'N'
                    token = base + m.group() + insertion.upper()  # e.g., A+3ACG
                    if astr[i+1] == '+':
                        alist.append(token)
                    else:
                        alist.append(base)
                    i += len(token)
                    j += 1
                else:
                    # Operative case: sequence matches reference (And no indel ahead)
                    q = ord(qstr[j])-33
                    base = astr[i].upper() if q >= qCutoff else 'N'
                    alist.append(base)
                    i += 1
                    j += 1

            atypes = set(alist)
            intermed = []
            for atype in atypes:
                intermed.append((alist.count(atype), atype))
            intermed.sort(reverse=True)

            if intermed:
                token = intermed[0][1]
            else:
                token = 'N'

            if '+' in token:
                m = indel_re.findall(token)[0] # \+[0-9]+
                conseq += token[0]
                if int(m) % 3 == 0:
                    # only add insertions that retain reading frame
                    conseq += token[1+len(m):]
            elif token == '-':
                conseq += '-'
            else:
                conseq += token

        # remove in-frame deletions (multiples of 3), if any
        pat = re.compile('([ACGT])(---)+([ACGT])')
        conseq = re.sub(pat, r'\g<1>\g<3>', conseq)
        conseqs.update({ref: conseq})

    return conseqs


def update_reference(reference, conseq):
    #alignment = pairwise2.align.localxx(reference, conseq)  # too slow!!!
    infile = os.path.join(tempdir, 'remap.fa')
    outfile = infile.replace('.fa', '.mafft.fa')
    with open(infile, 'w') as handle:
        handle.write('>ref\n%s\n>conseq\n%s\n' % (reference, conseq))
    os.system('mafft %s > %s' % (infile, outfile))
    with open(outfile, 'rU') as handle:
        for line in handle:
            sys.stdout.write(line)
    # TODO: use alignment to modify reference
