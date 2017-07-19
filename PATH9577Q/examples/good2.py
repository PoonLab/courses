"""
Calculate nucleotide frequencies from a FASTA file
"""
import argparse
import re
import sys
import os

nucleotides = 'ACGT'  # which symbols to count

def count_bases(path, wait=1e4):
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
    for ln, line in enumerate(handle):  # <-- `ln` = line number
        if ln % wait == 0:
            print('.', end='', flush=True)  # provide feedback on progress
        
        if line.startswith('>'):
            # this line contains a record header, ignore
            continue
        
        # otherwise the line contains sequence
        for char in line:
            if char in nucleotides:
                freqs[char] += 1  # increment this base count
    handle.close()
    print('')
    
    return(freqs)


def is_binary(filename, max_chunks=100):
    """Return true if the given filename is binary.
    @raise EnvironmentError: if the file does not exist or cannot be accessed.
    @attention: found @ http://bytes.com/topic/python/answers/21222-determine-file-type-binary-text on 6/08/2010
    @author: Trent Mick <TrentM@ActiveState.com>
    @author: Jorge Orpinel <jorge@orpinel.com>"""
    fin = open(filename, 'rb')
    try:
        CHUNKSIZE = 1024
        chunk_count = 0
        while 1:
            chunk = fin.read(CHUNKSIZE)
            chunk_count += 1
            if b'\0' in chunk: # found null byte
                return True
            if len(chunk) < CHUNKSIZE or chunk_count > max_chunks:
                break # done
    finally:
        fin.close()
    return False


def is_fasta(filename, maxline=100):
    """ Try to guess if the file is a valid FASTA file with nucleotide sequences """
    pat = re.compile('^[ACGTWRKYSMBDHVN?-]+$')  # regex for nucleotide sequence
    nrecords = 0
    with open(filename, 'rU') as handle:
        for ln, line in enumerate(handle):
            if line.startswith('>'):
                nrecords += 1
                continue
            if not pat.findall(line.upper()) and len(line.strip()) > 0:
                # non-header lines should contain valid nucleotide sequence
                print(line)
                return False
            if ln > maxline:
                break
    if nrecords == 0:
        print ('no records')
        return False
    return True
    

def protectedFileType(path):
    """ Returns an open handle in write mode if the given path does not already have a file """
    assert not os.path.exists(path), "{} exists, no overwrite permitted".format(path)
    return open(path, 'w')
    

def parse_args():
    parser = argparse.ArgumentParser(
        description="Calculate nucleotide frequencies from a FASTA file."
    )
    parser.add_argument('path', help='<input> Relative or absolute path to a FASTA file')
    parser.add_argument('out', help='<output> Path to write output.')
    parser.add_argument('--wait', default=10000, type=int, help="<optional> Number of FASTA lines represented by '.'")

    return parser.parse_args()


def main():
    args = parse_args()

    assert not is_binary(args.path), "This looks like a binary file - I can't process it."
    assert is_fasta(args.path), "This doesn't look like a nucleotide FASTA file :-/"
    
    # args.out is a string
    if os.path.exists(args.out):
        print ("WARNING: output file exists.")
        sys.exit()
    
    freqs = count_bases(args.path, wait=args.wait)
    
    # send formatted output to file
    outfile = open(args.out, 'w')
    outfile.write("Base\tCount\n")
    for nuc, count in freqs.items():
        outfile.write("{}\t{}".format(nuc, count) + '\n')

if __name__ == '__main__':
    main()
