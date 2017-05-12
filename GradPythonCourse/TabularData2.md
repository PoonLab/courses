# Tabular Data 2

* preceded by [Tabular Data 1](https://github.com/PoonLab/courses/blob/master/GradPythonCourse/TabularData.md)

## Outline
* A brief tour of tabular data sets in health research
* 


## A brief tour of tabular data in bioinformatics and medical sciences

### NCBI ClinVar
[ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) is NCBI's web portal to query their curated database of associations between variants in the human genome (alleles) and phenotypes (measurable characteristics).  Results from a ClinVar database query can be saved to your computer as a plain-text file in a tab-separated values (TSV) tabular format.  Here is a snippet of the results when querying `BRCA2`, which returns a table of all variants within the BRCA2 gene and their clinical associations:
```
Name	Gene(s)	Condition(s)	Frequency	Clinical significance (Last reviewed)	Review status	Chromosome	Location	Assembly	VariationID	AlleleID(s)	
NM_000059.3:c.156_157insAlu	BRCA2	Breast-ovarian cancer, familial 2		Pathogenic	no assertion criteria provided			GRCh38	403703	390673
NM_000059.3:c.(9257_9501)ins(400)	BRCA2	Breast-ovarian cancer, familial 2		Pathogenic(Last reviewed: Oct 2, 2015)	criteria provided, single submitter			GRCh38	373889	360777
NM_000059.3(BRCA2):c.8954-?_9256+?del	BRCA2	Breast-ovarian cancer, familial 2		Pathogenic(Last reviewed: Oct 2, 2015)	criteria provided, single submitter			GRCh38	267710	262799
```
Note that this data file contains a header row.  

### 


## Review: parsing a tabular data file in Python

Here is a basic skeleton of a script that opens a file and attempts to read data from it by assuming that it is in a tabular data format:
```python
# set the character or substring we're going to use to 
delimiter ='\t'

# open a stream to the file in read mode
handle = open('file.tsv', 'rU')

# if we want to skip a header row, we need to advance one line in the stream
_ = handle.readline()

#for line in handle.readlines():
for line in handle:  # this is equivalent to the above statement
    # remove the line break and break the remaining string down to a list of values
    items = line.strip('\n').split('\t')
    
```
This isn't by any means the only way to write this sort of script, and I'm sure it's far from the best.  I'm only using this as a foundation for reviewing some of the basic concepts we've covered so far.

