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

A regular expression is a representation of a subset of all possible strings, called a *pattern*.  The concept of regular expressions originates from linguistics, particularly the field of computational linguistics (natural language processing), the study of breaking a language down into a strict (formal) set of rules that can be encoded for a machine.

Regular expressions (or *regex*es, for short) are extremely useful when you are dealing with text-based data sets.  We can screen a set of strings for those that match the regex, capture parts of those strings, and then use those parts to rewrite the string.  It doesn't sound like much, but it is a big deal.

![](https://imgs.xkcd.com/comics/regular_expressions.png)

A regular expression is defined by inserting special characters into the string.  Many of these are characters that we would normally want to use for their original meaning, such as the round brackets `(` and `)`.  To tell Python that we want to use brackets in the "normal" way, we need to use the escape symbol `\` like we do for line breaks (`\n`):
"""
"\(like this\)"
"""
Unforunately, there are different kinds of regular expressions.  Python use Perl-style regular expressions.

To load the regular expressions module, type:
```python
>>> import re
```


### Defining groups

A group matches any of a subset of characters.  It is defined by square brackets.  For example, `"c[aou]t"` matches `"cat"`, `"cot"` and `"cut"`, but not `"cet"`.  It also does not match `"bat"`, because the pattern expects the group to have a `'c'` on the  left and a `'t'` on the right.

Some times you want to specify a large range of characters in a group.  To save you the trouble of typing all of those characters in, regular expressions have a range syntax: `"[x-y]"` where `x` and `y` are the inclusive limits of the range.  For example, `"[a-z]"` is the subset of all lower case characters in the alphabet.  `"[0-9]"` is all the digits.

You can specify a partial range.  `"[A-C]"` matches `'A'`, `'B'`, and `'C'`, but not `'D'`.  You can also concatenate ranges.  For example, `"[A-CE-Z]"` is the upper case alphabet excluding D.  Finally, you can invert a group with the `^` symbol.  The pattern `[^D]` matches any character except `'D'`.  Python's regular expressions also assumes a specific order of characters.   The digits `0-9` precede `A-Z`, which in turn precede `a-z`.  This means that you can define a range that spans these intuitive groupings.  For example, `"foo[5-HT-j]"` matches `"foo9"` and `"food"`, but not `"fooJ"` or `"foot"`.

Finally, the symbol `.` matches *any* character, so you don't have to write out all possible characters with the square bracket notation.

Note that we are simply declaring a string.  This string defines a pattern under the rules of regular expressions.  We don't have to use double-quotes `"` for these strings; single-quotes `'` will serve just as well.  For consistency, however, I'll keep using double-quotes.


### Using patterns

Before we go on with defining patterns, we need to learn a bit about how to use them so that we can work through some examples.  There are generally two ways to use the `re` module.  First, you can directly call functions from the module:
```python
>>> dir(re)
['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_alphanum_bytes', '_alphanum_str', '_cache', '_cache_repl', '_compile', '_compile_repl', '_expand', '_locale', '_pattern_type', '_pickle', '_subx', 'compile', 'copyreg', 'error', 'escape', 'findall', 'finditer', 'fullmatch', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'sys', 'template']
```
For example, we can look for all substrings that match the pattern `"[A-Z]"`:
```python
>>> re.findall("[A-Z]", 'YaRo0w!')
['Y', 'R']
```
The `findall` function returned a list of all substrings (in this case, single characters) that matched the pattern.  This list can be assigned to a variable to be used later on.  If there are no matches, then it returns an empty list:
```python
>>> re.findall("[A-Z]", 'python?')
[]
```

Second, you can compile a pattern, which creates an `SRE_Pattern` object:
```python
>>> p = re.compile("[A-Z]")
```



Second,


### Repeating characters and groups

Let's start with the `+` symbol.  This symbol is used to describe a regular expression where the preceding character can be repeated one or many times.  For example, `a+` can represent `a`, `aa`, or `aaaaaaa`.  This symbol will only affect the character immediately in front of it.  `ba+` matches `baa` but not `bbaa`.

If you want to match


## Date and time data

##