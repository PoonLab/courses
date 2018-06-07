# Take-home assignment 6
## Refactoring bad code

1. This is an intentionally bad script that takes a nucleotide sequence from the command line and returns the amino acid translation.
```python
c={'CTT':'L','ATG':'M','ACA':'T','XXX':'?','ACG':'T','ATC':'I','AAC':'N','ATA':'I','AGG':'R','CCT':'P','ACT':'T','AGC':'S','AAG':'K','AGA':'R','CAT':'H','---':'-','AAT':'N','ATT':'I','CTG':'L','CTA':'L','CTC':'L','CAC':'H','TGG':'W','CCG':'P','AGT':'S','CCA':'P','CAA':'Q','CCC':'P','TAT':'Y','GGT':'G','TGT':'C','CGA':'R','CAG':'Q','TCT':'S','GAT':'D','CGG':'R','TTT':'F','TGC':'C','GGG':'G','TAG':'*','GGA':'G','TAA':'*','GGC':'G','TAC':'Y','TTC':'F','TCG':'S','TTA':'L','TTG':'L','TCC':'S','ACC':'T','TCA':'S','GCA':'A','GTA':'V','GCC':'A','GTC':'V','GCG':'A','GTG':'V','GAG':'E','GTT':'V','GCT':'A','AAA':'K','TGA':'*','GAC':'D','CGT':'R','GAA':'E','CGC':'R'}
from sys import argv
print(''.join(map(lambda x:c.get(x,'?'),sys.argv[1])))
```
