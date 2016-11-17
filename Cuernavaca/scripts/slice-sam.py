import re
import sys
import argparse
import itertools


def apply_cigar(cigar, seq, qual, pos=0, clip_from=0, clip_to=None):
    """ Applies a cigar string to recreate a read, then clips the read.

    Use CIGAR string (Compact Idiosyncratic Gapped Alignment Report) in SAM data
    to apply soft clips, insertions, and deletions to the read sequence.
    Any insertions relative to the sample consensus sequence are removed to
    enforce a strict pairwise alignment, and returned separately in a
    dict object.

    @param cigar: a string in the CIGAR format, describing the relationship
        between the read sequence and the consensus sequence
    @param seq: the sequence that was read
    @param qual: quality codes for each base in the read
    @param pos: first position of the read, given in zero-based consensus
        coordinates
    @param clip_from: first position to include after clipping, given in
        zero-based consensus coordinates
    @param clip_to: last position to include after clipping, given in
        zero-based consensus coordinates, None means no clipping at the end
    @return: (sequence, quality, {pos: (insert_seq, insert_qual)}) - the new
        sequence, the new quality string, and a dictionary of insertions with
        the zero-based coordinate in the new sequence that follows each
        insertion as the key, and the insertion sequence and quality strings as
        the value. If none of the read was within the clipped range, then both
        strings will be blank and the dictionary will be empty.
    """
    newseq = '-' * int(pos)  # pad on left
    newqual = '!' * int(pos)
    insertions = {}
    is_valid = re.match(r'^((\d+)([MIDNSHPX=]))*$', cigar)
    tokens = re.findall(r'  (\d+)([MIDNSHPX=])', cigar, re.VERBOSE)
    if not is_valid:
        raise RuntimeError('Invalid CIGAR string: {!r}.'.format(cigar))
    end = None if clip_to is None else clip_to + 1
    left = 0
    for token in tokens:
        length, operation = token
        length = int(length)
        # Matching sequence: carry it over
        if operation == 'M':
            newseq += seq[left:(left+length)]
            newqual += qual[left:(left+length)]
            left += length
        # Deletion relative to reference: pad with gaps
        elif operation == 'D':
            newseq += '-'*length
            newqual += ' '*length  # Assign fake placeholder score (Q=-1)
        # Insertion relative to reference
        elif operation == 'I':
            if end is None or left+pos < end:
                insertions[left+pos-clip_from] = (seq[left:(left+length)],
                                                  qual[left:(left+length)])
            left += length
        # Soft clipping leaves the sequence in the SAM - so we should skip it
        elif operation == 'S':
            left += length
        else:
            raise RuntimeError('Unsupported CIGAR token: {!r}.'.format(
                ''.join(token)))
        if left > len(seq):
            raise RuntimeError(
                'CIGAR string {!r} is too long for sequence {!r}.'.format(cigar,
                                                                          seq))

    if left < len(seq):
        raise RuntimeError(
            'CIGAR string {!r} is too short for sequence {!r}.'.format(cigar,
                                                                       seq))

    return newseq[clip_from:end], newqual[clip_from:end], insertions


