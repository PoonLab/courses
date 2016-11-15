import argparse
import remap
import sys

def main():
    parser = argparse.ArgumentParser(
        description='Generate a new reference sequence from the consensus '
                    'of reads that were mapped to the current reference.'
    )
    parser.add_argument('sam', type=argparse.FileType('rU'),
                        help='<input> SAM file')
    parser.add_argument('ref', type=argparse.FileType('rU'),
                        help='<input> FASTA file containing reference')
    args = parser.parse_args()

    # load the reference sequence
    refseq = ''
    for line in args.ref:
        if line.startswith('>'):
            continue
        refseq += line.strip('\n')

    pileup, counts = remap.sam_to_pileup(args.sam)
    conseqs = remap.pileup_to_conseq(pileup, 10)

    conseq = remap.update_reference(refseq, conseqs.values()[0])
    sys.stdout.write(conseq)

if __name__ == '__main__':
    main()