> This document is in progress

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
Note that I had to specifically ask for Python version 3 instead of version 2 (on my Linux distro, this is just `python`).

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

Using Python as a calculator is handy but we're not really doing any programming.  A fundamental concept in programming is the abstraction of tasks like arithmetic so that the same operations can be applied to any inputs.  Variables are a fundamental concept in programming - a variable is an agreement between you and the computer to refer to something with a name that you've both agreed on:
```python
>>> sandwich = 3
>>> sandwich
3
```
What just happened here?  We've named a variable `sandwich` and assigned to it the integer value `3`.  Python interprets the equal sign `=` as a directive to assign the value on the right side to a variable on the left side.  I think most programming languages follow this right to left convention, although there are different notations used for variable assignment.  For example, *R* uses a notation (`<-`) that is less ambiguous.

Second, entering the variable name by itself is requesting Python to print the value associated with the variable.  Since we just assigned the integer value `3` to our variable, that's what is printed out.

Let's try messing around with Python a bit:
```python
>>> 2=3
  File "<stdin>", line 1
SyntaxError: can't assign to literal
```
This is an error because we can't use `2` as a variable.  It has a fixed value, which is what the error statement means when it's referring to it as a literal object.  Let's try something else:
```python
>>> 2two=3
  File "<stdin>", line 1
    2two=3
       ^
SyntaxError: invalid syntax
```
Python didn't like this because it has strict rules about variable names.  It doesn't allow variable names to have any characters other than `_`, `A` to `Z`, `a` to `z`, and `0` to `9`, and the name cannot start with a digit.  These rules have to exist because if our variable name contains a character that has another role in the language, such as `=`, then Python is going to get confused!

## Numbers

