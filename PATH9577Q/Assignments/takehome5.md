# Take-home assignment 5

For this assignment, we're going to use the same single-cell gene expression data set as [in-class assignment 5](inclass5.md).  Please refer to that assignment for links to the data set.

This CSV file encodes a very large matrix.  Each column corresponds to a single cell labeled with a 10nt barcode, and assigned to one of five sample groups.  For example, `AAGTCTGGTAGCGTCC-3` corresponds to a barcode from group 3.

1. The groups in this study are as follows:
   1. Monocyte 1
   2. Monocyte 2
   3. Ascites Macrophages
   4. Ascites DCs
   5. Tonsil DCs

   Convert this listing into a Python dictionary, where the integers are keys:
   ```python
   samples = {
       # put your entries here
   }
   ```

2. Extract the header row from the CSV file.  Skip the first entry (it's an empty string) and for every other entry, split the string on the `-` character.  Append the first part to a List called `barcodes`, and the second part to a List called `groups`.
   ```python
   import csv
   # paste your code here
   
   ```

3. Let's use the objects that we prepared in the first two questions to 'unwind' this massive CSV matrix into a narrower but extremely long CSV format with the following column labels:
   * gene
   * barcode
   * group
   * count
   
   The `gene` entry comes from the first item in each row - it's simply a gene name such as `OR4F5`.  We'll write the output to a separate file called `GSE111007-long.csv`.  Finally, let's skip any entry that has a value of `0`.  This will drastically reduce the size of our output file since most of the entries in this gene-barcode matrix are zeroes!  This approach is known as a *sparse* CSV matrix format.

   Paste your code below:
   ```python
   import csv
   # your code from Q1 and Q2 can go here
   
   # open a stream to an output file and wrap in a csv.writer object
   
   # iterate over rows in the csv.reader object (remember the header was already removed and processed)
   
       # break out of this loop if we hit 1,000 lines
       
       # assign the first item in this row to `gene`
       
       # iterate over the remaining items and keep track of the index with `enumerate`
       
           # assign the i-th item to `count`
           
           # only do the next step if count is non-zero
           
               # write the following to your csv.writer: [gene, barcodes[i], samples[groups[i]], count]
               # think: why are we indexing into `groups` and then keying into `samples`?
   
   # when we're done, close the two file streams

   ```

   Copy the first 10 lines of the output file below:
   ```shell
   
   ```
   For the record, the total file size of this sparse output if we ran the whole CSV file is about 369Mb, and the original CSV file is 542Mb!  We could probably get more compact if we use integers instead of the full barcode and sample labels, but then we'd want additional CSV files to associate those integers back to the original labels.

