> This document is in progress

# Variables

## Python as a calculator

## Making variables

 Variables are a fundamental concept in programming - a variable is an agreement between you and the computer to refer to something with a name that you've both agreed on:
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

