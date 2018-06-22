# In-class assignment 8

## Zika virus dating

Zika virus is a single-stranded RNA virus that is associated with microcephaly in newborns and Guillain-Barré syndrome in adults (although its pathogenesis remains undetermined).  Global awareness of Zika virus has grown in association with recent outbreaks in Brazil and subsequent spread to other countries.  As of June 19, 2018, NCBI Genbank held roughly 1,100 Zika virus sequence records.  

Obtain a compressed data dump of these records at this link:
https://github.com/PoonLab/courses/blob/master/PATH9577Q/data/zika.gb.gz

Next, install [Biopython](https://biopython.org/).  In Linux, the easiest approach is to use your package manager, *e.g.,* `apt` (Debian/Ubuntu) or `yum` (Fedora/Redhat):
```
art@orolo:~$ apt search biopython
Sorting... Done
Full Text Search... Done
python3-biopython/xenial 1.66+dfsg-1build1 amd64
  Python library for bioinformatics (implemented in Python 3)
art@orolo:~$ sudo apt install python3-biopython
```

On macOS, you can use the Python Packaging Authority (PyPA, http://pypa.io) script to install the Python package manager `pip`, which you can then use to install Biopython:
```
[Elzar:~] artpoon% wget https://bootstrap.pypa.io/get-pip.py
[Elzar:~] artpoon% sudo python3 get-pip.py
[Elzar:~] artpoon% sudo pip install biopython
```

1. Use `gunzip --keep zika.gb.gz` to uncompress the Genbank file you downloaded, and then `less` to manually examine the file.  Copy and paste the first ten lines here:
   ```
   # top of zika.gb
   ```


2. Use Biopython to parse this Genbank data set and extract the first record.
   ```python
   # load the SeqIO submodule from the Bio module
   
   # open a file stream in read mode to zika.gb

   # use SeqIO to create a generator object with this stream
   
   # generate the first record from the stream using `next`
   
   ```


4. Use `dir` to inspect the attributes of this `Bio.SeqRecord` object.  There is often a large amount of information buried in the `.features` list attribute.  Each entry in this list has a `.qualifiers` dictionary attribute.  Manually investigate this dictionary and then write a function that takes a `SeqRecord` as its argument and returns a tuple of the sampling country and collection date if present, and `None` if absent:
   ```python
   # paste your answer here
   
   ```


5. The record deposition dates (`SeqRecord.annotations['date']`) are all in the same format: `31-MAY-2018`.  (We're not so lucky with sample collection dates.)  Use the `datetime` module and write a function that takes one of these strings and returns a tuple containing (1) the date in ISO format, and (2) the number of days since January 1, 2000.
   ```python
   
   
   ```


6. Last step!  Let's use the function from Q5 and complete a script that parses the Genbank file to produce two output files: (1) a FASTA containing the accession number, description and sequence (*hint* use `.format('fasta')`), and (2) a CSV file containing:
   * accession number
   * description
   * record date in ISO format
   * number of days since 2000-01-01
   * sampling country
   * sampling date