def merge_pairs(seq1,
                seq2,
                qual1,
                qual2,
                ins1=None,
                ins2=None,
                q_cutoff=10,
                minimum_q_delta=5):
    """
    Combine paired-end reads into a single sequence.

    Manage discordant base calls on the basis of quality scores, and add any
    insertions.
    @param seq1: a read sequence of base calls in a string
    @param seq2: a read sequence of base calls in a string, aligned with seq1
    @param qual1: a string of quality scores for the base calls in seq1, each
        quality score is an ASCII character of the Phred-scaled base quality+33
    @param qual2: a string of quality scores for the base calls in seq2
    @param ins1: { pos: (seq, qual) } a dictionary of insertions to seq1 with
        the zero-based position that follows each insertion as the
        key, and the insertion sequence and quality strings as the
        value. May also be None.
    @param ins2: the same as ins1, but for seq2
    @param q_cutoff: Phred-scaled base quality as an integer - each base quality
        score must be higher than this, or the base will be reported as an N.
    @param minimum_q_delta: if the two reads disagree on a base, the higher
        quality must be at least this much higher than the other, or that base
        will be reported as an N.
    @return: the merged sequence of base calls in a string
    """
    mseq = ''
    # force second read to be longest of the two
    if len(seq1) > len(seq2):
        seq1, seq2 = seq2, seq1
        qual1, qual2 = qual2, qual1

    q_cutoff_char = chr(q_cutoff+33)
    is_forward_started = False
    is_reverse_started = False
    for i, c2 in enumerate(seq2):
        if c2 != '-':
            is_reverse_started = True
        if i < len(seq1):
            c1 = seq1[i]
            if not is_forward_started:
                if c1 == '-' and c2 == '-':
                    continue
                is_forward_started = True
                mseq = seq1[:i]
            else:
                if c1 == '-' and c2 == '-':
                    mseq += '-'
                    continue
            q1 = qual1[i]
            q2 = qual2[i]
            if c1 == c2:  # Reads agree and at least one has sufficient confidence
                if q1 > q_cutoff_char or q2 > q_cutoff_char:
                    mseq += c1
                else:
                    mseq += 'N'  # neither base is confident
            else:
                if abs(ord(q2) - ord(q1)) >= minimum_q_delta:
                    if q1 > max(q2, q_cutoff_char):
                        mseq += c1
                    elif q2 > max(q1, q_cutoff_char):
                        mseq += c2
                    else:
                        mseq += 'N'
                else:
                    mseq += 'N'  # cannot resolve between discordant bases
        else:
            # past end of read 1
            if c2 == '-':
                if is_reverse_started:
                    mseq += c2
                else:
                    mseq += 'n'  # interval between reads
            elif qual2[i] > q_cutoff_char:
                mseq += c2
            else:
                mseq += 'N'

    if ins1 or ins2:
        merged_inserts = merge_inserts(ins1, ins2, q_cutoff, minimum_q_delta)
        for pos in sorted(merged_inserts.keys(), reverse=True):
            ins_mseq = merged_inserts[pos]
            mseq = mseq[:pos] + ins_mseq + mseq[pos:]
    return mseq


def merge_inserts(ins1, ins2, q_cutoff=10, minimum_q_delta=5):
    """ Merge two sets of insertions.

    @param ins1: { pos: (seq, qual) } a dictionary of insertions from a
        forward read with
        the zero-based position that follows each insertion as the
        key, and the insertion sequence and quality strings as the
        value. May also be None.
    @param ins2: the same as ins1, but for the reverse read
    @param q_cutoff: Phred-scaled base quality as an integer - each base quality
        score must be higher than this, or the base will be reported as an N.
    @param minimum_q_delta: if two insertions disagree on a base, the higher
        quality must be at least this much higher than the other, or that base
        will be reported as an N.
    @return: {pos: seq} for each of the positions in ins1 and ins2. If the same
        position was in both, then the two insertions are merged. If the minimum
        quality for an insertion is below q_cutoff, that insertion is ignored.
    """
    ins1 = {} if ins1 is None else ins1
    ins2 = {} if ins2 is None else ins2
    q_cutoff_char = chr(q_cutoff+33)
    merged = {pos: seq
              for pos, (seq, qual) in ins1.iteritems()
              if min(qual) > q_cutoff_char}
    for pos, (seq2, qual2) in ins2.iteritems():
        if min(qual2) > q_cutoff_char:
            seq1, qual1 = ins1.get(pos, ('', ''))
            merged[pos] = merge_pairs(seq1,
                                      seq2,
                                      qual1,
                                      qual2,
                                      q_cutoff=q_cutoff,
                                      minimum_q_delta=minimum_q_delta)

    return merged


