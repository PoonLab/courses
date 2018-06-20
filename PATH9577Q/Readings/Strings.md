## Strings

A string is a kind of object in Python.  We identify a string constant by enclosing text in single or double quotes.
```python
>>> type('I am a string')
<class 'str'>
>>> s = "I am assigned to a variable"
>>> type(s)
<class 'str'>
>>> "Your quotes have to be balanced'
  File "<stdin>", line 1
    "Your quotes have to be balanced'
                                    ^
SyntaxError: EOL while scanning string literal
```
`EOL` stands for "end of line".  Python's upset that I hit the `Enter` key before closing out the string I was writing.  With the first `"`, I promised Python that I would end the growing string with a second `"`. 

>A literal is Python's way of talking about a string constant -- the sequence of characters is being read literally, instead of being interpreted as symbols in the Python language.

>A [syntax error](https://en.wikipedia.org/wiki/Syntax_error) means that you accidentally broke the rules of the programming language and Python has no idea what you're talking about.  It is like having as having a conversation with someone and saying: "... so we opened the door and gabato flimm zxayaok *blows raspberry* *makes farting noise with armpit*".

`"` and `'` are reserved characters in Python strings.  For example, we can't simply toss in a single quote for an apostrophe without causing trouble:
```python
>>> a_string = 'Don't try this at home'
  File "<stdin>", line 1
    a_string = 'Don't try this at home'
                    ^
SyntaxError: invalid syntax
```
There are a couple of solutions to this common problem.
1. Enclose the strings with double quotes:
```python
>>> "It's a single quote!"
"It's a single quote!"
```
2. Escape the single quote with a backslash character (`\`), so the quote is interpreted as a symbol instead of being read literally:
```python
>>> 'It\'s still a single quote!'
"It's still a single quote!"
```

What happens if we need to declare a literal that contains both single and double quotes?  First, we could take strategy 2 and diligently escape every quote, but this is kind of a pain for long strings with lots of quotes.  Second, Python has a "nuke it from orbit" alternative, which is to enclose the string in **triple quotes**:
```python
>>> '''"So, you're the UNIX guru."'''
'"So, you\'re the UNIX guru."'
```
(Note that when Python echos back the string literal, it returns it in a format that's a valid input.)
We can use either three single `'''` or double `"""` quotes to enclose the string literal, as long as we use the same choice for both the left and right ends of the string.

Can a string literal contain line breaks?  During an interactive session of Python, if we hit the `Enter` key while writing out a string that we meant to enclose in single or double quotes, then we're going to get a syntax error.  Again we have two choices - first, we can use a special escape character, `\n`, to represent the line break:
```python
>>> a = 'break this line\nok'
>>> print(a)
break this line
ok
```
or we can declare the string literal using triple quotes:
```python
>>> a = """break this line
... ok"""
>>> a
'break this line\nok'
>>> print(a)
break this line
ok
```


## Indexing and slicing
Strings are a very different type of object in Python than [integers or floats](Variables.md).  First, a string is an *iterable* object.  It is an ordered sequence of smaller objects (characters), which means that we can move from one part of the string to another in a meaningful way, and partition the string into substrings.

A string is an ordered sequence because a character has a specific location in the string, and changing this location would give you a different string.  If the order of values in the sequence is meaningful, then we can legitimately ask Python for the value located at the third position of the sequence.  This is called *indexing*.  Python is a zero-index language: it starts counting from zero.  Other languages, such as *R*, are one-index languages and start counting from one.  Here's an example:

```python
>>> s1 = "hotdog"  # define a string by enclosing characters with double-quotes and assign it to a variable
>>> s1[1]
'o'
>>> s2 = 'ketchup'  # single quotes are okay too
>>> s2[0]
'k'
>>> s2[0] = 'Z'  # now let's try to assign a new value to the first position
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

A very important generalization of indexing is *slicing*, where we cut out a continuous interval of a sequence.  A slice is invoked by square brackets and a pair of integers separated by a colon (`:`) that describes a range:
```python
>>> s2[0:3]  # the first 3 letters of "ketchup"
'ket'
>>> s2[:3]  # we can omit the zero
'ket'
>>> s2[3:5]  # the 3rd and 4th letters
'ch'
>>> s2[-3:]  # the last 3 letters
'hup'
>>> s2[1:-1]  # exclude the first and last letters
'etchu'
```
So to sum up, the first integer gives the left limit of the range and the second gives the right limit.  If an integer is negative, then we start counting from the end of the string instead of the beginning.  Negative indexes are one-index instead of zero-index because we can't distinguish between `0` and `-0`.

When you're learning Python for the first time, it's easy to get tripped up by slice notation.  First of all, remember that Python is a zero-index language, so we always start counting from `0`.  In other words, the element at position `1` is the 2nd element of a sequence.  In the first example, it might look like we've asked for four elements because the range `0:3` seems to span the numbers 0, 1, 2, and 3.  However, Python slices are left-closed/right-open intervals - they include the leftmost value, but they don't include the rightmost value.  This is actually a nice convention for a zero-indexed language: it allows us to ask directly for the first 3 letters with the integer value 3.

There is actually a third "argument" to slice notation that people seldom use, but I'll mention it because you might encounter it when reading someone else's script.  This third argument specifies the step size used to progress through the range specified by the first and second arguments.  For example:
```python
>>> s2[0:5:2]  # s2 is still "ketchup"
'kth'
```
returns the first, third and fifth letters.  If you ever do encounter this type of slice notation, it'll probably be the following usage:
```python
>>> s2[::-1]  # return the entire string in reverse
'puhctek'
```
This implies that the following is a legitimate (but kind of pointless) slice, and it is indeed:
```python
>>> s2[:]
'ketchup'
```

![](https://imgs.xkcd.com/comics/donald_knuth.png)


### Mutability

A string is "immutable":  Python won't allow you to change parts of the string by assigning a different character.  This is a property that strings share in common with [integers and floats](Variables.md).  On the other hand, you can concatenate two strings together without changing the content of either string.  This is accomplished with the plus sign (`+`):
```python
>>> s1+s2
'hotdogketchup'
```
Other operators don't work:
```python
>>> s1-s2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> s1*s2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
```
But if we multiply a string with an integer, then it gets repeated:
```python
>>> s1*3
'hotdoghotdoghotdog'
```


### Getting class attributes with `dir`

I've mentioned that being a particular `type` means that the object (variable or constant) automatically takes on a number of properties.  To learn about these properties, we can use the `dir` function:
```python
>>> dir(s1)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
This function returns a [list](Lists.md) of the attributes that belong to all `str`-type variables.  Note that many of these entries are enclosed in double underscores (`__`, also known as a "dunder") -- in Python, this notation is used to identify special methods that often correspond to built-in methods in Python.  For example, `__add__` corresponds the method that Python uses when you use the `+` operator on a string (we can use this to concatenate two strings).  This is pretty low-level stuff and we won't go into any more detail than this --- I'm just trying to make all these dunder methods less intimidating.  From now on, we're going to completely ignore the dunder methods!

A nice feature of Python is that you can call the `dir` function on any instance of an object and get the list of that object's attributes.  Here, we called `dir` on the `s1` variable - because we assigned a string value to this variable, we get the list of string functions.  It works just as well to call `dir` on a string constant.  Try it!

There are several useful functions to talk about here.  I'm going to collect these into "descriptive" and "manipulative" groups of functions.

### Descriptive string functions

I'm referring to these functions as descriptive because they are essentially tests on the content of a string: they return a `True` or `False` value that is the outcome of the test.  They don't return a new string or strings that are the product of the original string.  In most of the following brief descriptions, I am not going to go into some of the optional arguments for the respective functions; you can always learn more about them with the `help` function, *e.g.*, `help(''.beginswith)`.

* `beginswith` and `endswith` test whether a string starts or ends with a particular substring, respectively.  For example:
 ```python
 >>> s = 'jabberwocky'
 >>> s.startswith('jab')
 True
 >>> s.endswith('hockey')
 False
 ```

* `in` is actually an operator like `+` or `==`, not a function.  However, I'm going to mention it here because it is a useful test that is less specific than `beginswith` and `endswith`: it simply tests whether a substring occurs anywhere in the string:
 ```python
 >>> 'wock' in s  # variable still holds "jabberwocky"
 True
 ```
 
* A more informative test of substring occurrence is provided by `find` and `index`, which both return the index of the first occurrence.  The key difference between these two functions is that `find` returns a `-1` integer value if the substring is not found in the string, and `index` raises an Error.
 ```python
 >>> s.index('wock')
 6
 >>> s.find('wock')
 6
 >>> s.find('oaijreg')
 -1
 >>> s.index('oiajewf')
 Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
 ValueError: substring not found
 ```
 
 * `count` returns the number of times that a substring occurs in the string:
 ```python
 >>> s.count('b')  # jabberwocky has two 'b's
 2
 ```


### Manipulative string functions

I'm using this term to describe string functions that return a string or multiple strings.  Again, most of these functions have optional arguments that I won't be covering, and which can be examined with the `help` function.

* `strip` : When this function is called without any arguments, it removes any leading or trailing whitespace (spaces or tabs on the extreme left or right of a string) by default.  If you supply a substring as the optional argument, then any occurrence *of any character* in the substring is removed from the left or right of the string.  `lstrip` and `rstrip` are special cases where `strip` is applied only to the left or right of a string, respectively.
 ```python
 >>> s = '  shrubbery \t'
 >>> s.strip()
 'shrubbery'
 >>> s.lstrip()
'shrubbery \t'
 >>> s.rstrip()
 '  shrubbery'
 >>> '  the spaces between us  '.strip()  # whitespace within a string is protected
 'the space between us'
 >>> s.strip(' sy')  # can you explain why we get this output?
 'hrubbery \t'
 ```

* `replace` : This function has two required arguments.  The first argument is a substring to search for, and the second argument is a substring to replace every occurrence of the former.  
 ```python
 >>> s.replace('b', '')
 '  shruery \t'
 >>> s.replace('r', 'NI')
 '  shNIubbeNIy \t'
 ```

* `split` : `split` is an extremely useful function for working with tabular data - it locates every occurrence of the substring argument and cuts the string into pieces wherever it removes the substring.  `split` always returns a list, even if the substring wasn't found.  Like `strip`, `split` cuts at whitespace by default.
 ```python
 >>> s = 'LCD Soundsystem'
 >>> s.split()
 ['LCD', 'Soundsystem']
 >>> s.split('s')
 ['LCD Sound', 'y', 'tem']
 ```
 
* `join` : is the antipode of `split`.  It takes a list of strings and then concatenates them together into a single string using a given substring as glue.  A key difference between `join` and the other functions is that the substring that is being used as glue is the calling object, not the argument.  This is necessary because the return value of `split` is a list, and a list can be sequence of any kind of object including a mixture of strings, integers and other lists.  It doesn't make sense to concatenate the items in a mixed list into a single string!
 ```python
 >>> s = "it's going to be a long trip"
 >>> '...'.join(s.split())  # not "s.split().join('...')"
 "it's...going...to...be...a...long...trip"
 ```
 
