import argparse


def iter_fasta (handle):
    """
    Parse open file as FASTA.  Returns a generator
    of handle, sequence tuples.
    """
    label = None
    sequence = ''
    for line in handle:
        if line.startswith('$'): # skip header
            continue
        elif line.startswith('>') or line.startswith('#'):
            if len(sequence) > 0:
                yield label, sequence
                sequence = ''   # reset containers
            label = line.lstrip('>#').rstrip('\n')
        else:
            # deal with spaces in sequence entries
            sequence += line.replace(' ', '').strip('\n').upper()
    yield label, sequence


def count_bases(seq):
    return seq.count('A') + seq.count('C') + seq.count('G') + seq.count('T')

def main():
    parser = argparse.ArgumentParser(
        description='Filter a FASTA file for sequences that are too short.'
    )
    parser.add_argument('fasta', type=argparse.FileType('rU'),
                        help='<input> FASTA file containing sequence alignment to filter.')
    parser.add_argument('minlen', type=int,
                        help='Minimum number of unambiguous bases per sequence.')
    parser.add_argument('outfile', type=argparse.FileType('w'),
                        help='<output> FASTA file to write filtered sequences to.')
    args = parser.parse_args()

    passed = filter(lambda x: count_bases(x[1]) > args.minlen, iter_fasta(args.fasta))
    for label, seq in passed:
        args.outfile.write('>%s\n%s\n' % (label, seq))
        

if __name__ == '__main__':
    main()