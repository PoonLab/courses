# In-class assignment 4
In the Tabular Data readings, I mentioned processing the `Clinical Significance (Last reviewed)` field of the ClinVar BRCA1 data set, but I didn't actually revisit this in the readings.  This task is set aside for an in-class assignment.  In this assignment, our objective is to separate the "last reviewed" date into a new columns with the year, month and day encoded in [ISO format](https://en.wikipedia.org/wiki/ISO_8601).  In a later class, we will cover how to handle date-time objects using a built-in module, but for now we will do this manually.

Obtain a copy of the ClinVar data set if you haven't already done so:
```bash
art@orolo:~/Downloads$ wget https://github.com/PoonLab/courses/raw/master/PATH9577Q/examples/ClinVar.BRCA1.tsv
```

1. Create a new Python script that will:
   * open this ClinVar file
   * convert the first line into a List object by splitting on '\t'
   * print this List to the console and exit
   ```python
   # Paste your code here
   
   ```

2. Based on the output of the previous script, determine the index of the `Clinical Significance (Last reviewed)` column.  Use this index to extract the clinical significance field while iterating over rows in this file.  Print the first 10 values (not including the header row) and exit.
   ```python
   # Paste your code here
   
   ```

3. Write a function that will take a date string in the format `Oct 2, 2015` and convert it to ISO format: `2015-10-02`.  Hints:
   * you will need to use a dictionary to convert `Oct` to `10` and so on
   * you can use `split` to separate the date from the rest of the `Clinical Significance` string.
   * use `split` again to isolate the month, day and year components of the date string.
   * use `strip` to remove the comma from the day component
   ```python
   # Paste your code here.
   
   ```
   
4. Complete the script so that it iterates through the ClinVar file and writes rows to a new file, so that the new tabular data set contains a new column for the ISO format dates with header `Last reviewed`, and the previous `Clinical Significance (Last reviewed)` column has been trimmed to the clinical significance component (rename this column `Clinical Significance`).
   ```python
   # Paste your code here.
   
   ```
