> This document is being revised

# Tabular Data 2 - Lists and Control flow

## Outline
* A second example data set 
* Review: handling tabular data in Python
* Iterable objects
  * strings, lists and tuples
  * compiling a list of unique entries
* Control flow - if-else, break and continue
* Composing and debugging scripts


## Example: NCBI ClinVar
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




## This is probably a good point for a break

![](https://imgs.xkcd.com/comics/outreach.png)



## Composing and debugging scripts

Let's get back to our example.  We're going to put everything we've covered so far to reformat this data set to address a couple of issues.  First of all, the first field `name` contains a lot of information that has been munged together into a long unintelligible string.  Let's break this up into parts that are easier to work with.  Second, the clinical significance field has a "Last reviewed" comment appended to it that we'd like to break into a separate field. 

When we're composing a script, it generally helps to write it out in stages with a text editor and run those drafts with a non-interactive Python interpreter to check some intermediate outputs.  Any plain text editor will do.  I tend to use PyCharm, but gedit works just as well and if I know that I'm making a small change, I prefer to use UNIX [vim](https://en.wikipedia.org/wiki/Vi).

![](https://imgs.xkcd.com/comics/real_programmers.png)

Let's start by creating a file and calling it `parse-brca1.py`.  For convenience, you might like to have it in the same directory as the `ClinVar.BRCA1.tsv` file.  Myself, I like keeping my scripts and data in separate folders within a project folder and then calling scripts with relative paths to make the code portable.
```python
handle = open('ClinVar.BRCA1.tsv')
header = handle.readline().strip('\n').split('\t')

for line in handle:
    values = line.strip('\n').split('\t')
    # temporary code - see how labels line up with content of first row
    for i, val in enumerate(values):
        print(header[i], '"', val, '"')  # enclose in quotes to make empty strings more apparent
    break  # run only once!
```
Try this out and see what you get!

Okay, let's start tackling the first objective.  I trying to guess how to parse the `name` field.
```python
handle = open('ClinVar.BRCA1.tsv')
header = handle.readline().strip('\n').split('\t')

# now I just want to run for the first 10
for idx, line in enumerate(handle):
    # The output of the last run tells us about what content we expect per line
    name, _, _, _, clinical, _, _, _, _, _, _ = line.strip('\n').split('\t')
    # ... removed temporary code ...
    accno, rest = name.split(':')  # the first part looks like an accession number
    print(accno, rest)
    if idx == 9:
        break
```

This results in the following output - note the `print` function inserts a space between each argument:
```
NM_007294.3 c.(671_4096)ins(300)
NG_005905.2 g.61068_98138del
NG_005905.2 g.137094_142043del
NG_005905.2 g.118449_154829del
NG_005905.2 g.116321_140085del
NG_005905.2 g.110966_142550del
NG_005905.2 g.133626_139705dup
NM_007294.3(BRCA1) c.81-?_547+?dup
NM_007294.3(BRCA1) c.81-?_5193+?del
NM_007294.3(BRCA1) c.81-?_5152+?dup
```

Uh-oh.  There's some extra stuff tacked onto the first part in some cases.  Let's amend our script to strip it out.
```python
handle = open('ClinVar.BRCA1.tsv')
header = handle.readline().strip('\n').split('\t')

for idx, line in enumerate(handle):
    name, _, _, _, clinical, _, _, _, _, _, _ = line.strip('\n').split('\t')
    accno, rest = name.split(':')
    accno2 = accno.strip('(BRCA1)')
    print(accno2)
    if idx == 9:
        break
```

Output:
```shell
[Elzar:courses/GradPythonCourse/examples] artpoon% python parse-brca1.py | tail -n3
NM_007294.3
NM_007294.3
NM_007294.3
```
OK, that helped.  I'm feeling confident, so I try removing the last two lines to run through the entire file.  
```
NP_009225.
NP_009225.
[...other stuff...]
Traceback (most recent call last):
  File "parse-brca1.py", line 6, in <module>
    accno, rest = name.split(':')
ValueError: not enough values to unpack (expected 2, got 1)
```
Whoops.  That wasn't good enough after all.  We've got two problems.  The first is that the `strip` statement was too much and the clipped off the trailing `1` in some of the accession numbers.  In other words, `NP_009225.` should have remained `NP_009225.1`.  

Second, not all of the `name` values contain a `:`.  What was the value that caused this to happen?  Unfortunately, Python exited the script without telling us.  We need to insert a debugging statement to reveal the contents of the value when our script hits this bug:
```python
handle = open('ClinVar.BRCA1.tsv')
header = handle.readline().strip('\n').split('\t')
for idx, line in enumerate(handle):
    name, _, _, _, clinical, _, _, _, _, _, _ = line.strip('\n').split('\t')
    try:
        accno, rest = name.split(':')
    except:
        print (line)  # show the entire line where the bug occurs
        raise
    accno2 = accno.split('(')[0]  # amended this line
    print(accno2)
```
When we run this, we get the following (I truncated the output after the first line of the traceback):
```
L824X	BRCA1	Breast-ovarian cancer, familial 1		Pathogenic(Last reviewed: Feb 20, 2013)	no assertion criteria provided			GRCh38	125869	131407

Traceback (most recent call last):
```
Our hunch was right - this is one of the few lines where the first value doesn't contain a colon character (`:`).  This would be a good place for a conditional statement:
```python
handle = open('ClinVar.BRCA1.tsv')
header = handle.readline().strip('\n').split('\t')
for idx, line in enumerate(handle):
    name, _, _, _, clinical, _, _, _, _, _, _ = line.strip('\n').split('\t')
    if ':' in name:
        accno, rest = name.split(':')
        accno = accno.split('(')[0]
    else:
        # plain format
        accno = ''  # empty string
        rest = name
    print (accno)
```

We're feeling pretty swell!  But now there's *another* bug:
```shell
Traceback (most recent call last):
  File "parse-brca1.py", line 7, in <module>
    accno, rest = name.split(':')
ValueError: too many values to unpack (expected 2)
```
This error message tells me that when I split the `name` string on the `:` character, I got back more than two substrings.  In other words, one of the `name` values has more than one `:`.  I put in another `try..except` clause and dug up the offending line:
```
NM_007294.3:c.-19-48_80+248delinsU77841.1:g.2145_2536	BRCA1	Breast-ovarian cancer, familial 1		Pathogenic(Last reviewed: Oct 2, 2015)	criteria provided, single submitter	17	43123769 - 43124163	GRCh38	373856	360740
```
Yup, two colons.  We need to make this instruction a little less fragile:
```python
handle = open('ClinVar.BRCA1.tsv')
header = handle.readline().strip('\n').split('\t')
for idx, line in enumerate(handle):
    name, _, _, _, clinical, _, _, _, _, _, _ = line.strip('\n').split('\t')
    if ':' in name:
        tokens = name.split(':')
        accno = tokens[0].split('(')[0]
        rest = ':'.join(tokens[1:])  # stitch the other parts back together
    else:
        accno = ''
        rest = name
    print (accno)
```
And *hooray*, our script now runs through the file without throwing exceptions!  

What just happened?  You've now undergone the horrific experience of debugging code.  [Maurice Wilkes](https://en.wikipedia.org/wiki/Maurice_Wilkes) has a famous quote on debugging attributed to him:
> As soon as we started programming, we found to our surprise that it wasn't as easy to get programs right as we had thought. Debugging had to be discovered. I can remember the exact instant when I realized that a large part of my life from then on was going to be spent in finding mistakes in my own programs.

My motivation for writing this section was to give you a basic idea of what goes on when someone starts writing a script.  You never get it right the first time, and even after the hundredth iteration, there is inevitably some small problem in the code with more complex projects.  As far as composing a single script goes, I like this iterative process of writing a bit, getting some output and testing it out, writing a bit more, and so on.  It (*hopefully*) prevents the situation where you've written a big mess of code and end up having to throw it all away.

![](https://imgs.xkcd.com/comics/new_bug.png)

## In-class assignment: the second objective

For the rest of this session, I'd like you to have a try at implementing our second objective - to separate the "Last reviewed" comment from the `Clinical significance` field of our data set and return the first part (*e.g.,* `Pathogenic`).  Feel free to work in groups, but please e-mail me your own version of the script when you're done.

## Additional exercises
1. Adapt your Python script to output all lines that contain the word `Pathogenic`.  Skip the header line.  Use `print` to write output to standard out, and then redirect this stream to a file by calling your script from the shell and using the `>` operator.  Generate a second file with the same criteria, but using UNIX `grep` instead of Python.  Run UNIX `diff` on the two files to determine if they are the same.

