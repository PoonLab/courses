# More complex text processing

## Python modules

A module is a collection of functions and objects in Python.  There are many modules that are distributed with Python that are not loaded by default, and thousands of others that are developed by people and distributed as open-source software.  To load a module, you just use the `import` command:
```python
import os
```
and all the `sys` functions and objects will become available for you to use.  To see what's been loaded with the module, use the `dir` command:
```python
>>> dir(os)
['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_TRAPPED', 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', ...
```
and to find out what each function or object does, use the `help` command:
```python
>>> help(os.system)
```
Remember that the `help` command causes your session to enter another shell for viewing the help documentation, and that to exit this shell, you need to enter `q` to quit and return back to an interactive Python session.

For this class we're going to cover a couple of modules that are especially useful for working with text-based data.  Next class we'll talk about two other modules that are good for working with numbers.


## Regular expressions

A regular expression is a representation of a subset of all possible strings.  It is a concept that originates from linguistics, particularly computational linguistics (natural language processing) and the study of breaking a language down into a strict (formal) set of rules that can be encoded for a machine.

Regular expressions (or *regex*es, for short) are extremely useful when you are dealing with complex data comprising strings.  We can screen a set of strings for those that match the regex, capture parts of those strings and then use those parts to rewrite the string.

## Date and time data

##