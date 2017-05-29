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

Regular expressions (or *regex*es, for short) are extremely useful when you are dealing with text-based data sets.  We can screen a set of strings for those that match the regex, capture parts of those strings, and then use those parts to rewrite the string.  It doesn't sound like much, but it is a big deal.  Unforunately, there are different kinds of regular expressions.  Python uses Perl-style regular expressions.

![](https://imgs.xkcd.com/comics/regular_expressions.png)

A regular expression is defined by inserting special characters into the string.  Many of these are characters that we would normally want to use for their original meaning, such as the round brackets `(` and `)`.  To tell Python that we want to use brackets in the "normal" way, we need to use the escape symbol `\` like we do for line breaks (`\n`):
"""
"\(like this\)"
"""
Also note that *any* character can be used in a regular expression, such as spaces and punctuation marks.

To load the regular expressions module, type:
```python
>>> import re
```


### Defining groups

A group matches any of a subset of characters.  It is defined by square brackets.  For example, `"c[aou]t"` matches `"cat"`, `"cot"` and `"cut"`, but not `"cet"`.  It also does not match `"bat"`, because the pattern expects the group to have a `'c'` on the  left and a `'t'` on the right.

Some times you want to specify a large range of characters in a group.  To save you the trouble of typing all of those characters in, regular expressions have a range syntax: `"[x-y]"` where `x` and `y` are the inclusive limits of the range.  For example, `"[a-z]"` is the subset of all lower case characters in the alphabet.  `"[0-9]"` is all the digits.

You can specify a partial range.  `"[A-C]"` matches `'A'`, `'B'`, and `'C'`, but not `'D'`.  You can also concatenate ranges.  For example, `"[A-CE-Z]"` is the upper case alphabet excluding D.  Finally, you can invert a group with the `^` symbol.  The pattern `[^D]` matches any character except `'D'`.  Python's regular expressions also assumes a specific order of characters.   The digits `0-9` precede `A-Z`, which in turn precede `a-z`.  This means that you can define a range that spans these intuitive groupings.  For example: `"foo[5-HT-j]"` matches `"foo9"` and `"food"`, but not `"fooJ"` or `"foot"`.

Finally, the symbol `.` matches *any* character, so you don't have to write out all possible characters with the square bracket notation.

Note that we are simply declaring a string.  This string defines a pattern under the rules of regular expressions.  We don't have to use double-quotes `"` for these strings; single-quotes `'` will serve just as well.  I'm not going to be consistent!


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
This object has the many of the same functions as the `re` module itself:
```python
>>> set(dir(p)).intersection(dir(re))
{'sub', 'search', 'fullmatch', 'match', 'findall', '__doc__', 'finditer', 'subn', 'split'}
```
Indeed, it returns exactly the same results as our previous examples calling from `re`:
```python
>>> p.findall('YaRo0w!')
['Y', 'R']
>>> p.findall('python?')
[]
```
One difference is that we don't have to keep entering the pattern-defining string when calling this function.  A more important difference, however, is that Python doesn't have to keep compiling our regular expression pattern, which is a waste of computing time if we are running the same function many times.  For example, this script (don't bother copying this out):
```python
from time import time
import re

t0 = time()
for i in range(10000):
    matches = re.findall("[A-Z]", 'YaRo0w!')
t1 = time()

t2 = time()
p = re.compile("[A-Z]")
for i in range(10000):
    matches = p.findall('YaRo0w!')
t3 = time()

print('module {} seconds'.format(t1-t0))
print('compiled {} seconds'.format(t3-t2))
print('compiling is {} times faster'.format((t1-t0)/(t3-t2)))
```
This script produces the following result:
```shell
module 0.0111448764801 seconds
compiled 0.00501084327698 seconds
compiling is 2.22415187705 times faster
```
I would expect even greater speed gains with more complex regular expressions.

For now, `findall` is good enough to illustrate how various patterns work.  Later on, we'll cover some of the other functions, such as `match` and `sub`.


### Repeating characters and groups

Let's continue on with the `+` symbol.  This symbol is used to describe a regular expression where the preceding character can be repeated one or many times.  For example, `a+` can represent `a`, `aa`, or `aaaaaaa`.  This symbol will only affect the character immediately in front of it.  `ba+` matches `baa` but not `bbaa`.

This symbol is especially powerful when combined with a group expression.  For example, `"[A-Z]+"` matches any substring combining upper case letters, of any length:
```python
>>> p = re.compile('[A-Z]+')
>>> p.findall('JACKET')
['JACKET']
>>> p.findall('pants')
[]
>>> p.findall('Tie')
['T']
```

If you want to include the possibility that there is *no* match, then you can use the `*` symbol.  For example:
```python
>>> p = re.compile('i[aon]*n')
>>> p.findall('in')
['in']
>>> p.findall('piaaaaaano')
['iaaaaaan']
```

You can also declare a pattern that expects a specific number or range of matches.  For example:
```python
>>> p = re.compile('[abc]{3}')
>>> p.findall(' abcbacbabca ')
['abc', 'bac', 'bab']
```
only returns matches that span 3 characters in the group `[abc]`.  This is different behaviour than:
```python
>>> p = re.compile('[abc]+')
>>> p.findall(' abcbacbabca ')
['abcbacbabca']
```
If you want to match a range of lengths, then you can use the `{m,n}` syntax:
```python
>>> p = re.compile('a{3,5}')
>>> p.findall('aa')
[]
>>> p.findall('aaa')
['aaa']
>>> p.findall('aaaaaaaa')
['aaaaa', 'aaa']
```
The range can contain zero:
```python
>>> p = re.compile('da{0,5}d')
>>> p.findall('daaad')
['daaad']
>>> p.findall('dd')
['dd']
```

Finally, the special case of `{0,1}` has its own symbol `?`, which means that the preceding character or group may or may not appear once in the pattern:
```python
>>> p = re.compile('to?ny')
>>> p.findall('tny')
['tny']
```
Note that this means we have to escape `?` if we mean the question mark, and not the 0/1 match:
```python
>>> p = re.compile('tony?')  # may or may not contain 'y'
>>> p.findall('anton?')
>>> p = re.compile('tony\?')  # literal question mark
>>> p.findall('anton?')
[]
>>> p.findall('antony?')
['tony?']
```
The same thing goes for every other special character we've covered.

** Exercise **
> Try writing a regular expression pattern that matches Genbank accession numbers.  These are supposed to start with one or two upper case letters, and end with five or six digits.  For example, `JN398015` and `U15660` are permitted accession numbers, but `8AB801` and `CYY5018599` are not.


### Position

So far we've assumed that a substring matching our pattern can appear anywhere in the master string.  If we want to find substrings in a particular location in the string, then we need to be able to refer to the start and end of that string.  Thus, we have the special characters `^` and `$`, respectively.  Note that this is the second special usage of the character `^` - it can also be used to invert the contents of a group.  For example, `"^[^a]` matches any string that does not start with an `'a'`.

Regular expressions become very powerful when you can make ambiguous or exact matches relative to the start or end of a string.  For example, suppose that we want to capture the last date in ISO format `YYYY-MM-DD` in a long line of text:
```python
s = "
```


### Capturing groups



### Example: Parsing broken identifiers


## Date and time data

##