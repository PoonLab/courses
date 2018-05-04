# Assignment 2.  Working with tabular data in Python

Submit your completed assignment by e-mail as a Markdown file by May 16, 2017.

## Background

The Stanford HIV Drug Resistance Database is an extremely important resource for HIV research and clinical management.  The database holds over 80,000 anonymized patient records collected from around the world.  Screening for the presence of drug resistant variants by generating a nucleotide sequence from the virus genome is standard-of-care and equivalent and more cost-effective than laboratory cell-culture assays.


## Data source
Download the tabular HIV RT data set at this link:

https://hivdb.stanford.edu/modules/lookUpFiles/geno-rx-datasets/RT.txt

and save the file to a location in your filesystem that you can easily navigate to.  I find it helpful to directly download this file to my filesystem instead of attempting to render it in my web browser, by right-clicking on the above URL and selecting "Save Link As..." or whatever the equivalent is for your browser application.  If you're not using a web browser and you're running Linux, you can also use the following command line:
```
wget https://hivdb.stanford.edu/modules/lookUpFiles/geno-rx-datasets/RT.txt
```

This is a tab-separated values (TSV) file that comprises published HIV reverse transcriptase sequence data that are annotated with patient drug treatment histories and sample collection information, such as country and year of sampling.

## Tasks

1. Use a UNIX command to determine the number of records in this file.  Assume that the first line is the header row.  How many records are there?
   ```
   
   ```


2. Using an interactive session of Python, open a file stream in read mode to this file and print the collection year for every sample.  Note that this field includes extra characters like `= ` and `< ` (note the spaces).  You don't want to stream this output to your console - instead, redirect it into a file when you call your script with non-interactive Python on the command line using the `>` operator.  

   Provide your code here:
   ```python
   # insert code here
   ```


3. Modify your code to exclude the non-numeric characters (`<`, `=` and ` `) from the collection year field.  Provide your revised code here:
   ```python
   # insert code here
   
   ```


4. Write some Python code that will extract the only the following fields (see header row):
   * AccessionID - this is a [GenBank accession number](https://www.ncbi.nlm.nih.gov/Sequin/acc.html)
   * Region
   * Year
   * Subtype
   * NASeq - this is the HIV nucleotide sequence from the region encoding RT
  
   and print the result as a line of comma-separated values.  Hint: you can assign the list of substrings returned by `split` to a variable that you can call something like `items` and then assign specific strings in the list that you want to work to other variables.  To assign the last item, you can use something like `last_item = items[-1]`
  
   Provide your code here:
   ```python
   # insert code here
   
   ```

