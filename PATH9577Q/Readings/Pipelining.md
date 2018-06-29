# Pipelining

## Outline

* Calling one script on many files with bash
* Calling many scripts - pipelining
* Calling other programs - subprocessing
* Harnessing multiple cores

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
Actually, we can get the same output if we run `wc -l *.md`, but many programs will not interpret UNIX wildcards this way.

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
   
3. Skip using bash altogether and generate a list of files within Python's `glob` module.


## Batch processing with Python - `glob`

A *glob* is kind of like a [regular expression](RegularExpressions.md) - it is a special string that represents one or more other strings.  We've already been using globs to refer to multiple files in UNIX-like systems:
```shell
art@Shinji:~/git/courses/GradPythonCourse/examples$ ls ../Readings/*.md
../Readings/basicunixcommands.md   ../Readings/ScriptingLanguages.md
../Readings/DateTime.md            ../Readings/SequenceData.md
../Readings/Dictionaries.md        ../Readings/TabularData2.md
../Readings/Pipelining.md          ../Readings/TabularData.md
../Readings/RegularExpressions.md
```

Here, we've used the symbol `*` to indicate that we want *all* files whose names end with `.md`.  This symbol is called a *wildcard*.  There are several wildcards that can be used in glob expressions:

| Wildcard | Matches |
|----------|---------|
| `*` | Any character or sequence of characters |
| `?` |  Any single character |
| [abc] | Any single character in the set |
| [a-z] | Any single character in the defined range |

For example, we can use a glob to list all Markdown files that begin with a `T`:
```shell
art@Shinji:~/git/courses/GradPythonCourse/Readings$ ls T*.md
TabularData2.md  TabularData.md
```
I've noticed that in Ubuntu, my globs are not case-sensitive:
```shell
art@Shinji:~/git/courses/GradPythonCourse/Readings$ ls [A-D]*.md
basicunixcommands.md  DateTime.md  Dictionaries.md
```

To illustrate, let's create a new file called `batching.py`:
```python
from glob import glob
files = glob('../Readings/*.md')
print(files)
```

Calling our script yields the following output:
```shell
art@Shinji:~/git/courses/GradPythonCourse/examples$ python batching.py 
['../Readings/Dictionaries.md', '../Readings/DateTime.md', '../Readings/ScriptingLanguages.md', '../Readings/TabularData2.md', '../Readings/basicunixcommands.md', '../Readings/Pipelining.md', '../Readings/SequenceData.md', '../Readings/TabularData.md', '../Readings/RegularExpressions.md']
```
Our script is brittle - it cannot be called from another directory:
```shell
art@Shinji:~/git/courses/GradPythonCourse/examples$ cd ..
art@Shinji:~/git/courses/GradPythonCourse$ python examples/batching.py 
[]
```
We can fix this by using an absolute path in our glob expression instead of a relative one.  However, this makes the script less portable - I like to use the same directory structure for copies of the same project on multiple computers, but the absolute paths may differ between systems (*e.g.,* **macOS** uses `/Users` instead of `/home`) or user accounts.

## Example - Diabetes data

