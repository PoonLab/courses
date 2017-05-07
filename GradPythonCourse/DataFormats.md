# Bioinformatic data formats

## Binary and text files
First, let's draw a distinction between plain text and binary files.  All files correspond to a series of 1's and 0's on the hard drive or in memory.  A plain text file has a flag that tells the computer that it should apply a [character encoding](https://en.wikipedia.org/wiki/Character_encoding) that maps binary sequences (bit strings) to symbols, such as characters in an alphabet.  For example, the [ASCII](https://en.wikipedia.org/wiki/ASCII) encoding maps the bit string `1001010` to the letter `J`.  This means that when you open the file, the computer knows that it should display its contents as a collection of meaningful characters.  Obviously this is a big advantage for making a file immediately interpretable.  However, we sacrifice some efficiency to make this possible, so binary files tend to be more compact while storing the same information. 

For a plain text file, a format is a set of rules about how the characters are arranged to encode information.  Data formats are a necessary evil in bioinformatics.  Learning to parse new formats and converting between formats is a ubiquitous task that is often made more difficult by the lack of a strict standardization for popular formats such as [NEXUS](https://en.wikipedia.org/wiki/Nexus_file) or [Newick](https://en.wikipedia.org/wiki/Newick_format).  Fortunately, the pervasiveness of such tasks means that there are also plenty of resources in the public domain that make them easier to accomplish.

![](https://imgs.xkcd.com/comics/binary_heart.jpg)

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
These are aggregate data from a case-control study of esophageal cancer in France.  If you're interested about the study, you can read more about it in the source reference: [Brewlow and Day 1980](https://www.iarc.fr/en/publications/pdfs-online/stat/sp32/).  

How do we record this information in a plain text file?  Typically, we preserve the row structure of the table by placing line breaks between each row.  A [line break](https://en.wikipedia.org/wiki/Newline) is a special character encoding that tells the computer to move to a new line when displaying the content of a text file.  Different operating systems use [different control characters](https://en.wikipedia.org/wiki/Newline#Representations) in the ASCII encoding set to represent a line break: UNIX and its descendants use `LF` (line feed); Apple computers used `CR` (carriage return) until the OS became a UNIX-like system; and Microsoft Windows uses a combination of `LF` and `CR`.  This frequently causes problems when passing data files originating from different computers between programs that were developed on different platforms!  If you are trying to process a data file with a program and it isn't working, this is a possible cause.

We still have to deal with preserving the column structure of a tabular data set.  This is usually accomplished with a [delimiter](https://en.wikipedia.org/wiki/Delimiter): a character or sequence of characters that is used to separate content that belongs to different items.  The comma `,` is probably the most common delimiter, closely followed (if not surpassed) by the [tab character](https://en.wikipedia.org/wiki/Tab_key#Tab_characters), which is represented by the escape character `\t`.  To illustrate, here is how our `esoph` data would appear in a comma-separated values (CSV) file:
```
agegp,alcgp,tobgp,ncases,ncontrols
75+,40-79,0-9g/day,2,5
75+,40-79,10-19,1,3
35-44,80-119,10-19,0,6
65-74,80-119,10-19,4,12
55-64,40-79,30+,3,6
45-54,120+,10-19,3,4
55-64,120+,20-29,2,3
25-34,80-119,30+,0,2
55-64,40-79,20-29,4,17
55-64,80-119,10-19,8,15
```

and here is the same data set as a tab-separated values (TSV) file:
```
agegp	alcgp	tobgp	ncases	ncontrols
75+	40-79	0-9g/day	2	5
75+	40-79	10-19	1	3
35-44	80-119	10-19	0	6
65-74	80-119	10-19	4	12
55-64	40-79	30+	3	6
45-54	120+	10-19	3	4
55-64	120+	20-29	2	3
25-34	80-119	30+	0	2
55-64	40-79	20-29	4	17
55-64	80-119	10-19	8	15
```

An important feature of these formats is that the first line is being used to store the column labels.  This is often referred to as the *header row*.  Including the header row is optional in a CSV or TSV file, but it is important to be aware of whether it is present or absent when you are processing the file.  

A tabular data file should have the same number of items on each line.  If a line has more items than another, then the assignment of items to the various columns becomes ambiguous (especially if the data are similar types, such as a large set of numbers).  In other words, did we append an extra number to the left, or the right, or some where in the middle?  

What happens if our data includes entries that contain the delimiter?  For example, suppose that our data set includes text fields that contain a description of symptoms, such as: `muscular pain, acute`.  This creates the exact problem that we just described!  Fortunately, this format is so widely used, and this problem so common, that there is a standardized solution: we enclose the affected item in double quotes.  In other words, this row:
```
67,muscular pain, acute,Toronto
```
becomes this:
```
67,"muscular pain, acute",Toronto
```

![](https://imgs.xkcd.com/comics/file_extensions.png)



## Working with tabular data files in Python

Okay, let's use `cd` and `ls` to navigate to the `examples` folder.  I've placed a CSV file derived from the `esoph` R data set, which I've uncreatively named `esoph.csv`:
```shell
[Elzar:~/git/courses] artpoon% pwd
/Users/artpoon/git/courses
[Elzar:~/git/courses] artpoon% cd GradPythonCourse/
[Elzar:~/git/courses/GradPythonCourse] artpoon% cd examples/
[Elzar:courses/GradPythonCourse/examples] artpoon% ls
esoph.csv
```

Use the `head` command to have a quick look at the contents of this file:
```
[Elzar:courses/GradPythonCourse/examples] artpoon% head -n5 esoph.csv 
agegp,alcgp,tobgp,ncases,ncontrols
25-34,0-39g/day,0-9g/day,0,40
25-34,0-39g/day,10-19,0,10
25-34,0-39g/day,20-29,0,6
25-34,0-39g/day,30+,0,5
```

Now let's fire up an interactive session with Python.  
```shell
[Elzar:courses/GradPythonCourse/examples] artpoon% python
Python 3.6.0b3 (default, Nov  1 2016, 16:08:38) 
[GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

The first thing we need to do is to open the file.  This is accomplished with the built-in Python function `open`:
```python
>>> handle = open('esoph.csv', 'rU')
```
Before we talk about what's happening here, we need to talk a bit about functions and variables.


### Intermission - working with Python functions
Since this may be the first time you've encountered a function call in Python (or even in any programming language!), I need to take a minute to explain some basic concepts.  A function is a set of instructions in the programming language that we've asked the computer to set aside and label with a name.  Whenever we call that name, the computer will know to run that set of instructions.  Functions become really useful if you can apply the same set of instructions to different things.  We pass those things to a function as "arguments".  There are two arguments being passed to the `open` function in this example:
1. `'esoph.csv'` is a string (sequence of characters) that corresponds to a relative path to the file.  Since we initiated our Python session in the same directory as the file, we don't need to specify any other directories.
2. `'rU'` is another string that tells Python to open the file in "read-only" mode (`r`) and to interpret the stream of ones and zeros being transmitted from the file with a Unicode encoding `U`.  
How are we supposed to know what arguments to pass to a function?  You need to use another built-in Python function called `help`:
```python
help(open)
```

This spawns another interactive shell for viewing the help documentation for the `open` function:
```shell
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise IOError upon failure.
```
There's actually many more lines than this!  This shell works the same way as `less` and `man`: you can scroll up and down with the arrow keys, and return to your Python session at any time by typing `q`.  The first line of the help document provides some concise information about how to use the function (to get more detailed information, keep reading!).  There are 8 different arguments that can be passed to the `open` function.  There is only 1 argument that doesn't have a default value: `file`.  That is what we use to specify an absolute or relative path to the file that we want to open a stream from. The `mode` argument is the only one that I've ever used in practice.  Note that it defaults to a read-only mode (`r`).  This is good behaviour - if it defaulted to a write mode (`w`), then you'd wiped out every file you tried to open! 

### Another intermission - Variables
Functions usually have *return values* --- they pass something back to you when they've completed their task.  You need to capture this return value by assigning it to a variable.  Variables are a fundamental concept in programming - a variable is an agreement between you and the computer to refer to something with a name that you've both agreed on:
```python
>>> sandwich = 3
>>> sandwich
3
```
What just happened here?  We've named a variable `sandwich` and assigned to it the integer value `3`.  Python interprets the equal sign `=` as a directive to assign the value on the right side to a variable on the left side.  I think most programming languages follow this right to left convention, although there are different notations used for variable assignment.  For example, *R* uses a notation (`<-`) that is less ambiguous.

Second, entering the variable name by itself is requesting Python to print the value associated with the variable.  Since we just assigned the integer value `3` to our variable, that's what is printed out.

Let's try messing around with Python a bit:
```python
>>> 2=3
  File "<stdin>", line 1
SyntaxError: can't assign to literal
```
This is an error because we can't use `2` as a variable.  It has a fixed value, which is what the error statement means when it's referring to it as a literal object.  Let's try something else:
```python
>>> 2two=3
  File "<stdin>", line 1
    2two=3
       ^
SyntaxError: invalid syntax
```
Python didn't like this because it has strict rules about variable names.  It doesn't allow variable names to have any characters other than `_`, `A` to `Z`, `a` to `z`, and `0` to `9`, and the name cannot start with a digit.  These rules have to exist because if our variable name contains a character that has another role in the language, such as `=`, then Python is going to get confused!

When a function returns a value, you need to assign this value to a variable.  When there are multiple return values, you can provide an equal number of variables to assign them to.  Otherwise, they will be assigned to a single variable as a collection of objects such as a [tuple](https://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences).


### Back to our regular programming

Okay, let's go back to this situation:
```python
>>> handle = open('esoph.csv', 'rU')
```
Calling the `open` function caused Python to open a stream to the file named `esoph.csv`.  Since this file is in the present working directory (typically where our shell was located in the file system when we triggered an interactive Python session), we don't have to specify an absolute or relative path to the file.  

Think of a stream as a binary sequence of ones and zeros that are being read off the storage device.  The stream always starts at the beginning of the file; it can't start somewhere in the middle.  By default, Python will interpret a file stream in read mode using the Unicode encoding.  Once you've moved forward in the stream, you can't easily go back.  It's possible, but it requires calling functions that we won't cover in this course.

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
This is valid Python, but it's also stupid.  No, we're going to have to learn about `for` loops.


## for loops