def is_first_read(flag):
    """
    Interpret bitwise flag from SAM field.
    Returns True or False indicating whether the read is the first read in a pair.
    """
    IS_FIRST_SEGMENT = 0x40
    return (int(flag) & IS_FIRST_SEGMENT) != 0


def parse_read_pair(rows, qcut, max_prop_n):
    """ Merge two matched reads into a single aligned read.

    Also report insertions and failed merges.
    @param rows: tuple holding a pair of matched rows - forward and reverse reads
    @return: (refname, merged_seqs, insert_list, failed_list) where
        merged_seqs is {qcut: seq} the merged sequence for each cutoff level
        insert_list is [{'qname': query_name,
                         'fwd_rev': 'F' or 'R',
                         'refname': refname,
                         'pos': pos,
                         'insert': insertion_sequence,
                         'qual': insertion_quality_sequence}] insertions
        relative to the reference sequence.
        failed_list is [{'qname': query_name,
                         'qcut': qcut,
                         'seq1': seq1,
                         'qual1': qual1,
                         'seq2': seq2,
                         'qual2': qual2,
                         'prop_N': proportion_of_Ns,
                         'mseq': merged_sequence}] sequences that failed to
        merge.
    """
    row1, row2 = rows
    mseqs = {}
    failed_list = []
    insert_list = []
    rname = row1['rname']
    qname = row1['qname']

    cigar1 = row1['cigar']
    cigar2 = row2 and row2['cigar']
    failure_cause = None
    if row2 is None:
        failure_cause = 'unmatched'
    elif cigar1 == '*' or cigar2 == '*':
        failure_cause = 'badCigar'
    elif row1['rname'] != row2['rname']:
        failure_cause = '2refs'

    if not failure_cause:
        pos1 = int(row1['pos'])-1  # convert 1-index to 0-index
        seq1, qual1, inserts = apply_cigar(cigar1, row1['seq'], row1['qual'])

        # report insertions relative to sample consensus
        for left, (iseq, iqual) in inserts.iteritems():
            insert_list.append({'qname': qname,
                                'fwd_rev': 'F' if is_first_read(row1['flag']) else 'R',
                                'refname': rname,
                                'pos': pos1+left,
                                'insert': iseq,
                                'qual': iqual})

        seq1 = '-'*pos1 + seq1  # pad sequence on left
        qual1 = '!'*pos1 + qual1  # assign lowest quality to gap prefix so it does not override mate

        # now process the mate
        pos2 = int(row2['pos'])-1  # convert 1-index to 0-index
        seq2, qual2, inserts = apply_cigar(cigar2, row2['seq'], row2['qual'])
        for left, (iseq, iqual) in inserts.iteritems():
            insert_list.append({'qname': qname,
                                'fwd_rev': 'F' if is_first_read(row2['flag']) else 'R',
                                'refname': rname,
                                'pos': pos2+left,
                                'insert': iseq,
                                'qual': iqual})
        seq2 = '-'*pos2 + seq2
        qual2 = '!'*pos2 + qual2

        # merge reads
        mseq = merge_pairs(seq1, seq2, qual1, qual2, q_cutoff=qcut)
        prop_N = mseq.count('N') / float(len(mseq.strip('-')))
        if prop_N > max_prop_n:
            # fail read pair
            failure_cause = 'manyNs'
        else:
            mseqs[qcut] = mseq

    if failure_cause:
        failed_list.append({'qname': qname,
                            'cause': failure_cause})

    return rname, mseqs, insert_list, failed_list