The [UC Irvine Machine Learning Repository] hosts a number of data sets in the public domain for the development and comparison of machine learning algorithms.  One of these data sets ([link](https://archive.ics.uci.edu/ml/datasets/diabetes)) comprises records for 70 individuals with diabetes - these records were derived either from an electronic device or from paper records.  These are tabular data sets with tab-separated values.  Here is an excerpt from one of the data sets:

| Date       | Time  | Code | Value |
|------------|-------|----|----|
| 07-13-1990 | 11:36 | 57 | 84 |
| 07-13-1990 | 11:39 | 33 | 3 |
| 07-13-1990 | 16:43 | 65 | 0 |
| 07-13-1990 | 16:44 | 66 | 0 |
| 07-13-1990 | 16:44 | 62 | 180 |

The codes can be interpreted with a map that is contained in the *README* file; here is an excerpt:
```
33 = Regular insulin dose
34 = NPH insulin dose
35 = UltraLente insulin dose
48 = Unspecified blood glucose measurement
57 = Unspecified blood glucose measurement
```

If we apply the map to the excerpt above, we get the following sequence of events:
1. Subject 43 took a blood glucose measurement (84 mmol/L) and subsequently took an insulin dose.  
2. About five hours later, they experienced hypoglycemic symptoms.  They took a glucose measurement (180 mmol/L) and then ate dinner.

There are a total of 29,330 lines in these data sets.  

Here is a script that has three objectives:
1. Convert the date fields into standard ISO format (`YYYY-MM-DD`).
2. Translate codes into text.
3. Write the result as a CSV file.
Let's call the script `ParseDiabetesTSV.py`.

```python
import re
import sys

mdy = re.compile('(\d{2})-(\d{2})-(\d{4})')

codes = {
    '33': "Regular insulin dose", 
    '34': "NPH insulin dose", 
    '35': "UltraLente insulin dose", 
    '48': "Unspecified blood glucose measurement", 
    '57': "Unspecified blood glucose measurement", 
    '58': "Pre-breakfast blood glucose measurement", 
    '59': "Post-breakfast blood glucose measurement", 
    '60': "Pre-lunch blood glucose measurement", 
    '61': "Post-lunch blood glucose measurement", 
    '62': "Pre-supper blood glucose measurement", 
    '63': "Post-supper blood glucose measurement", 
    '64': "Pre-snack blood glucose measurement", 
    '65': "Hypoglycemic symptoms", 
    '66': "Typical meal ingestion", 
    '67': "More-than-usual meal ingestion", 
    '68': "Less-than-usual meal ingestion", 
    '69': "Typical exercise activity", 
    '70': "More-than-usual exercise activity", 
    '71': "Less-than-usual exercise activity", 
    '72': "Unspecified special event"
}

def standardize_date(dt):
    """ Convert MM-DD-YYYY format to ISO standard YYYY-MM-DD """
    matches = mdy.findall(dt)
    if not matches:
        print ("ERROR: Failed to parse date {}".format(dt))
        sys.exit()
    month, day, year = matches[0]
    isodate = '{}-{}-{}'.format(year, month, day)
    return isodate

def translate_code(code):
    """ Use dictionary to map code to a brief description """
    desc = codes.get(code, None)
    if not desc:
        print ("ERROR: Encountered unknown code {}".format(code))
        sys.exit()
    return desc

def main(tsv):
    """ Main function for parsing TSV file """
    handle = open(tsv, 'rU')
    outfile = open(tsv+'.csv', 'w')
    
    for line in handle:
        date, time, code, value = line.strip('\n').split('\t')
        isodate = standardize_date(date)
        desc = translate_code(code)
        outfile.write(','.join([isodate, time, desc, value]) + '\n')
        
    outfile.close()
    handle.close()    
```

Now let's write another script that will utilize the functions defined in `ParseDiabetesTSV.py` to perform batch processing.  How do we begin?


## Pipelining with multiple scripts

So far we've assumed that we are applying a single script to our data with batch processing.  This is good enough in many situations, but for more complex tasks we may want to call on more than one script.  A sequence of scripts is often called a pipeline.  Pipelines play a central role in bioinformatics, and some pipelines have become a core method of emerging fields.  For example, [QIIME](http://qiime.org/scripts/) is essentially a collection of Python scripts for working with metagenomic data for microbial ecology.  

A pipeline is essentially a recipe for applying some sequence of scripts and programs to your data set.  It is helpful to implement your pipeline as a sort of "meta" script, because this creates a record of how you process your data.  Otherwise, it may be easy to mix up the sequence of analyses, leading to inconsistent results.  Pipelines can be written as a bash script:
```bash
python script1.py input.txt output1.txt
python script2.py output1.txt output2.txt
python script3.py input.txt output2.txt output3.txt
```
or as a Python script:
```python
import sys
import script1
import script2
import script3

input = sys.argv[1]
output1 = input.replace('.txt', '.out1')  # modify file path
script1.run(input, output1)

output2 = input.replace('.txt', '.out2')
script2.run(output1, output2)

output3 = input.replace('.txt', '.out3')
script3.run(input, output2, output3)
```
This fake Python pipeline script assumes that the scripts comprising the pipeline are in the same working directory.  

> **Exercise:**  Break up `ParseDiabetesTSV.py` into two scripts and write a pipeline script to apply them to the data.


## Calling other programs with `subprocess`

So far we've covered how build pipelines and carry out batch processing with Python scripts.  However, not everything is done with Python!  Sometimes it is useful or even necessary to run your data with someone else's program that has been compiled from C or Java, for example.  These can be important steps in a pipeline.  That doesn't mean that we stop the pipeline there and then pick up again afterwards.  We can still automate the process of calling a binary executable (program) on a data set.  The recommended way of doing this is with Python's `subprocess` module.  Its name emphasizes the fact that our current process (running Python) is spawning a child process or subprocess that will run another program.  

Automation with subprocesses can be complicated.  We are responsible for:
* starting the subprocess
* sending data to that subprocess
* waiting for that subprocess to finish working with the data
* receiving output from the subprocess
* handling errors raised by the subprocess
* closing the subprocess when it is finished
For example, if we close the subprocess before it is finished, then we lose its output.  

Let's start with importing the `subprocess` module and running some basic commands:
```python
>>> import subprocess
>>> exit_code = subprocess.check_call(['ls', '-l'])
...
>>> exit_code
0
```
An exit code of `0` means normal operation.  Any non-zero code means that there was some kind of error.  Note that the directory listing was streamed onto our console.  We haven't captured it as a variable, so we can't do anything with it.  In order to capture this stream, we can use the `check_output` command:
```python
>>> stdout = subprocess.check_output(['ls', '-l'])
>>> stdout
b'total 429196\n-rw-rw-r-- 1 art art   1186681 Apr 21 23:14 Canada.txt\n-rw-r--r-- 1 art art 162321443
```
Note that this line contains line break characters `\n`.  Also note that the string is prefixed with a `b`, which indicates that this is a [byte string](https://docs.python.org/3/reference/lexical_analysis.html#strings).  A byte string can only contain [ASCII](https://en.wikipedia.org/wiki/ASCII) characters.

If you try to pass a UNIX wildcard to `ls` via subprocess, you get an error:
```python
>>> stdout = subprocess.check_output(['ls', '-l', '*.py'])
ls: cannot access '*.py': No such file or directory
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.5/subprocess.py", line 626, in check_output
    **kwargs).stdout
  File "/usr/lib/python3.5/subprocess.py", line 708, in run
    output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['ls', '-l', '*.py']' returned non-zero exit status 2
```
What's going on?  Python is not passing this command through a shell interpreter that would handle the UNIX wildcard, so the string `*.py` is being taken literally - the `ls` program is looking for a file with a name that starts with an asterisk.  Why is this happening?  There is a security risk in running commands through a shell interpreter from Python that is called an [injection attack](https://en.wikipedia.org/wiki/Code_injection#Shell_injection).  Much of the risk from shell injection can be avoided by not running `subprocess` commands through the shell.  Furthermore, this security risk is the reason that commands are passed as lists instead of a single string, *i.e.*, `['ls', '-l']` instead of `ls -l`.

![](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)

In sum, we can use the `subprocess` module to call external programs such as `MUSCLE` or `bowtie2` and capture the output as a Python object.  The functions `check_call` and `check_output` are convenient methods for handling return codes and the content of the stdout stream.  However, if the output is massive then it helps to break the stream down to individual lines instead of loading the entire contents into memory, much the way we would handle a large file.  We can do this with a lower level function of `subprocess` called `Popen`.  For example, here is a Python script that will call `bowtie2` on a FASTQ file and process the output stream:
```python
import subprocess
import sys

path = sys.argv[1]  # path to unpaired FASTQ file
refpath = 'chr7'
outfile = path.replace('.fastq', '.sam')
handle = open(outfile, 'w')

p = subprocess.Popen(['bowtie2', '--quiet', '-x', refpath, '-U', path, '--local'], stdout=subprocess.PIPE)
for line in p.stdout:
    if line.startswith('@'):
        handle.write(line)  # carry over header line
        continue

    _, _, rname, _, mapq = line.split('\t')[:5]
    if rname == 'chr7' and int(mapq) > 10:
        # only keep reads that mapped to chr7 with decent quality
        handle.write(line)

handle.close()
```
This type of script is sometimes called a "wrapper script", because it is wrapping around another program, which provides an opportunity to sanitize and regularize the inputs, and to parse the outputs "online" (as the other program generates the output).  


## Using multiple cores

Most computers today have processors with multiple cores - each core is an independent processing unit.  Having multiple cores enables the CPU to handle multiple processes at the same time.  For day-to-day programming, this provides a huge benefit because you can run processes like your web browser or music player in the background while performing other tasks with little to no impact on computing performance.  For bioinformatics, using multiple cores can be extremely useful for large data sets or batch processing many data sets.  This is referred to as [parallel computing](https://en.wikipedia.org/wiki/Parallel_computing).  

However, taking advantage of multiple cores requires the programmer to tell the computer how different tasks are supposed to be distributed across the cores.  There are a few ways of doing this.  I tend to use the [message passing interface](https://en.wikipedia.org/wiki/Message_Passing_Interface) (MPI) protocol for parallel computing, but this would probably require you to install an implementation of MPI such as [OpenMPI](https://www.open-mpi.org/) or [MPICH](https://www.mpich.org/), as well as the excellent [mpi4py](http://pythonhosted.org/mpi4py/) module.  Instead, we'll talk about Python's [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html) module, which is included in the base distribution of Python.

Running multiple processes concurrently creates a host of potential problems.  Which tasks go to which processes, and what are they going to do when they've completed their respective tasks?  Who gets access to specific objects?  What happens when two processes want to write to the same file on the hard drive?  Since we can easily get beyond the scope of this class with these problems, we're going to focus on the simplest task of farming out a set of *N* tasks to *M* processes.  We'll assume that the processes don't have to communicate with other processes once they've been given their list of tasks.  The `multiprocessing` module takes care of many of these issues.

### Pool

The `Pool` object from the `multiprocessing` module creates a pool of worker processes that partition a set of tasks for parallel computing.  Here is a simple example:
```python
from multiprocessing import Pool, TimeoutError
from time import time
import os

def chaos(x, depth=1000000):
  for i in range(depth):
    x = 3.71 * x*(1-x)
  return x

if __name__ == '__main__':
    # solve with single process
    t0 = time()
    for i in range(1, 10):
        print(chaos(0.1*i))
    t1 = time()
    print ("single process consumed {} seconds".format(t1-t0))

    # start 4 worker processes
    with Pool(processes=4) as pool:
        t0 = time()
        print(pool.map(chaos, [0.1*x for x in range(1,10)]))
        print ("multiprocess consumed {} seconds".format(time()-t0))
```
Here is the output of this script:
```
0.7114574649127849
0.8279692074428943
0.709192872087976
0.4926733572846207
0.8725565654535977
0.8154038994007364
0.7235149052994692
0.8279692074428943
0.5925503469981489
single process consumed 1.204334020614624 seconds
[0.7114574649127849, 0.8279692074428943, 0.709192872087976, 0.4926733572846207, 0.8725565654535977, 0.8154038994007364, 0.7235149052994692, 0.8279692074428943, 0.5925503469981489]
multiprocess consumed 0.40645694732666016 seconds
```
The multiprocess version is about three times faster.  This might not seem like a big deal, but for a month-long analysis this means that you can get your results in about a week.  If you're running high-performance hardware, then your computer may boast upwards of 10 cores each capable of running two threads each -- this can translate into a 20-fold speed gain!

The `chaos` function is making use of the chaotic behaviour of the [logistic formula](https://en.wikipedia.org/wiki/Logistic_map#Chaos_and_the_logistic_map) to provide a simple but time-consuming numerical problem that does not converge towards an answer.  

In order to understand what's going on in the rest of this script, we have to explain this line:
```python
if __name__ == '__main__':
```
This tells Python what to run if the script is being called from the command line.  Why is this necessary?  When Python sends jobs to the worker processes, they each run the script.  If we don't block off the lower portion of the script spawning a pool of worker processes, then our script could cascade into an infinite number of processes!  Hence, we need to protect this block of code from being executed by the worker processes.

What about this line?
```python
pool.map(chaos, [0.1*x for x in range(1,10)])
```
Here, `pool` is a `Pool` object from the `multiprocessing` module.  `map` is one of its functions that applies the first argument, which should be a function, to every item in the second argument, which should be an iterable object.  In our example, the iterable is `range(1,10)` that is simply the integers from `1` to `9`.  I'm using a list comprehension to convert these integers to the floats `0.1` through `0.9`.  This gives me a range of points along the interval `(0,1)` where my logistic function is defined.  

![](https://imgs.xkcd.com/comics/here_to_help.png)
