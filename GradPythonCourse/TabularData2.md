# Tabular Data 2

* preceded by [Tabular Data 1](https://github.com/PoonLab/courses/blob/master/GradPythonCourse/TabularData.md)

## Outline
* A second example data set 
* Iterable objects - file handles, strings, lists and tuples
* Control flow - if-else, break and continue
* Writing output with formatted strings


### NCBI ClinVar
[ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) is NCBI's web portal to query their curated database of associations between variants in the human genome (alleles) and phenotypes (measurable characteristics).  Results from a ClinVar database query can be saved to your computer as a plain-text file in a tab-separated values (TSV) tabular format.  Here is a snippet of the results when querying `BRCA1`, which returns a table of all variants within the BRCA1 gene and their clinical associations:
```
Name	Gene(s)	Condition(s)	Frequency	Clinical significance (Last reviewed)	Review status	Chromosome	Location	Assembly	VariationID	AlleleID(s)	
NM_007294.3:c.(671_4096)ins(300)	BRCA1	Breast-ovarian cancer, familial 1		Pathogenic(Last reviewed: Oct 2, 2015)	criteria provided, single submitter			GRCh38	373890	360778
NG_005905.2:g.61068_98138del	BRCA1	Breast-ovarian cancer, familial 1	Pathogenic(Last reviewed: Oct 2, 2015)	criteria provided, single submitter	GRCh38	373857	360746
NG_005905.2:g.137094_142043del	BRCA1	Breast-ovarian cancer, familial 1	Pathogenic(Last reviewed: Oct 2, 2015)	criteria provided, single submitter	GRCh38	373853	360745
```
Note that this data file contains a header row.  I've uploaded this CSV file into the `examples/` directory.  To resync your local copy of the repository with the remote copy, navigate to your `courses/` directory and enter the following command:
```shell
art@Misato:~/git/courses/GradPythonCourse/examples$ git pull origin master
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), done.
From http://github.com/PoonLab/courses
 * branch            master     -> FETCH_HEAD
   aa44207..d506966  master     -> origin/master
Merge made by the 'recursive' strategy.
 GradPythonCourse/TabularData2.md | 20 +++++++++++---------
 1 file changed, 11 insertions(+), 9 deletions(-)
```
Your output will vary depending on when you last synced with the remote, and whether you've made any changes to files in your local repository.


Try using some of the UNIX commands we've covered to have a quick look at this file, such as `wc`, `head`, and `grep`.


## Review: parsing a tabular data file in Python

Here is a basic skeleton of a script that opens a file and attempts to read data from it by assuming that it is in a tabular data format:
```python
# set the character or substring we're going to use to 
delimiter ='\t'

# open a stream to the file in read mode
handle = open('ClinVar.BRCA1.tsv', 'rU')

# if we want to skip a header row, we need to advance one line in the stream
_ = handle.readline()

#for line in handle.readlines():
for line in handle:  # this is equivalent to the above statement
    # remove the line break and break the remaining string down to a list of values
    values = line.strip('\n').split(delimiter)
    # do stuff with values here

# tidy up after ourselves
handle.close()
```
This isn't by any means the only way to write this sort of script, and it's far from the best (for one thing, there's no handling of values enclosed in double-quotes).  I'm only using this as a foundation for reviewing some of the basic concepts we've covered so far.  In a later section, I'll talk about a better way of handling tabular data in Python (with the *csv* module).

Recall that a tabular data format is generally defined by separating table rows into different lines in the file, and separating the values within each row (table columns) with a delimiter.  This example script opens the file, pops the first line off as a header row, and then loops through the remaining lines in the file until it reaches the end.  Each line is broken up into pieces (substrings) that get assigned to a list.  

Iteration over the file handle (looping over lines) plays a key role in our script.  
```python
for line in handle:  # this is equivalent to the above statement
```
An open file stream in Python is an iterable object.  Looping over the lines of a file is such a common task that it just made sense to incorporate this into the behaviour of a file stream object; in other words, you don't have to call its `readlines()` function.

This isn't the only iterable object that we're dealing with in this script.  There's also an iterable object being returned from this line:
```python
values = line.strip('\n').split('\t')
```
The `split` function returns a list comprising all the substrings produced by cutting the original string wherever the delimiter occurs.  Since we're already dealing with two iterable objects, I think it makes sense to expand on what these are and how we work with them.


## Iterables

An iterable object in Python is a collection of other objects.  Some iterables can be indexed and sliced, like strings, because they are ordered collections (sequences).  We've covered string indexing, but here's a quick review:
```python
>>> # enclosing characters in double quotes constructs a string that we've assigned to the variable `s`
>>> s = "quesadilla"
>>> s[0]  # index to the first element in the string
'q'
>>> s[-1]  # index to the last element
'a'
>>> s[2:7]  # slice out a substring from the middle
'esadi'
```

Another way to explain what an iterable object in Python is to give an example of something that is not.  An integer is not an iterable object.  It doesn't make sense to think of an integer as a collection.  Not all collections can be indexed.  For example, a *set* is an unordered collection.  You can iterate over it, but the order of iteration is arbitrary.
```python
>>> for i in set([1,2,3]):
...   print(i)
...
1
2
3
>>> for i in set([3,2,1]):
...   print (i)
...
1
2
3
```
(Yeah, to explain something about iterables and indexing, I had to break out yet another kind of Python object: *sets*.  Sets are useful but that's more or less all I'll say about them for a while.)

## Lists
Lists are another kind of iterable object in Python.  We've already been using a few, so it's high time that we talked about what they are and how we work with them.  A list is an ordered collection of any other kind of object.  That's right: you can have a list of numbers, strings, and even other lists!
```python
a_simple_list = [1,2,3,5,7,11,13]
a_mixed_list = [1, 'cow', ['foobar', 5.7], 3.1416]
```

Like strings, list objects have a number of special functions.  
```
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

To learn about what some of these functions do, let's continue working through the BRCA1 example data set.  We left off inside a for-loop iterating over lines of the file stream, stripping the line break off each string and breaking the string up into pieces at every tab character.  Here is the same script with comments removed:
```python
delimiter ='\t'
handle = open('ClinVar.BRCA1.tsv', 'rU')
_ = handle.readline()

for line in handle:
    values = line.strip('\n').split(delimiter)

```


