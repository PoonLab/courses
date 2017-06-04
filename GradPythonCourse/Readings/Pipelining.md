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
generates a listing of Markdown files in the `Readings` folder, where I'm using the bash *echo* command to write each parameter value to the console. 

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
The first line of our script imports the `sys` module, which provides access to system-level resources.  You can read more about this module [here](https://docs.python.org/3/library/sys.html).  The second line is displaying a special variable that belongs to the `sys` module, called `argv`, which is short for "argument vector".  A vector is an ordered sequence of things that we represent in Python as a list or tuple; in this case, it is a list (note the square brackets).  The list has only one value: the name of the script that we called the interpreter on.  


