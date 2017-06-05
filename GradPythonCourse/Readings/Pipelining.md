# Pipelining

## Outline

* Calling one script on many files with bash
* Calling many scripts - pipelining
* Calling other programs - subprocessing
* Harnessing multiple cores with MPI

## Background

One of the key advantages of scripting is that you can automate a great many computing tasks.  This makes your analysis reproducible, which is critical for robust science.  Having a script also makes it easy to apply the same analysis to a very large number of data files, which is a common task that is often referred to as "batch processing".  In addition, we can link together a series of different scripts to process a data set, through intermediate steps until we obtain the final product.  This series of scripts is often referred to as a "pipeline".  In this class, we're going to talk about different approaches to pipelining, and how to make use of multi-core architectures to speed up the processing of data sets with a pipeline.  

![](https://imgs.xkcd.com/comics/automation.png)

## Batch processing with `bash`

The `bash` command language has a framework for repeating a set of commands on a number of inputs.  For example, here is a `bash` command for counting from `1` to `10`:
```bash
art@Shinji:~$ for i in {1..5}; do echo $i; done
1
2
3
4
5
```
Unfortuntately the shell in Apple's *macOS* does not reproduce this script; you have to create a text file and run it with the `bash` command, *e.g.,* `bash foo.sh`.

To make this iteration useful, we want to adapt this command to iterate over a list of files.  We [already know](basicunixcommands.md) how to get a listing of files in UNIX: `ls *`.  Suppose we have a bunch of files in the current working directory that share the suffix `*.csv`.  We can get a list of these files with the command `ls *.csv`.  Now, how can we use this list for iteration in a bash script?  The answer is that we need to make use of backticks (\`).  A bash command enclosed in backticks will be evaluated before the outer commands.  For example:
```bash
art@Shinji:~/git/courses/GradPythonCourse$ cd Readings/
art@Shinji:~/git/courses/GradPythonCourse/Readings$ for f in `ls *.md`; do echo $f; done
basicunixcommands.md
DateTime.md
Dictionaries.md
...
```
generates a listing of Markdown files in the `Readings` folder, where I'm using the bash *echo* command to write each parameter value to the console.  Calling `echo` isn't terribly useful; we're just apeing the basic functionality of `ls`.  For a slightly more useful example, let's call the `wc -l` command to get the number of lines for each Markdown file:
```shell
art@Shinji:~/git/courses/GradPythonCourse/Readings$ for f in `ls *.md`; do wc -l $f; done
235 basicunixcommands.md
47 DateTime.md
160 Dictionaries.md
29 Pipelining.md
337 RegularExpressions.md
137 ScriptingLanguages.md
375 SequenceData.md
655 TabularData2.md
543 TabularData.md
```

We can use this bash command to perform some simple batch processing, where we're calling some python script `foo.py` on each file in the list.  However, this requires that we have written a script that will take input from the command line.  So far, we've been simply hard-coding the input file into a script, like this:
```python
handle = open('local-file.csv', 'rU')
# do stuff with the file
handle.close()
```
This isn't useful for batch processing, because we want to change the file path in our `open()` command.


## Getting arguments with `sys.argv`
Recall that when we call an executable on the command line, we can follow the name of that executable with arguments that alter the behaviour of that executable.  For example, `ls` generates a tabular listing of files and directories, whereas setting the `-l` option generates a long listing:
```shell
art@Shinji:~/git/courses$ ls -l
total 84
drwxrwxr-x 2 art art  4096 Jun  4 13:09 BIOL4289B
drwxrwxr-x 2 art art  4096 Jun  4 13:09 css
drwxrwxr-x 5 art art  4096 Jun  4 13:09 Cuernavaca
drwxrwxr-x 2 art art  4096 Jun  4 13:09 failureToLaunch
```
Similarly, when we invoke our Python script by calling the interpreter, we are passing a single argument -- a relative or absolute path to the script we want to run.  Remember that the Python interpreter is just another binary executable that usually lives at `/usr/bin`.  (To find out exactly, enter the command `which python`.)  Let's write a script that will reveal this information:
```python
import sys
print ("Python was called with these arguments: {}".format(sys.argv))
```
Write these two lines into a file, save it as `argv.py` and run it from the command line.  You should get some output like this:
```shell
art@Shinji:~/git/courses/GradPythonCourse/examples$ python argv.py 
Python was called with these arguments: ['argv.py']
```
The first line of our script imports the `sys` module, which provides access to system-level resources.  You can read more about this module [here](https://docs.python.org/3/library/sys.html).  The second line is displaying a special variable that belongs to the `sys` module, called `argv`, which is short for "argument vector".  A vector is an ordered sequence of things that we represent in Python as a list or tuple; in this case, it is a list (note the square brackets).  The list has only one value: the name of the script that we called the interpreter on.  If I start an interactive session of Python, I have an empty argument vector:
```python
>>> import sys
>>> sys.argv
['']
```

We can pass a bunch of random stuff on the command line and see the results with our new script:
```shell
art@Shinji:~/git/courses/GradPythonCourse/examples$ python3 argv.py I want to see this stuff
Python was called with these arguments: ['argv.py', 'I', 'want', 'to', 'see', 'this', 'stuff']
```
Note that each "argument" was converted into a string object.  If I pass numbers, they will also be interpreted as strings by default.  If I want to do some math with these values, I'll have to cast them using `int` or `float`.  I can't pass arguments to Python when calling an interactive session, because it expects the first argument to be a path to a script.  
```shell
art@Shinji:~/git/courses/GradPythonCourse/examples$ python boogabooga
python: can't open file 'boogabooga': [Errno 2] No such file or directory
```

We can refer to individual members of `sys.argv` with the usual indexing method because it's just an ordinary list.  Let's edit our little script to extract the first member of the argument vector and assign it to a variable:
```python
import sys
print ("Python was called with these arguments: {}".format(sys.argv))
filename = sys.argv[1]
handle = open(filename, 'rU')
print(handle.readline())  # show the first line
handle.close()
```
Remember, the first member of the list is the script, so we're going straight to the second (zero-index `1`).  
Let's see this script in action:
```shell
art@Shinji:~/git/courses/GradPythonCourse/examples$ python argv.py Decapod-PEPCK.fa 
Python was called with these arguments: ['argv.py', 'Decapod-PEPCK.fa']
>EU427182.1 Albunea holthuisi phosphoenolpyruvate carboxykinase (PEPCK) gene, partial cds
```
What if we forget to add the additional argument?  Python returns an error:
```shell
art@Shinji:~/git/courses/GradPythonCourse/examples$ python argv.py
Python was called with these arguments: ['argv.py']
Traceback (most recent call last):
  File "argv.py", line 3, in <module>
    filename = sys.argv[1]
IndexError: list index out of range
```
An `IndexError` is Python's way of telling us that we just tried to access a member of a list at an index that doesn't exist.  

We've just made our script more versatile - it can be called on any file!  This is perfect for batch processing with bash.  To illustrate, let's first edit our `argv.py` script a little:
```python
import sys

filename = sys.argv[1]
handle = open(filename, 'rU')
first_line = handle.readline()
handle.close()

output = "Filename: {}\nFirst line:\n{}".format(filename, first_line)
print(output)
```
Now we can call the script iteratively with bash:
```shell
art@Shinji:~/git/courses/GradPythonCourse/examples$ for f in `ls ../Readings/*.md`; do python argv.py $f; done
Filename: ../Readings/basicunixcommands.md
First line:
# A brief introduction to *nix

Filename: ../Readings/DateTime.md
First line:
# Date and time objects in Python
```
where I've truncated the output to the first few lines.

This is pretty good for batch processing with multiple inputs.  What if we want to write multiple outputs?  If we fix an output file to write results to, then we're going to wipe out that file every time we call our script.  For example, let's modify `argv.py` as follows:
```python
import sys

filename = sys.argv[1]
handle = open(filename, 'rU')
first_line = handle.readline()
handle.close()

output = "Filename: {}\nFirst line:\n{}".format(filename, first_line)
outfile = open('wrong-way.txt', 'w')
outfile.write(output)
outfile.close()
```
and let's use the same bash command to call our script on every Markdown file in the `Readings` directory.  Use `cat` to examine the contents of the `wrong-way.txt` file that results:
```shell
art@Shinji:~/git/courses/GradPythonCourse/examples$ cat wrong-way.txt 
Filename: ../Readings/TabularData.md
First line:
# Working with tabular data in Python
```
As we expected, we only see the output produced when `argv.py` was called on the *last* Markdown file.

There are a few things we can do here:
1. We can open the output file in *append* mode (`a`) instead of *write* mode (`w`):
   ```python
   outfile = open('wrong-way.txt', 'a')
   ```
   This results in a complete output file.  For simple batch processing, this can be sufficient but there are a couple of drawbacks.  First, we need to make sure that the output file is either empty or does not exist - otherwise, anything that was already in the file will remain there!  Second, it might not be easy to associate each output back to its input file.
   
2. Derive an output filename from each input filename.
   ```python
   outfile = open(filename.replace('.md', '.txt'), 'w')
   ```
   This can be better for more complex batch processing where we might want to make sure that the output derived from each input file is kept separate from other outputs.  However, this approach can be dangerous - if you make a mistake specifying the output file path, then you may end up overwriting the input files!  


# Batch processing with Python - `glob`




