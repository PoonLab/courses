# Variables

## Python as a calculator

I stole this section title from the [official Python tutorial](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator) because I really like the idea of introducing students to Python by launching it in interactive mode and working with this session in a familiar way, *e.g.,* punching in numbers and operations like a simple calculator.  First, let's launch an interactive session of Python:
```bash
art@orolo:~$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
(Note that I had to specifically ask for Python version 3 instead of version 2 -- on my Linux distro, this is just `python`.) This is a command line shell just like you've been working with for class on the [command line interface](Readings/basicunixcommands.md).  It has a prompt that comprises three greater-than signs: `>>>`.  The same tricks for navigating a command line entry and the history of your session apply equally well to this Python shell as they did for working with UNIX; we can use:
* the `left` and `right` arrow keys to move along the command line
* the `up` and `down` arrow keys to recall previous commands
* `Ctrl-A` and `Ctrl-E` to jump to the start or end of the current command line
* `Tab` to autocomplete a command if what you have already typed in uniquely refers to one of the available commands

First things first.  We've entered the Python interactive shell.  How do we get out?  You can get back to the original command line interface by typing `Ctrl-D`.  If you forget, type `exit` or `quit` and Python will remind you!
```python
>>> quit
Use quit() or Ctrl-D (i.e. EOF) to exit
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
```

Let's start doing some very basic calculations in Python:
```python
>>> 1+2
3
>>> 2*3
6
>>> 1+2*3  # Python adheres to the order of operations
7
>>> (1+2)*3  # we can use brackets
9
>>> 3/2
1.5  # note in Python 2.x this returns a 1
>>> 3%2  # 3 modulo 2 (divide and return the integer remainder)
1
>>> 3//2  # divide 3 by 2 and return only the integer part
1
>>> 3**2  # 3 to the power of 2
9
```
All floating point numbers (numbers with decimal places) in Python are [internally represented as the sum of one or more fractions](https://docs.python.org/3.0/tutorial/floatingpoint.html).  In some cases, there is no exact representation for the number, which gives you funny results like this:
```python
>>> 0.1*3
0.30000000000000004
```


## Making variables

Using Python as a calculator is handy but we're not really doing any programming.  A fundamental concept in programming is the abstraction of tasks like arithmetic so that the same operations can be applied to any inputs.  A variable is an agreement between you and the computer to refer to something with a unique name:
```python
>>> sandwich = 3  # assignment operation
>>> sandwich  # print the value currently assigned to this variable
3
```
What just happened here?  We've named a variable `sandwich` and assigned to it the integer value `3`.  Python interprets the equal sign `=` as a directive to **assign** the value on the right side to a variable on the left side.  I think most programming languages follow this right to left convention, although there are different notations used for variable assignment.  For example, *R* uses a notation (`<-`) that is less ambiguous.  Second, entering the variable name by itself is requesting Python to print the value associated with the variable.  Since we just assigned the integer value `3` to our variable, that's what is printed out.

Now, we apply operations to this `sandwich` variable so that it becomes a generic action on any value that we assign to `sandwich`:
```python
>>> sandwich + 1
4
>>> sandwich = 0.5  # assign a different value
>>> sandwich + 1  # same operation as before
1.5
```
Here, we've abstracted the act of adding one to some quantity, so we can use the same command to apply this action to *any* value that we assign to the `sandwich` variable.

Variables are also useful for capturing the result of some operations so that we can use it for other calculations:
```
>>> cat = 1+3
>>> dog = cat /2
>>> dog
2.0
```
It's also useful for "saving our work", *e.g.*, when we want to do some more operations with this variable later on.  We can use the variable as many times as we want!  *However*, we have to be careful that we don't inadvertently modify the variable so that it holds a completely different value by the time we want to re-use the original.

## Naming variables

Let's try messing around with Python a bit:
```python
>>> 2=3
  File "<stdin>", line 1
SyntaxError: can't assign to literal
```
This is an error because we can't use `2` as a variable.  It has a fixed value, which is what the error statement means when it's referring to it as a literal object.  We would say that `2` is a constant, not a variable.  Let's try something else:
```python
>>> 2two=3
  File "<stdin>", line 1
    2two=3
       ^
