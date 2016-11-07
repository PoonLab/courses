# Secuenciaci&oacute;n de pr&oacute;xima generaci&oacute;n para la evoluci&oacute;n del virus
<!--- Next-generation sequencing analysis for virus evolution -->
## Art Poon [@GitHub](github.com/ArtPoon)

#### Departments of Pathology and Laboratory Medicine; Microbiology and Immunology; Applied Mathematics at Western University, Ontario, Canada



# Why we need to learn code

* NGS data are massive and difficult to analyze with conventional software (e.g., Excel)
* Bioinformatic tools for NGS analysis are extremely valuable
* The majority of tools are designed for human genomics; metagenomics
* Virus populations are too diverse - we need to make our own tools



# What does it mean to code?

* You can't make a button for everything
* Command-line interface offers unlimited versatility
* The open source community provides many powerful resources for free (*e.g.* R)
* Unix-like systems have become the standard for bioinformatics
* The downside is that there is a steep learning curve



# NGS platforms

* Usually people are dealing with 454, Ion Torrent and Illumina
* 454 is an abandoned platform
* 454 and Ion Torrent have insurmountable issues with homopolymer errors
* Illumina a *de facto* standard until better options become mainstream



# InterOp files

* These are binary files (not human readable) that store quality and error metrics associated with the run.
* Try this:
```
less ErrorMetricsOut.bin
```
* Contents of this file are documented [here](http://support.illumina.com/content/dam/illumina-support/documents/documentation/software_documentation/sav/sequencing-analysis-viewer-v1_8_46-guide-15066069-a.pdf)
* We want to access the tile/cycle-specific &phi;X174 error rates contained in `ErrorMetricsOut.bin`



# Running a pipeline

```
% mkdir sandbox
% python scripts/parse-interop.py examples/ErrorMetricsOut.bin \
 sandbox/errorrates.csv
% Rscript scripts/plot-errors.R sandbox/errorates.csv \
 sandbox/errorrates.pdf
```



# Show R plot result here



# The Illumina data files

* Raw data files are too large to allow these to accumulate uncompressed
* Compression reduces file size by about X fold
* Uncompress a file as follows:
```
gunzip TESTFILE.fastq.gz
```



# FASTQ format

```
% head -n4 TESTFILE.fastq
@label
ACGT...
+
!!!!
```
* Illiumina quality scores encoded as follows (see also [Wikipedia](https://en.wikipedia.org/wiki/FASTQ_format#Encoding)):
```
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJ
|                              |         |
0                              31        41
```



# Alignment

* There are two general approaches to aligning short read data:

 1. *de novo* assembly of reads into contigs
 2. mapping to a reference genome

* *de novo* assembly can be a reasonable option if your objective is the consensus genome sequence
* reference mapping is better if your objective is variant detection



# Reference-based mappers

* Generally work on the principle of looking up sequence fragments in a reference index
* Break down reference genome into fragments and record location of each
* Permit mismatches by augmenting index with all 1- and 2-off variants
* There are many mappers (BWA, bowtie2) with none clearly superior



# bowtie2

* Can index 2-off variants
* Allows soft clipping (5' or 3' end of read can be excluded from index query)
* Efficient "Smith-Waterman" alignment to reference after indexing


# Running bowtie2

```
bowtie2 -X examples/index -1 examples/example.R1.fastq -2 examples/example.R2.fastq \
-S sandbox/output.sam
```



# SAM format

* Based on [SAMtools](https://github.com/samtools/samtools) programs (SAM = sequence alignment/map)
* `.sam` has become a *de facto* standard output format for short read mappers



# Tablet

* Java-based tool for visualizing SAM/BAM outputs
