
## Formatted output

So far we've mostly talked about reading text from files, parsing information from that text, and printing some information to the console with `print()`.  We also need to learn how to write output to another file, which is more convenient when there is a lot of output or if we need to write to multiple files, making it difficult to use stream redirection with the `>` operator.

First let's talk about constructing formatted strings.  A formatted string embeds information from one or more variables into specific locations of a string.  There are two ways of defining a formatted string in Python, the old way:
```python
example1 = "A number %d and a string %s" % (27, 'like this')
```
and the newer way:
```python
example2 = "A number {} and a string {}".format(27, 'like this')
```

The old style borrows the `%` notation from the programming language C.  `%d` represents an integer, and `%s` represents a string.  In contrast, the string `format` function does not require you to specify what kind of variable you want to embed in the string.

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
