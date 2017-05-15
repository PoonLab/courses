# Tabular Data 2

* preceded by [Tabular Data 1](https://github.com/PoonLab/courses/blob/master/GradPythonCourse/TabularData.md)

## Outline
* A second example data set 
* Review: handling tabular data in Python
* Iterable objects
  * strings, lists and tuples
  * compiling a list of unique entries
* Control flow - if-else, break and continue
* Writing output with formatted strings


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


## Lists

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

Lists are another kind of iterable object in Python.  We've already been using a few, so it's high time that we talked about what they are and how we work with them.  A list is an ordered collection of any other kind of object.  That's right: you can have a list of numbers, strings, and even other lists!
```python
>>> a_simple_list = [1,2,3,5,7,11,13]
>>> a_mixed_list = [1, 'cow', ['foobar', 5.7], 3.1416]
```

![](https://imgs.xkcd.com/comics/seven.png)

The same indexing and slicing operations that we used for strings apply just as well to lists:
```
>>> a_simple_list[3]
5
>>> a_simple_list[2:5]
[3, 5, 7]
>>> a_mixed_list[-2]
['foobar', 5.7]
>>> a_mixed_list[::-1]
[3.1416, ['foobar', 5.7], 'cow', 1]
```
Note the smaller list nested within `a_mixed_list` kept is original ordering.  It's an element of the list being reversed, so while its position has changed, it is not itself affected.


### Lists and their descriptive functions
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
You may have noticed something unusual about this last line.  I've called two different string functions, `strip` and `split`, and simply concatenated them together.  What's going on here is that `line.strip()` is returning a new string with any `\n` characters removed from the left or right of the calling string, and then we're calling `split` on the new string.  Put another way, the return value of the first function is calling a second function before we discard it (because it's not being assigned to anything).  Here is another way of writing the same set of instructions:
```python
line2 = line.strip('\n')
values = line2.split(delimiter)
```

The list of substrings returned by the `split` command is assigned to a variable that I've named `values`.  Let's run through some list functions by adding them to our script.  As before, let's start with the descriptive list functions.
```python
delimiter ='\t'
handle = open('ClinVar.BRCA1.tsv', 'rU')
_ = handle.readline()  # skip the first line

for line in handle:
    values = line.strip('\n').split(delimiter)
    print(len(values))  # the length of the list
    print(values.count(''))  # count the number of list elements that are empty strings
    print(values[0])  # display the first list element
    break  # exit loop having processed the second line only
    
handle.close()
```

This should result in the following output:
```python
11
3
NM_007294.3:c.(671_4096)ins(300)
```
Illustrative, but not very practical.  Let's use some list indexing to assign some string elements from our list into variables.  Also, suppose that we're dealing with a very large tabular data set with hundreds columns - we are specifically interested in a subset of the columns that we know the labels for beforehand.  For example, suppose the BRCA1 data set is a *lot* larger and we're specifically interested in the variables `Name` and `Clinical significance (Last reviewed)`.  Since the data set is really large, it might not be easy to figure out what the column indices are, *i.e.*, is `Clinical significance` column number 78 or 79?  In this case, we want to parse the header to determine these indices.  Let's revisit our example:
```python
delimiter ='\t'
handle = open('ClinVar.BRCA1.tsv', 'rU')

# locate variables of interest
labels = handle.readline()
name_idx = labels.index('Name')
clin_signif_idx = labels.index('Clinical significance (Last reviewed)')

# use indices to extract values and assign them to variables
for line in handle:
   values = line.strip('\n').split('\t')
   name_val = values[name_idx]
   clin_signif_val = values[clin_signif_idx]
```
This example assumes that we know the *exact* label for the variables we want to work with.  That can be an unreasonable expectation, especially if the labels are complicated.  To make our script a little more robust, let's instruct Python to search for the right label based on some basic information:
```python
clin_signif_idx = None
idx = 0 
for label in labels:
   # convert the label to all lower-case to make our test more robust
   if label.lower().startswith('clinical'):
      clin_signif_idx = idx
      break  # take the first instance only
   idx += 1  # otherwise, add one to index and go to next item in list

if clin_signif_idx is None:
   print ("Failed to index clinical variable from header")
```
The last part of this bit of code is there to warn us if we failed to locate the clinical significance label.  This isn't how I would usually implement this kind of search, but I hope it's a bit easier to follow because the different steps are broken down.  For what it's worth, I would probably do something more like this:
```
indices = filter(lambda x: x.lower().startswith('clinical'), labels)
clin_signif_idx = indices[0] if indices else None
```

![](https://imgs.xkcd.com/comics/code_quality.png)

Indexing values out of the list and assigning them to their own variables is especially useful when we need to do some further processing.


### Building and modifying lists
Recall that String objects are not mutable objects:
```python
>>> bear = 'paddington'
>>> bear[0]
'p'
>>> bear[0]='s'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```
List objects are mutable.  We can also convert a string into a list, and vice versa:
```python
>>> bear = list(bear)
>>> bear
['p', 'a', 'd', 'd', 'i', 'n', 'g', 't', 'o', 'n']
>>> bear[0] = 's'
>>> str(bear)
"['s', 'a', 'd', 'd', 'i', 'n', 'g', 't', 'o', 'n']"
>>> ''.join(bear)
'saddington'
```

To illustrate how we can make use of list mutability, let's construct a list that will contain all *unique* values of clinical significance, excluding the "last updated" suffix.  For brevity I'm going to assume that we already know the index of this variable in the list for each row of the table.
```python
handle = open('ClinVar.BRCA1.tsv', 'rU')
_ = handle.readline()  # skip the first line

unique_clinical = []  # initialize an empty list
for line in handle:
    var_name, _, _, _, clinical_lastrev = line.strip('\n').split('\t')[:5]
    
    # we need to remove the "last reviewed" field
    #  e.g., "Pathogenic(Last reviewed: Oct 2, 2015)"
    if 'reviewed' in clinical_lastrev:
       clinical, last_update = clinical_lastrev.split('(')
    
    if not clinical in unique_clinical:
        unique_clinical.append(clinical)

handle.close()
print (unique_clinical)
```
This script gives the resulting output:
```python
['Pathogenic', 'Uncertain significance', 'Conflicting interpretations of pathogenicity', 'Pathogenic/Likely pathogenic', 'Benign', 'Likely pathogenic', 'Likely benign', 'not provided', 'Conflicting interpretations of pathogenicity, not provided', 'Benign/Likely benign', 'Pathogenic/Likely pathogenic, not provided', 'Benign/Likely benign, not provided']
```
The `append` function adds an object to a list.  The items in this list are in order of appearance in the file (Hollywood-style).  Again, this isn't the best way to go about accomplishing this task -- using a *set* or *dictionary* object would be more efficient -- but it gets the job done.


## This is probably a good point for a break

![](https://imgs.xkcd.com/comics/outreach.png)


## Control flow

### *for* and *while* loops
A big challenge of taking a data-driven approach to learning about Python is that there is a lot of stuff we need to cover before we can start doing anything practical.  One of the general concepts in programming that I've been skirting around is control flow.  Think of running a simple script as water running down a pipe.  We've covered for-loops; these are like pumps that send water upwards for a while.  Another control statement that has a similar effect is the `while` loop:
```python
>>> i = 0
>>> while i < 5:
...     print('pants!')
...     i += 1  # shorthand for `i = i + 1`
... 
pants!
pants!
pants!
pants!
pants!
```
There are a few structural differences between `for` and `while` loops.  In Python, a `for` loop is defined by an iterable object, such as a string or a list.  A `while` loop is defined by a stopping condition.  This can make it slightly more useful than a `for` loop when you need to do something repeatedly until some condition is met, and you can't anticipate how long the loop has to run.  For example, here's a `while` loop that repeats until we get a random integer that's divisible by 7:
```python
>>> import random  # load a module - we'll learn about these later
>>> while True:
...     y = random.randint(0,1000)
...     print(y)
...     if y % 7 == 0:  # modulus operator; 11%7 is 4, the remainder
...         break
... 
683
503
922
244
49
```
Note that the instructions that are being repeated by the `while` loop are indented by some whitespace, just like how we structure our `for` loops.  The whitespace defines the code block affected by the loop.  Off the top of my head, I can't think of a simple way to implement this with a `for` loop.  Also, this `while` loop can *conceivably* go on for a very long time -- I can't think of a simple way to implement a potentially infinite `for` loop.

![](https://imgs.xkcd.com/comics/loop.png)

So far the way we've written loops requires that every pass through the loop evaluates the same set of instructions (not withstanding instructions tucked into an `if` statement).  Some times we need to short-circuit the flow within a loop.  In the example above, I've used a `break` statement that exits out of a `while` loop that would otherwise run on forever.  A `break` will only exit its own loop - it won't affect an outer loop that it is nested within.  For example:
```python
>>> for word in ['one', 'two', 'three']:  # outer loop
...     for letter in word:  # inner loop
...         print(letter)
...         if letter in 'nwr':
...             break  # only exits the inner loop
...     print('')  # print tacks on line break onto empty string
... 
o
n

t
w

t
h
r

```

When we break out of a loop, none of the subsequent iterations get run.  Often, we want to jump back to the top of the loop when a certain condition is met, instead of breaking out of it entirely -- then the loop keeps chugging along as if nothing's happened.  The `continue` statement serves this purpose:
```python
>>> for i in range(10):
...     if i % 2 == 0:
...         continue  # jump to top of loop
...     print(i)
... 
1
3
5
7
9
```

### if-else conditionals

If `for` and `while` loops are like pumps that recycle the water up to a higher section of the pipe, then `if` and `else` statements are like diverters in the pipe -- they split the flow in one direction or another.  Conditional statements are a fundamental component of programming languages, since we usually don't want to do *exactly* the same thing to every value that passes through our instructions.  There are different ways of structuring conditionals.  The simplest is a single `if` statement:
```python
>>> for i in range(5):
...     if i == 3:
...         print('Three.')
...     print(i)
... 
0
1
2
Three.
3
4
```
The second `print` statement is executed *every* time we pass through the loop, but the `if` statement is triggered only *once*.  When we get to the bottom of this `if` statement, we continue on through the rest of the loop as though nothing happened.

You might be wondering about the double-equals sign `==`.  This is different than the assignment operator that uses a single equals sign (`=`).  Instead, it is a test of whether the left side is equivalent to the right side, and returns a `True` or `False` value.  Here are some other tests and logical operators:
```python
>>> a = 5  # assignment
>>> a == 5  # equality test
True
>>> a != 5  # inequality test
False
>>> not a == 5  # inverting the equality test has the same effect
False
>>> a < 6  # is less than
True
>>> a > 6  # is greater than
False
>>> a <= 5  # is equal to or less than
True
>>> a == 'five'  # silly but valid
False
>>> a == 5 and False  # both tests must evaluate True
False
>>> a != 5 or True  # either test can evalute True
True
>>> a == 5 or (True and False)  # use brackets to determine order of operations
True
>>> (a == 5 or True) and False
False
```


Here is a slightly more complicated set of conditional statements:
```python
>>> for i in range(5):
...     if i == 3:
...         print('Three.')
...     else:
...         print(i)
... 
0
1
2
Three.
4
```
The `else` statement is triggered if *none* of the conditions are met -- in this case, there is only one condition.  This structure is more like a pipe diverter; the flow can only go one way or another.  Any instructions you want to be applied to all items in the `for` loop can be placed outside the conditional statements:
```
>>> for i in range(3):
...     print('before')
...     if i == 1:
...         print('One.')
...     else:
...         print(i)
...     print('after')
... 
before
0
after
before
One.
after
before
2
after
```

![](https://imgs.xkcd.com/comics/conditionals.png)

Finally, there are `if..elif..else` sequences.  `elif` is an abbreviation of `else if`:
```python
>>> for i in range(4):
...     if i == 0:
...         print('One!')
...     elif i == 1:
...         print('Two!')
...     else:
...         print('Anything else.')
... 
One!
Two!
Anything else.
Anything else.
```
Since `elif` is an abbreviation of `else if`, we can expand it out to this:
```python
>>> for i in range(4):
...     if i == 0:
...         print('One!')
...     else:
...         if i == 1:
...             print('Two!')
...         else:
...             print('Anything else.')
```
Note there are three levels of indentation here!  Every `elif` saves us a level of indentation.

If you're confused about the difference between these sets of conditional statements, it might help to draw out some flowcharts.
![](https://imgs.xkcd.com/comics/flowchart.png)




## Writing output: formatted strings


