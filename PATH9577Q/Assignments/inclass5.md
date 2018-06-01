# In-class assignment 5
### Convert a wide-format to long-format CSV data set for an RNAseq study.

For this exercise, download the CSV file at: 

https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE115007&format=file&file=GSE115007%5Fmono%5Fmac%5Fdc%5Fa%5Fdc%5Fam%2Ecsv%2Egz

If you're having trouble obtaining this file from the NCBI website, I've also uploaded a copy to the OWL course Resources page.  In either case, you will need to use the GNU `gunzip` program to uncompress this file (over half a gigabyte!).

This is a next-generation sequencing-based ([10X Chromium](https://www.10xgenomics.com/solutions/single-cell/)) single-cell gene expression profiling study of five cell types from the tumor ascites of a single patient.  The cell types are as follows:
1. Monocyte 1
2. Monocyte 2
3. Ascites Macrophages
4. Ascites DCs
5. Tonsil DCs

where DC is dendritic cell and 1, 2 and 5 are presumably controls (at the time of composing this exercise, this was an unpublished study!).  Specifically, this is a dense gene-barcode matrix data set from the study.

We're going to rely on the `csv` module for this exercise.  If you need to review how this works, check the readings on [tabular data sets](Readings/TabularData.md).

1. This data set is so large, it is difficult to use even the command-line tools like `head` to get a sense of what the dimensions are.  First, let's parse the header line and count the total number of entries.  Copy-paste your code into the block below.
   ```python
   # open a stream to this file in read mode
   
   # wrap this stream in a `csv.reader` object
   
   # extract the first row listing from this object
   
   # print the length of this list
   ```
   
   What number did you get?
   ```shell
   ```
   
2. Next, let's print every 1000th entry in this list.  Slice into the list from Q1 and print the result:
   ```python
   
   # provide output of print() here

   ```
   You should see a List object containing strings like this: `'CTCGTCATCGAGAGCA-1'`.  The nucleotide sequence is a barcode. The number after the dash is a [GEM group](https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/output/bam) that is used to differentiate the different samples on a multiplexed run.  We'll assume that these numbers 1 to 5 correspond to the cell types that I listed above.  Each barcode within a group identifies a single cell.

3. Now let's iterate over the rest of the CSV file and print the first 10 entries of every 1000 rows, along with its row number.  Copy-paste your code below:
   ```python
   # start a loop over the csv.reader object
   
       # add an `if` statement to check if we're printing this row
       
           # print the row number and first element in the row
           
   ```

   ```shell
   # copy the output here
   ```

4. The result from Q3 suggests that the first column holds a gene name, and the rest of the entries in a row are integers that count the number of times a transcript from that gene was observed for a particular cell.  Let's calculate the total number of transcripts observed for each gene, and break out of the loop after the first 20 genes.  Start a new script for this question - you can reuse some of the code from the above:
   ```python
   # start a new script
   import csv
   
   # open the file and create a csv.reader object
   
   # skip the header
   
   # start a loop over the csv.reader object - use `enumerate` to track iteration numbers
   
       # iterate over this row (skip the first entry), cast each entry to an integer and sum
       
       # print the first entry (gene name) and the sum
       
       # tell Python to exit this loop if we've done 20 entries
   ```
   Copy the output below:
   ```
   
   ```
