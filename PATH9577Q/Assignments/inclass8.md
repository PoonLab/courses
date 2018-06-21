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
```

1. Use `gunzip` to uncompress the Genbank file you downloaded, and then `less` to manually examine the file.  Copy and paste the first ten lines here:
   ```
   # top of zika.gb
   ```
   What do you notice about this file?
   ```
   # Write your brief response here
   
   ```

2. 
