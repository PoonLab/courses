# String formatting

So far we've mostly talked about reading text from files, parsing information from that text, and printing some information to the console with `print()`.  We also need to learn how to write output to another file, which is more convenient when there is a lot of output or if we need to write to multiple files, making it difficult to use stream redirection with the `>` operator.  We've generally made use of string concatenation in Python using the `+` operator or the `join` function.  

In this section, we're going to talk about more complex methods for constructing formatted strings.  A formatted string is basically a template for making strings from one or more variables.  It contains symbols that tell Python how to embed the information contained in the variables into specific locations of a string.  There are two ways of defining a formatted string in Python, the old way:
```python
example1 = "A number %d and a string %s" % (27, 'like this')
```
and the newer way:
```python
example2 = "A number {} and a string {}".format(27, 'like this')
```

## C-style string formatting
The old style borrows the `%` notation from the programming language C.  The percent sign identifies a placeholder in the string -- it is interpreted as a symbol instead of a literal substring.  In general, we use this notation as follows:
```python
>>> '%s, %s and %s' % ('cow', 'horse', 'chicken')
'cow, horse and chicken'
```
Note that the percent sign `%` has been used in two different ways here.  First, it is used repeatedly within the first (formatted) string to indicate where we want to insert some values.  Second, it is an operator between the formatted string and a tuple that contains variables or constants (literals) that we want to insert into the formatted string.  Note that if there is only one value to insert into the formatted string, it is alright to omit the tuple notation (round brackets):
```python
>>> a = 'Alfred'
>>> 'My name is not %s' % a
'My name is not Alfred'
```
but I personally prefer to keep using a tuple because it's more consistent:
```python
>>> 'My name is still not %s' % (a, )
'My name is still not Alfred'
```

Here is only a partial list of some of the placeholders available in this method:
* `%s` represents a string.  If you send an integer value, it will automatically be cast as a string:
  ```python
  >>> '%s' % (123,)
  '123'
  ```
  We can also allocate a minimum number of characters to insert the string value as follows:
  ```python
  >>> '%5s' % ('cat',)
  '  cat'
  >>> '%2s' % ('cat',)  # if the string length exceeds the allocated space, Python inserts the entire string
  'cat'
  ```
  
* `%d` represents an integer.  Like `%s` placeholders, `%5d` allocates 5 characters to insert the integer.  For example:
  ```python
  >>> '%5d' % (123)
  '  123'
  ```
  Further, if you append a `0` then the unused characters are replaced with zeroes:
  ```python
  >>> '%05d' % (123)
  '00123'
  ```
  
* `%f` represents a float:
  ```python
  >>> '%f' % (123,)
  '123.000000'
  >>> '%f' % ('dog',)  # this doesn't work!
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: float argument required, not str
  ```
  It behaves like `%s` and `%d` in allocating a minimum number of characters to insert a value, with a slight difference in that Python automatically sets the number of decimal places to `6` by default:
  ```python
  >>> '%5f' % (1.23,)  # we might expect '  1.23'
  '1.230000'
  >>> '%10f' % (1.23,)
  '  1.230000'
  ```
  The number of decimal places can be controlled as follows:
  ```python
  >>> '%5.1f' % (1.23,)
  '  1.2'
  >>> '%5.3f' % (1.23,)
  '1.230'
  ```


## `format`
The Python string `format` function does not require you to specify what kind of variable you want to embed in the string.

The new style also provides a little more functionality.  First, you can reference different arguments with integer indices:
```python
>>> "A string {1} and a number {0}".format(27, "like this")
'A string like this and a number 27'
```
This is a nice feature when you need to repeat an entry:
```python
>>> "{1}: {0} {0}".format(27, "like this")
'like this: 27 27'
```
and you can even index into nested objects that you've already indexed:
```python
>>> "{0[3]} is a {1}".format([1,2,3,5,7], "prime")
'5 is a prime'
```
You can also refer to keyword instead of positional arguments in the `format` command:
```python
>>> "{name}: {height} cm".format(name="Theo", height=170)
'Theo: 170 cm'
```
I think these particular examples are the most useful when we pass a tuple or dictionary as an argument to `format`.  To pass a tuple, you need to unpack it with a `*` operator:
```python
>>> tup = (27, "like this")
>>> "{1}: {0}".format(*tup)
'like this: 27'
```
and a dictionary can be unpacked with a `**` operator (we'll talk more about dictionaries in a bit):
```python
>>> data  = {'name': 'Theo', 'height': 170}
>>> "{name}: {height} cm".format(**data)
'Theo: 170 cm'
```

This is only a handful of things you can do with the new approach.  To see more examples, see [this documentation page](https://docs.python.org/3.5/library/string.html#format-examples).