SyntaxError: invalid syntax
```
Python didn't like this because it has strict rules about variable names.  It doesn't allow variable names to have any characters other than `_`, `A` to `Z`, `a` to `z`, and `0` to `9`, and the name cannot start with a digit.  These rules have to exist because if our variable name contains a character that has another role in the language, such as `=`, then Python is going to get confused!

It's important to choose good variable names.  Here are some general guidelines:
* Avoid using single letters as variable names like `x`, with an exception for generic variables such as [loop](Readings/ControlFlow.md) counters where we often use `i` for counting integers.
* A name should be descriptive.  You don't want to name something `pepperoni` because your future self will have no idea what you're talking about.
* Names should be concise.  You'll get tired of typing out `the_number_of_amino_acids_in_the_sequence` over and over again, and long variable names will cause unnecessary clutter in your code.
* The [Python style guide](https://www.python.org/dev/peps/pep-0008/#id34) recommends that variable names be in lowercase and use underscores to separate words.  An alternative style is [camelcase](https://en.wikipedia.org/wiki/Camel_case), which uses a mix of upper and lowercase with uppercase used to indicate the start of a new word; *e.g.*, `theLastWord`.  It's fine if you prefer camelcase to underscores, but you should use one or the other consistently! 


## Variable types

So far we've mostly been messing around with integers.  An integer is a specific *type* of variable in Python.  An integer has a number of properties that it does not share in common with other variable types.  To determine the type of a variable or constant, we can make use of the built-in Python function `type`:
```python
>>> type(1)
<class 'int'>
>>> sandwich=3
>>> type(sandwich)
<class 'int'>
```
Here, the function `type` has identified the constant `1` as an instance of the class `int`.  A `class` is a more general category of objects in Python.  If this is getting confusing, think of a `type` as a subset of `class` - all types are classes, but not all classes are types.  Or if that is still too confusing, just think of `class` as a synonym of `type` for now.  

Python is a [dynamically-typed language](https://en.wikipedia.org/wiki/Type_system): this means that we don't have to tell Python what kind of variable we are trying to make.  Python is smart enough to guess at our intention when we make the variable assignment.  For example, when we assign a floating point number to `sandwich`, its type is changed:
```python
>>> sandwich = 3.01
>>> type(sandwich)
<class 'float'>
```
In many other programming languages, the assignment of type is much more explicit --- we have to spell out the fact that we are making a new variable of integer type, and bad things will happen if we try to do non-integer things to it.


## Coercion and casting variables

A float is a Python `type` that is used to represent floating point numbers (a number with a decimal point).  What happens when we add an integer to a float?  
```python
>>> a = 1.2 + 3
>>> a
4.2
>>> type(a)
<class 'float'>
```
Any result of a sum that involves one or more floats will always return a float, even if the floats are integer-valued: 
```python
>>> 1 + 2 + 3 + 4 + 5.0
15.0
```
This is called *variable coercion*.  It's important to be aware of this behaviour, especially when you start to mix more divergent Python types.

What if we want to keep the result of this sum as an `int` type?  There are a number of possibilities, but the most generic is to force the result of this sum to be an integer using the `int()` function, which takes a single argument and attempts to convert it into an `int` type:
```python
>>> int(3.0)
3
>>> int(3.1)
3
>>> int(1 + 2 + 3 + 4 + 5.0)
15
>>> int('3')  # cast a string as an integer
3
>>> int('three')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '3pizza'
```
(In this example, I've made use of [string](Readings/Strings.md) objects.  We'll talk more about these later.)  If `int` can't convert the argument into an integer, then it complains - it throws an exception.

When you cast a `float` as an `int`, the fractional part is simply dropped from the number.  The `round` function uses the fractional part to determine whether the value is rounded up or down to the nearest integer:
```python
>>> type(round(3.0))
<class 'int'> 
>>> round(3.49)
3
>>> round(3.51)
4
```

