# Take-home assignment 5

For this assignment, we're going to use the same single-cell gene expression data set as [in-class assignment 5](inclass5.md).  Please refer to that assignment for links to the data set.

This CSV file encodes a very large matrix.  Each column corresponds to a single cell labeled with a 10nt barcode, and assigned to one of five sample groups.  For example, `AAGTCTGGTAGCGTCC-3` corresponds to a barcode from group 3.

1. The groups in this study are as follows:
   1. Monocyte 1
   2. Monocyte 2
   3. Ascites Macrophages
   4. Ascites DCs
   5. Tonsil DCs

   Convert this listing into a Python dictionary:
   ```python
   
   ```

2. Let's use this dictionary to 'unwind' this massive CSV matrix into a narrower but extremely long CSV format with the following column labels:
   * gene
   * barcode
   * group
   * count
The `gene` entry comes from the first item in each row - it's simply a gene name such as `OR4F5`.  We'll write the output to a separate file called `GSE111007-long.csv`.  Finally, let's skip any entry that has a value of `0`.  This will drastically reduce the size of our output file since most of the entries in this gene-barcode matrix are zeroes!

Paste your code below:
   ```python
   import csv
   # open the CSV file
   
   # extract the header row
   
   ```