def matchmaker(handle, refname):
    """
    An iterator that returns pairs of reads sharing a common qname from a SAM file stream.
    Note that unpaired reads will be yielded paired with None.
    :param handle: open file handle to CSV generated by remap.py
    :return: yields pairs of rows from DictReader corresponding to paired reads
    """
    fieldnames = ['qname', 'flag', 'rname', 'pos', 'mapq', 'cigar', 'rnext', 'pnext', 'tlen', 'seq', 'qual']
    cached_rows = {}
    for line in handle:
        if line.startswith('@'):
            continue  # skip header row
        row = dict(zip(fieldnames, line.split('\t')[:11]))
        qname = row['qname']
        rname = row['rname']
        if rname != refname:
            continue  # skip read that did not map to target reference
        old_row = cached_rows.pop(qname, None)
        if old_row is None:
            cached_rows[qname] = row
        else:
            # current row should be the second read of the pair
            yield old_row, row

    # Unmatched reads
    for old_row in cached_rows.itervalues():
        yield old_row, None


def parse_sam(handle, refname, qcut, max_n):
    iter = itertools.imap(lambda rows: parse_read_pair(rows, qcut, max_n), matchmaker(handle, refname))
    for rname, mseqs, insert_list, failed_list in iter:
        if len(mseqs) == 0:
            continue  # failed pair
        yield mseqs.values()[0]


def main():
    parser = argparse.ArgumentParser(description="Generate a sequence alignment from SAM output of a short read"
                                                 "mapper, where reads have been filtered to those that map"
                                                 "to a user-specified interval of the reference.")

    # positional arguments
    parser.add_argument('sam', type=argparse.FileType('rU'),
                        help='<input> SAM generated by short read mapping')
    parser.add_argument('out', type=argparse.FileType('w'),
                        help='<output> FASTA of aligned reads')

    # keyword arguments
    parser.add_argument('-refname', type=str, default=None,
                        help='Reference name; must appear in SAM file. '
                             'Leave blank to output a list of available references.')
    parser.add_argument('-left', type=int, default=0,
                        help='Left limit of alignment to output')
    parser.add_argument('-right', type=int, default=None,
                        help='Right limit of alignment to output. '
                             'Leave blank to output the reference sequence length (max value).')
    parser.add_argument('-qcut', type=int, default=15,
                        help='Quality score cutoff for base censoring')
    parser.add_argument('-maxN', type=float, default=0.5,
                        help='Reject reads with a greater proportion of ambiguous bases than this cutoff (0 - 1.0)')
    parser.add_argument('-min_overlap', type=int, default=100,
                        help='Minimum overlap of target region (left:right).')

    args = parser.parse_args()

    if args.refname is None:
        for line in args.sam:
            if line.startswith('@SQ'):
                print re.sub('@SQ[ \t]+SN:(.+)[ \t]+.+', '\\1', line)
        sys.exit()

    if args.right is None:
        for line in args.sam:
            if line.startswith('@SQ') and args.refname in line:
                print re.sub('@SQ[ \t]+SN:(.+)[ \t]+LN:([0-9]+)[^0-9]*', '\\1  \\2', line)
                sys.exit()
        print 'ERROR: Failed to find header line for refname', args.refname
        sys.exit()

    assert args.left >= 0, "Require left >= 0"
    assert args.right >= 0, "Require right >= 0"
    assert args.left < args.right, "Require left < right"
    assert args.min_overlap > 0, "min_overlap must be greater than zero."
    assert args.qcut >= 0, "qcut must be a non-negative integer."
    assert args.maxN >= 0 and args.maxN <= 1.0, "maxN must be between 0 and 1.0 inclusive."


    filter_count = 0
    for mcount, mread in enumerate(parse_sam(args.sam, args.refname, args.qcut, args.maxN)):
        clip = mread[args.left:args.right]
        overlap = len(clip) - clip.count('-')
        if mcount % 1000 == 0:
            print filter_count, mcount  # progress indicator

        if overlap < args.min_overlap:
            continue  # not adequate coverage

        filter_count += 1
        args.out.write('>%d\n%s\n' % (mcount, clip))

if __name__ == '__main__':
    main()
