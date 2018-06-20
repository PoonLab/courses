# Working with tabular data in Python

> Note: this document is being revised

1. [Binary and text files](TabularData.md#binary-and-text-files)
2. [Tabular data](TabularData.md#tabular-data)
3. [Reading files in Python](TabularData.md#reading-files-in-python)
4. [Iterating over the file](TabularData.md#iterating-over-the-file)
5. [Example: NCBI ClinVar](TabularData.md#example-ncbi-clinvar)
6. [Composing and debugging scripts](TabularData.md#composing-and-debugging-scripts)
7. [The `csv` module](TabularData.md#the-csv-module)
8. [Writing CSV files](TabularData.md#writing-tabular-data)

## Binary and text files

### Binary and plain text
First, let's draw a distinction between plain text and binary files.  All files correspond to a series of 1's and 0's on the hard drive or in memory.  A stream of bits is all the computer needs to run a set of instructions, but it would be difficult for a person to read and interpret these instructions.  For this reason, a file that encodes an executable program is some times referred to as a "binary" - it isn't intended to be read by users.  (For fun, try running `head` on a binary executable file.)  

A plain text file has a flag that tells the computer that it should apply a [character encoding](https://en.wikipedia.org/wiki/Character_encoding) that maps binary sequences (bit strings) to symbols that make sense to a person, such as characters in an alphabet.  For example, the [ASCII](https://en.wikipedia.org/wiki/ASCII) encoding maps the bit string `1001010` to the letter `J`.  This means that when you open the file, the computer knows that it should display its contents as a collection of meaningful characters.  Obviously this is a big advantage for making a file immediately interpretable.  However, we sacrifice some efficiency to make this possible, so binary files tend to be more compact while storing the same information. 

### ASCII and Unicode
ASCII is a limited map: it encodes 128 characters (2 raised to the power of 7), including several special characters that represent specific operations such as a line break.  As a standard with roots in the U.S.A. (the A stands for American), it is really only suitable for encoding plain text in American English.  However, there are many languages in the world and some of those languages have thousands of characters representing different words!  For this reason, another consortium was founded (ironically also in the United States) to develop and maintain a larger character set for encoding many different languages: [Unicode](https://en.wikipedia.org/wiki/Unicode).  

![](https://imgs.xkcd.com/comics/unicode.png)

A Unicode transformation format (UTF) is like ASCII but uses more than 7 bits; for example, UTF-8 uses 8 bits and can encode 256 characters.  More importantly, multiple UTF-8 encoding bits can be combined to map to a massive number of characters.  For example, the current Unicode standard maps to 136,755 characters, including emoji, which can be reached by [combining UTF-8 bytes](https://en.wikipedia.org/wiki/UTF-8).

### Parsing text
For a plain text file, a format is a set of rules about how the characters are arranged to encode information.  Data formats are a necessary evil in bioinformatics.  Learning to parse new formats and converting between formats is a ubiquitous task that is often made more difficult by the lack of a strict standardization for popular formats such as [NEXUS](https://en.wikipedia.org/wiki/Nexus_file) or [Newick](https://en.wikipedia.org/wiki/Newick_format).  Fortunately, the pervasiveness of such tasks means that there are also plenty of resources in the public domain that make them easier to accomplish.

In this module, we are going to learn how to parse tabular data sets in Python, in which information is organized into a table with specific numbers of rows and columns.  Many bioinformatic data sets have a format that is consistent with tabular data.  Even though these data can be imported into a spreadsheet application such as Excel, the dimensions of many bioinformatic data sets make it difficult to work with manually and we usually need to process enormous numbers of rows and/or columns and to automate the batch processing of many files.


## Tabular data

Tabular data formats are probably the most common format for storing conventional data types.  A table is made up of rows and columns like a [spreadsheet](https://en.wikipedia.org/wiki/Spreadsheet).  Table rows (by convention) represent independent observations/records, such as a sample of patients, and columns represent different kinds of measurements (variables) such as height and weight.  For example:

|agegp |alcgp  |tobgp    | ncases| ncontrols|
|:-----|:------|:--------|------:|---------:|
|75+   |40-79  |0-9g/day |      2|         5|
|75+   |40-79  |10-19    |      1|         3|
|35-44 |80-119 |10-19    |      0|         6|
|65-74 |80-119 |10-19    |      4|        12|
|55-64 |40-79  |30+      |      3|         6|
|45-54 |120+   |10-19    |      3|         4|
|55-64 |120+   |20-29    |      2|         3|
|25-34 |80-119 |30+      |      0|         2|
|55-64 |40-79  |20-29    |      4|        17|
|55-64 |80-119 |10-19    |      8|        15|

These data come from the `esoph` dataset in [R](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/00Index.html). For what it's worth, to extract this subsample I used the following command in R:
```R
kable(esoph[sample(1:nrow(esoph), 10),], format='markdown', row.names=F)
```
where I used the `kable` function to display the table in Markdown format.  These are aggregate data from a case-control study of esophageal cancer in France.  If you're interested about the study, you can read more about it in the source reference: [Brewlow and Day 1980](https://www.iarc.fr/en/publications/pdfs-online/stat/sp32/).  

How do we record this information in a plain text file?  Typically, we preserve the row structure of the table by placing line breaks between each row.  A [line break](https://en.wikipedia.org/wiki/Newline) is a special character encoding that tells the computer to move to a new line when displaying the content of a text file.  Different operating systems use [different control characters](https://en.wikipedia.org/wiki/Newline#Representations) in the ASCII encoding set to represent a line break: UNIX and its descendants use `LF` (line feed); Apple computers used `CR` (carriage return) until the OS became a UNIX-like system; and Microsoft Windows uses a combination of `LF` and `CR`.  This frequently causes problems when passing data files originating from different computers between programs that were developed on different platforms!  If you are trying to process a data file with a program and it isn't working, this is a possible cause.

We still have to deal with preserving the column structure of a tabular data set.  This is usually accomplished with a [delimiter](https://en.wikipedia.org/wiki/Delimiter): a character or sequence of characters that is used to separate content that belongs to different items.  The comma `,` is probably the most common delimiter, closely followed (if not surpassed) by the [tab character](https://en.wikipedia.org/wiki/Tab_key#Tab_characters), which is represented by the escape character `\t`.  To illustrate, here is how the first few rows in our `esoph` data would appear in a comma-separated values (CSV) file:
```
agegp,alcgp,tobgp,ncases,ncontrols
75+,40-79,0-9g/day,2,5
75+,40-79,10-19,1,3
35-44,80-119,10-19,0,6
```

and here they are formatted as a tab-separated values (TSV) file:
```
agegp	alcgp	tobgp	ncases	ncontrols
75+	40-79	0-9g/day	2	5
75+	40-79	10-19	1	3
35-44	80-119	10-19	0	6
```

An important feature of these formats is that the first line is being used to store the column *labels* or headers.  This is often referred to as the *header row*.  Including the header row is optional in a CSV or TSV file, but it is important to be aware of whether it is present or absent when you are processing the file - otherwise you might intepret the labels as data, or vice versa.

A tabular data file should have the same number of items on each line.  If a line has more items than another, then the assignment of items to the various columns becomes ambiguous (especially if the data are similar types, such as a large set of numbers).  In other words, did we append an extra number to the left, or the right, or some where in the middle?  

What happens if our data includes entries that contain the delimiter?  For example, suppose that our data set includes text fields that contain a description of symptoms, such as: `muscular pain, acute`.  This creates the exact problem that we just described!  Fortunately, this format is so widely used, and this problem so common, that there is a standardized solution: we enclose the affected item in double quotes.  In other words, this row:
```
67,muscular pain, acute,Toronto
```
becomes this:
```
67,"muscular pain, acute",Toronto
```

One last thing.  There are several reasons why tabular data formats are not the most convenient choice for other types of data, or for many situations.  One of these situations is when you want to write some additional information about the content of the table in the file.  For example, suppose that we wanted to properly credit the authors of the study that these data came from.  We can't append lines to this table that contain a reference to the literature without breaking up the tabular data scheme and causing problems when we want to parse the data.  One solution to this problem is to reserve a special character to indicate that lines beginning with that character are comments and should be ignored.  There is no standard practice for commenting CSV files.  However, I have frequently seen the `#` character used for this purpose.

![](https://imgs.xkcd.com/comics/file_extensions.png)



## Reading files in Python

Okay, let's use `cd` and `ls` to navigate to the `examples` folder.  I've placed a CSV file derived from the `esoph` R data set, which I've uncreatively named `esoph.csv`:
```shell
[Elzar:~/git/courses] artpoon% pwd
/Users/artpoon/git/courses
[Elzar:~/git/courses] artpoon% cd PATH9577/
[Elzar:~/git/courses/PATH9577] artpoon% cd examples/
[Elzar:courses/PATH9577/examples] artpoon% ls
esoph.csv
```
If you haven't cloned this repository, you can grab this example file by directing your browser to [this link](https://github.com/PoonLab/courses/raw/master/PATH9577Q/examples/esoph.csv).

Use the `head` command to have a quick look at the contents of this file:
```
[Elzar:courses/PATH9577Q/examples] artpoon% head -n5 esoph.csv 
agegp,alcgp,tobgp,ncases,ncontrols
25-34,0-39g/day,0-9g/day,0,40
25-34,0-39g/day,10-19,0,10
25-34,0-39g/day,20-29,0,6
25-34,0-39g/day,30+,0,5
```

The first thing we need to do is to open the file.  This is accomplished with the built-in Python function `open`:
```python
>>> handle = open('esoph.csv', 'rU')
```
Before we talk about what's happening here, we need to talk a bit about functions and variables.  There are two arguments being passed to the `open` function in this example:
1. `'esoph.csv'` is a string (sequence of characters) that corresponds to a relative path to the file.  Since we initiated our Python session in the same directory as the file, we don't need to specify any other directories.
2. `'rU'` is another string that tells Python to open the file in "read-only" mode (`r`) and to interpret the stream of ones and zeros being transmitted from the file with a Unicode encoding `U`.  
How are we supposed to know what arguments to pass to a function?  You need to use another built-in Python function called `help`:
```python
>>> help(open)
```
This spawns another interactive shell for viewing the help documentation for the `open` function:
```shell
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise IOError upon failure.
```
There's actually many more lines than this!  This shell works the same way as `less` and `man`: you can scroll up and down with the arrow keys, and return to your Python session at any time by typing `q`.  The first line of the help document provides some concise information about how to use the function (to get more detailed information, keep reading!).  There are 8 different arguments that can be passed to the `open` function.  There is only 1 argument that doesn't have a default value: `file`.  That is what we use to specify an absolute or relative path to the file that we want to open a stream from. The `mode` argument is the only one that I've ever used in practice.  Note that it defaults to a read-only mode (`r`).  This is good behaviour - if it defaulted to a write mode (`w`), then you'd wiped out every file you tried to open! 

Calling the `open` function caused Python to open a stream to the file named `esoph.csv`.  Since this file is in the present working directory (typically where our shell was located in the file system when we triggered an interactive Python session), we don't have to specify an absolute or relative path to the file.  Think of a stream as a binary sequence of ones and zeros that are being read off the storage device.  The stream always starts at the beginning of the file; it can't start somewhere in the middle.  By default, Python will interpret a file stream in read mode using the Unicode encoding.  Once you've moved forward in the stream, you can't easily go back.  It's possible, but it requires calling functions that we won't cover in this course.

What are we supposed to do with this file stream object?
```python
>>> handle
<_io.TextIOWrapper name='esoph.csv' mode='rU' encoding='UTF-8'>
```
That wasn't very informative, but worth a try!  If we really want to learn about what this kind of object can do, we can use the `help` function again - however, this is going to splash a lot more information than you probably want to digest at this point.  Let's introduce another helpful function (ha ha): `dir`.
```python
>>> dir(handle)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']
```
This returns a list of all the possible functions associated with the kind of object that we've labelled `handle`.  The functions that have a name surrounded by double underscores (`__`) are attributes of the object that have standardized names.  For example, `__str__` is a function that determines what text will appear if you call the base function `print` on this object:
```python
>>> handle.__str__()
"<_io.TextIOWrapper name='DataFormats.md' mode='r' encoding='UTF-8'>"
```
Well, that's exactly what was returned to us when we entered the variable name `handle` by itself to print the value associated with this variable.  Don't worry about details of this output for now; I'm just using `__str__` as a convenient example.

Here are some of the more useful methods of file objects in read mode:
* `read` : This function returns the entire file stream as one long string
* `readlines` : This function cuts up the stream wherever it encounters a line break, and returns the resulting pieces as a list (a kind of Python object that we'll talk more about later).
* `readline` : Cuts the stream at the line breaks, but returns only one piece at a time.  The first time you call this function, you'll get the first line.  The second time returns the second line, and so on.
* `close` : When you're done with the file stream, it is good programming practice to clean up after yourself and close the stream.  

We're finally ready to do a little processing with our example file:
```python
>>> handle.readline()
'agegp,alcgp,tobgp,ncases,ncontrols\n'
>>> handle.readline()
'25-34,0-39g/day,0-9g/day,0,40\n'
>>> handle.readline()
'25-34,0-39g/day,10-19,0,10\n'
```
What's this `\n` thingy?  This is how line breaks are represented in UNIX.  The backslash character (`\`) has a special meaning in UNIX - it is known as an escape character that tells the computer to interpret the *next* character differently.  In this case, we want to tell the computer that this is not the letter `n`; it is a line break.

![](https://imgs.xkcd.com/comics/backslashes.png)

Well.  That's great, we can see the contents of the file, but it's flying off into the ether because we're not assigning it to a variable so we can do something with it.  Let's fix that:
```python
>>> line = handle.readline()
>>> line
'25-34,0-39g/day,20-29,0,6\n'
```
Now we've got a variable that we've named `line` that is holding onto the content of one of the lines in our file.  This is still not terribly useful, because there are still many lines in the file and I don't want to keep assigning those lines to this same variable.  I also don't want to come up with different variable names for every line, like this:
```
>>> line2 = handle.readline()
>>> line3 = handle.readline()
>>> another_line = handle.readline()
```
This is valid Python, but it's also stupid.  The smart thing to do here is to use a [for loop](ControlFlow.md) to iterate over the contents of the file.


## Iterating over the file

So far we've been messing around with our file in an interactive session of Python.  Now we're going to write structured code, so let's open a new text file and start out with this basic script:
```python
"""
Parse the contents of the tabular data set esoph.csv
"""
handle = open('esoph.csv')  # defaults to read mode
for line in handle.readlines():
    print(line)
```
Now save this script as `esoph.py` in the same directory as `esoph.csv` and run it with:
```shell
art@orolo:~/git/courses/PATH9577Q/examples$ python esoph.py 
agegp,alcgp,tobgp,ncases,ncontrols

25-34,0-39g/day,0-9g/day,0,40

25-34,0-39g/day,10-19,0,10

25-34,0-39g/day,20-29,0,6

```
Note that the output is skipping every other line because each string returned by `readlines()` keeps the line break at the end.  This still isn't very useful code - we could have accomplished the same thing with a `cat` statement.  No, for our script to start getting useful, we have to use what we've learned about [string manipulation](Strings.md).

Hopefully you'll have noticed that some (if not all) of the string functions that we just reviewed are really useful for working with tabular data sets.  Let's open a file handle to our example plain-text file again:
```python
handle = open('esoph.csv', 'rU')  # let's use Unicode encoding
```
We know that our file contains a header line, so we need to skip it before we process the rest of the data file.  We can do this with the following line:
```python
_ = handle.nextline()  # skip header line
```
In Python 2, I used to be able to use a different function called `next`, but `nextline` pretty much serves the same role: it tells our file object to return the current line and advance to the next line in the file stream.  (Alternatively, `next` has become a built-in function in Python 3 and we can replace `handle.nextline()` with `next(handle)`.)  Since I'm not interested in doing anything with this line, I'm assigning it to a dummy variable as indicated with a single underscore (`_`) --- a totally valid and utterly uninformative variable name!  

Now it's time to iterate through the rest of the file and do something with the information contained within.  We're going to work with prior knowledge about the content of the file - namely, that each row contains the following information:
 * age group
 * alcohol consumption category
 * tobacco consumption category
 * number of cases of esophageal cancer
 * number of controls

Here is a script that will do the following things:
 1. Replace the age group notation with the lower age limit.
 2. Replace 'g' with 'mL' in alcohol consumption units.
 3. Replace the case and control counts with proportion and sample size.
 4. Print each line to the console so we can stream it into another file in a tab-separated format.
 
Here's the entire script:
```python
handle = open('esoph.csv', 'rU')
_ = handle.readline()  # skip header line

for line in handle:
    # remove the line break character and split into substrings at commas
    agegp, alcgp, tobgp, cases, controls = line.strip('\n').split(',')
    min_age = agegp.split('-')[0].strip('+')  # extract first part of XX-YY and remove trailing plus sign
    alcvol = alcgp.replace('g', 'mL')  # alcohol consumption volume
    
    # calculate sample size and case proportion
    sampsize = int(cases) + int(controls)  # convert strings to integers
    propn = float(cases) / sampsize  # a floating point number has a decimal
    
    # write out to console as a tab-separated line
    print ('\t'.join([min_age, alcvol, tobgp, str(propn), str(sampsize)]))

handle.close()  # finished with the file
```

I've cluttered this example script a bit with some documentation, because I want you to get used to the idea of always providing documentation with your code.  This is as much for your own benefit as it is for anyone else who might read your code.  Think of it as doing a big favour for your future self, who has completely forgotten why you wrote this script and how it is supposed to work!

To understand what this script is doing, I find it helpful to extract one line from the file and manually run through the commands being applied to it.  Instead of entering a `for` loop, let's grab one line with `readline`:
```python
>>> line = handle.readline()  # called a second time (after popping off the header)
>>> line
'25-34,0-39g/day,0-9g/day,0,40\n'
>>> line.strip('\n')
'25-34,0-39g/day,0-9g/day,0,40'
>>> line.strip('\n').split(',')
['25-34', '0-39g/day', '0-9g/day', '0', '40']
```
And so on.  Interactively poke and prod at every operation being performed on this line.  What happens if you don't enclose `cases` and `controls` with `int()` functions?  How about if you try to compute the proportion with `int(cases)/sampsize`?


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



## Composing and debugging scripts

We're going to put everything we've covered so far to reformat this data set to address a couple of issues.  First of all, the first field `name` contains a lot of information that has been munged together into a long unintelligible string.  Let's break this up into parts that are easier to work with.  Second, the clinical significance field has a "Last reviewed" comment appended to it that we'd like to break into a separate field. 

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


## The `csv` module

So far, I've shown you a rudimentary approach to parsing a plain text file in CSV format with Python:
1. `open` the file
2. Iterate over each line in the file with a `for` loop
3. `strip` the line break
4. `split` the line into substrings on commas
5. Assign the resulting List object to variables.
6. Do stuff with the variables.
7. Return to step 2 until you reach the end of the file.
The critical step that is specific to CSV formats is step 4.  However, this step will obviously fail if the some entries in the tabular data contain commas.  If the CSV is in a [conventional format](https://tools.ietf.org/html/rfc4180), then each affected entry should be enclosed in double quotes.  If not, then the CSV format is broken and we've got bigger problems: there is no straight-forward way to determine which entry belongs in which column.

To get a useful example, let's download the "all causes" mortality database from the US Government website Data.gov:
```shell
[Elzar:courses/PATH9577Q/examples] artpoon% wget https://data.cdc.gov/api/views/bi63-dtpu/rows.csv
--2018-05-23 22:45:46--  https://data.cdc.gov/api/views/bi63-dtpu/rows.csv
Resolving data.cdc.gov (data.cdc.gov)... 52.206.140.199, 52.206.68.26, 52.206.140.205
Connecting to data.cdc.gov (data.cdc.gov)|52.206.140.199|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/csv]
Saving to: ‘rows.csv’

rows.csv                [ <=>                ] 118.65K  --.-KB/s    in 0.07s   

Last-modified header invalid -- time-stamp ignored.
2018-05-23 22:45:47 (1.65 MB/s) - ‘rows.csv’ saved [1275181]
```
There should now be a new file called `rows.csv` in your current working directory.  (These data are in the public domain but I don't feel comfortable uploading it to this repository, so please use `wget` to obtain your own copy.)  

Let's get a brief look at this file:
```shell
[Elzar:courses/PATH9577Q/examples] artpoon% head -n3 rows.csv
Year,113 Cause Name,Cause Name,State,Deaths,Age-adjusted Death Rate
1999,"Accidents (unintentional injuries) (V01-X59,Y85-Y86)",Unintentional Injuries,Alabama,2313,52.20
1999,"Accidents (unintentional injuries) (V01-X59,Y85-Y86)",Unintentional Injuries,Alaska,294,55.90
```
The very first line of data is going to cause problems - the entry `"Accidents (unintentional injuries) (V01-X59,Y85-Y86)"` contains the comma delimiter and our approach to parsing this file will fail.  To illustrate, here is a small script:
```python
handle = open('rows.csv')
header = next(handle)
print(header)  # show the column labels
for line in handle:
    year, cause113, cause, state, deaths, aad_rate = line.strip('\n').split(',')
```
I saved this to a file `rows.py`.  As expected, running this script throws an exception:
```shell
[Elzar:courses/PATH9577Q/examples] artpoon% python rows.py
Year,113 Cause Name,Cause Name,State,Deaths,Age-adjusted Death Rate

Traceback (most recent call last):
  File "rows.py", line 5, in <module>
    year, cause113, cause, state, deaths, aad_rate = line.strip('\n').split(',')
ValueError: too many values to unpack (expected 6)
```
The `too many values` message is our big clue.  The `expected 6` part tells us that Python was expecting to assign six members from a list returned by `split` to a series of variables, but instead the list had too many members.  This is exactly what we'd expect to happen if one of the entries contains an extra `,`.

Fortunately, parsing tabular data is such a frequent task that Python has a standard module (`csv`) that is already equipped to handle these cases.  To load this module, we simply use an `import` command that should normally appear at the top of your script.  Let's write a different script:
```python
import csv

handle = open('rows.csv')
header = next(handle)  # skip the header line
reader = csv.reader(handle, delimiter=',', quotechar='"')
for row in reader:
    year, cause113, cause, state, deaths, aad_rate = row
```
This time the script runs without throwing any exceptions!  (In fact, there is no output at all.  How would you modify this script to get more feedback to confirm that the tabular data are being processed as expected?)  `csv.reader` is a function in the `csv` module that returns an iterable object where each line is correctly parsed into a row of the tabular data set, including entries enclosed in double quotes.  I've called this function with three arguments:
* `handle` is the open file object (default read mode) that I created on the previous line
* `delimiter=','` is a keyword argument that specifies the delimiter used to separate entries
* `quotechar='"'` is another keyword argument that species the character used to enclose entries that contain the delimiter character.

Great!  Of course, the `csv` module comes with a lot of useful functions for working with tabular data sets.  I'll cover one more here because it's so useful.  `csv.DictReader` returns a different type of iterable object where the column labels contained in the first line of the file are used as keys in a Dictionary object.  The values in each subsequent line are assigned as values to the respective keys.  This is nice when we're working with a dataset that has a great many columns.  Here is yet another example script to illustrate:
```python
import csv

handle = open('rows.csv')
reader = csv.DictReader(handle, delimiter=',', quotechar='"')
for i, row in enumerate(reader):
    if i > 2:
        break  # just print the first 3 rows
    print(row)
```
This yields the following output:
```shell
[Elzar:courses/PATH9577Q/examples] artpoon% python dictread.py
{'Cause Name': 'Unintentional Injuries', 'Deaths': '2313', '113 Cause Name': 'Accidents (unintentional injuries) (V01-X59,Y85-Y86)', 'Age-adjusted Death Rate': '52.20', 'Year': '1999', 'State': 'Alabama'}
{'Cause Name': 'Unintentional Injuries', 'Deaths': '294', '113 Cause Name': 'Accidents (unintentional injuries) (V01-X59,Y85-Y86)', 'Age-adjusted Death Rate': '55.90', 'Year': '1999', 'State': 'Alaska'}
{'Cause Name': 'Unintentional Injuries', 'Deaths': '2214', '113 Cause Name': 'Accidents (unintentional injuries) (V01-X59,Y85-Y86)', 'Age-adjusted Death Rate': '44.80', 'Year': '1999', 'State': 'Arizona'}
```


## Writing tabular data

At this point, we have learned how to read and process tabular data from CSV-formatted files.  I'm going to finish off this section on how to export the results of your processing as tabular data in another file.  To write to a file, we use the `open` command just as we did for reading a file, except that we set the `mode` option to `w`:
```python
handle = open('output.txt', 'w')
```
**Warning:** This will erase the entire contents of the `output.txt` file!  Do not run this command unless you are certain that you don't mind losing everything in that file, or if the string you pass as the first argument to `open` is a valid path to a file that does not yet exist in your filesystem (i.e., a new file).  If you want to retain everything in a pre-existing file and simply append new content, then you have the option of opening the file in the mode `a`:
```python
handle = open('output.txt', 'a')  # nothing is erased
```

Instead of calling `.readline()` or iterating over this file handle, we want to use its `.write()` command:
```python
handle = open('output.txt', 'w')
handle.write('I just wrote something!\n')
handle.close()
```
If you ran this script, you'd now have a new text file in your current working directory named `output.txt` with a single line.

To write tabular data in a CSV format, we can take the following approach if we're not worried about extra commas:
```python
handle = open('output.csv', 'w')
data = [['a', '1'], ['b', '2'], ['c', '3']]
for row in data:
    handle.write(','.join(row) + '\n')
handle.close()
```
Running this script should produce the following file:
```shell
art@orolo:~/Desktop$ cat output.csv
a,1
b,2
c,3
```

Again, it is helpful to use the `csv` module when we're dealing with more complicated situations, such as needing to join a mixture of string and non-string objects into a comma-delimited line, or dealing with entries that contain the delimiter:
```python
import csv
outfile = open('temp.csv', 'w')
writer = csv.writer(outfile, delimiter=',', quotechar='"')
writer.writerow([1,'a', 'this, has a comma'])
outfile.close()
```
This yields the following file:
```shell
art@orolo:~/Desktop$ cat temp.csv
1,a,"this, has a comma"
```
Note that `csv.writer` knew how to handle an integer as well as the string containing the delimiter (`,`).
