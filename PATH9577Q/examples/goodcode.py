"""
Calculate nucleotide frequencies from a FASTA file
"""

import sys

nucleotides = 'ACGT'  # which symbols to count

def count_bases(path):
    """
    Open a FASTA file that contains nucleotide sequences, count the total numbers of 
    nucleotides (defined globally above), and return the result as a dictionary.
    """
    # prepare results container
    freqs = {}
    for nuc in nucleotides:
        freqs.update({nuc: 0})
    
    # iterate through file contents
    handle = open(path, 'rU')
    for line in handle:
        if line.startswith('>'):
            # this line contains a record header, ignore
            continue
        
        # otherwise the line contains sequence
        for char in line:
            if char in nucleotides:
                freqs[char] += 1  # increment this base count
    handle.close()
    
    return(freqs)


def main():
    # check number of arguments
    if len(sys.argv) != 2:
        print ("Usage: python nucfreqs.py [input FASTA]")
        sys.exit()  # quit!
    
    path = sys.argv[1]
    freqs = count_bases(path)
    
    # send formatted output to console
    print ("Base\tCount")
    for nuc, count in freqs.items():
        print ("{}\t{}".format(nuc, count))

if __name__ == '__main__':
    main()

