# In-class assignment 4
In the Tabular Data readings, I mentioned processing the `Clinical Significance (last reviewed)` field of the ClinVar BRCA1 data set, but I didn't actually revisit this in the readings.  This task is set aside for an in-class assignment.  In this assignment, our objective is to separate the "last reviewed" date into three separate columns for year, month and day.  In a later class, we will cover how to handle date-time objects using a built-in module, but for now we will do this manually.

Obtain a copy of the ClinVar data set if you haven't already done so:
```bash
art@orolo:~/Downloads$ wget https://github.com/PoonLab/courses/raw/master/PATH9577Q/examples/ClinVar.BRCA1.tsv
```

1. Create a new Python script that will:
   * open this ClinVar file
   * convert the first line into a List object by splitting on '\t'
   * print this List to the console and exit
   ```python
   # Write your code here
   ```
   
