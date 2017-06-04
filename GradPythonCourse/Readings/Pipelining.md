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
generates a listing of Markdown files in the `Readings` folder, where I'm using the bash *echo* command to write each parameter value to the console.  To 

