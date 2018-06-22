# Take-home assignment 8
## Filtering a FASTQ file for quality reads

Download a gzip-compressed FASTQ file at this link:
https://github.com/PoonLab/courses/blob/master/PATH9577Q/data/SRR2830253-small.fastq.gz

This is a dataset associated with a microbiome study of lung inflammation due to elevated Th17-lymphocytes (Segal *et al.*, Nature Microbiol 2016, https://www.ncbi.nlm.nih.gov/pubmed/27572644).  

1. Use the Biopython `SeqIO` submodule to create a parse object for this file.
   ```python
   from Bio import SeqIO
   
   ```
   
2. 
