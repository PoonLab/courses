# Control flow

1. [Running and writing scripts](ControlFlow.md#running-and-writing-scripts)
2. [Iteration](ControlFlow.md#iteration-in-python)
3. [Conditional statements](ControlFlow.md#conditional-statements)
4. [Functions](ControlFlow.md#functions)

[Control flow](https://en.wikipedia.org/wiki/Control_flow) determines how the computer moves through a set of instructions. Like many scripting languages, Python generally starts at the top of an instruction set and progresses downwards.  This downward flow can be interrupted by an instruction for Python to repeat a specific block of code a number of times (iteration).  It can also be diverted into separate streams depending on whether one or more specific conditions are met ([conditional branching](https://en.wikipedia.org/wiki/Branch_(computer_science))).  Finally, the program can be temporarily switched to a completely different set of instructions before continuing on the original flow ([subroutines](https://en.wikipedia.org/wiki/Subroutine)). 

In Python, these aspects of control flow are accomplished by iteration (with `for` and `while`), conditional statements (`if` and `else`), and by defining and calling functions (`def`). 


## Running and writing scripts

Since we're going to start working with more complex instructions in Python that span multiple lines and define blocks of code (more on this later), this is a good point to transition from working with Python's interactive shell to writing scripts and calling the Python interpreter on your script.  I've created a little text file with a single line of Python and saved it as `example.py`.  We can call the Python interpreter on our script by running the command `python3` and providing a relative or absolute path to the script file as the only argument:
```shell
art@Kestrel:~/Desktop$ cat example.py 
print("This is a very small script!")

art@Kestrel:~/Desktop$ python3 example.py 
This is a very small script!
```

Remember that if we call `python3` without any argument, the program defaults into launching an interactive shell.  Once Python has run through our script, it exits back into the command line.  If Python encounters a problem while running through the script, then it will issue an exception like we've encountered in interactive mode (*e.g.,* `SyntaxError`) and exit prematurely (without running the rest of the script).

Sometimes you will see a script that contains this statement on the first line:
```python
#!/usr/bin/env python3
```
The combination of `#!` symbols are called a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) and directs the operating system to use the rest of the line to call the appropriate interpreter program for running this script.  `/usr/bin/env` is an absolute path to the `env` program that tells UNIX to run the following program in a modified environment -- in this case, `env` is retrieving an absolute path to the `python3` binary in the filesystem.  

You might encounter this line at the top of a Python script when the author intended for it to be run like a normal executable program.  Again, we normally call the `python3` program and then give a path to the script as the sole argument.  The file containing our script doesn't need to be an executable file -- it's just a plain text file for which we only need read access.  Note: we really do need to have read access.  Let's modify our `example.py` script to illustrate:
```shell
art@orolo:~/Desktop$ cat example.py 
#!/usr/bin/env python3
print('Hello world!')
art@orolo:~/Desktop$ python3 example.py 
Hello world!
art@orolo:~/Desktop$ ./example.py
-bash: ./example.py: Permission denied
```

If we take away all permissions from everyone, we can't even run this script the usual way:
```
art@orolo:~/Desktop$ chmod 000 example.py 
art@orolo:~/Desktop$ ls -l example.py 
---------- 1 art art 46 May 15 21:18 example.py
art@orolo:~/Desktop$ python3 example.py 
python3: can't open file 'example.py': [Errno 13] Permission denied
art@orolo:~/Desktop$ chmod 664 example.py  # restore the original permissions
```

Now if we grant ourselves execution privileges on the script, we can call it like a local program:
```shell
art@orolo:~/Desktop$ chmod 755 example.py
art@orolo:~/Desktop$ ls -l example.py 
-rwxr-xr-x 1 art art 46 May 15 21:18 example.py
art@orolo:~/Desktop$ ./example.py 
Hello world!
```
In this case it is conventional to drop the `.py` extension.  If I temporarily move the file to a directory in my `$PATH` environment, then it acts like a typical program:
```shell
art@orolo:~/Desktop$ mv example.py example
art@orolo:~/Desktop$ sudo cp example /usr/local/bin/example
[sudo] password for art: 
art@orolo:~/Desktop$ cd
art@orolo:~$ ls example
ls: cannot access 'example': No such file or directory
art@orolo:~$ example  # Now we can run this script from anywhere in the filesystem
Hello world!
```

Why would anyone want to turn a Python script into a pretend executable file?  I've seen cases where scripts are installed into `/usr/local/bin` so a given script can be called by any user on the system as though it was a typical program.  



### Basic debugging
Let's create another text file with the following contents:
```python
a = 1
b = 2
print(str(a+b))
print('This will break)
print('This will not get run')
```
and call it `example2.py`.  If we run the script, Python will throw an exception:
```shell
art@Kestrel:~/Desktop$ python3 example2.py 
  File "example2.py", line 4
    print('This will break)
                          ^
SyntaxError: EOL while scanning string literal
```
We've encountered this `SyntaxError` before -- Python encountered the end of a line before we finished declaring a string literal.  (Remember that a *string literal* is a sequence of characters that represents one and only one string, and that it should be enclosed with matched single or double quotes if the string will only occupy a single line.) 

Python provides some useful information here.  First, it tells us which file contains the bug (`File "example2.py"`) and the line within that file that contains the bug (`line 4`).  It even shows us the line in question:
```python
    print('This will break)
                          ^
```
and highlights the offending character with a caret symbol (`^`).  We forgot to add a closing quote mark! 


### Comments

Because a script is a set of instructions that has been written into a file, we don't have to keep entering the same instructions over and over in an interactive shell.  Another great thing about writing a script is that we can write *comments* - discrete bits of text that explain what a piece of code is meant to do. 

There are several different kinds of comments, but for now we'll just talk about inline comments.  An inline comment occupies a single line.  It may be preceded by some code, but any text to the right of the starting symbol `#` is ignored by Python as commenting text:
```python
# The next line will not get run either
# print('dirty socks')
print('hairnets')  # but the piece of code to the left does get run
```

Comments are extremely important, not only because it documents the purpose and thought process behind your source code to others, but also because you will return to your code days or months from now and need those comments there to remind your future self.  We'll continue to cover comment writing and documentation practices in the readings on [good coding practices](GoodCode.md).

### Taking inputs from the command line

For a script to be really useful, you need some way of sending arbitrary inputs to the functions contained in the script.  Since we want to be working with data, we will usually want to read inputs from one or more files - we'll cover how to read and write files from Python in the next class.  For now, however, we'll just cover how to read inputs from the command line.  To do this, we need to access some special functions and variables that are contained in the Python module `sys`.  The `sys` module contains functions and variables for interacting with the operating system, the filesystem and the Python interpreter:
```python
import sys
>>> sys.platform  # what operating system are we running on?
'linux'
>>> sys.version  # what is the version number for this Python interpreter?
'3.5.2 (default, Nov 23 2017, 16:37:01) \n[GCC 5.4.0 20160609]'
>>> sys.path  # a list of relative and absolute paths to search for Python modules
['', '/usr/lib/python35.zip', '/usr/lib/python3.5', '/usr/lib/python3.5/plat-x86_64-linux-gnu', '/usr/lib/python3.5/lib-dynload', '/usr/local/lib/python3.5/dist-packages', '/usr/lib/python3/dist-packages']
```
In particular, we want to use the parameter `sys.argv` - this is a List object that stores the arguments from the command line when we called the Python interpreter on this script.  The first argument in `sys.argv` will always be the filename of the script being run.  Any other arguments (separated by spaces on the command line) will be appended to this list in the same order as they were entered on the command line.

For example, we can make a basic script called `argv.py` with the following contents:
```python
import sys
print(sys.argv)
```
Here's what happens when we call the script with a bunch of arbitrary arguments:
```shell
art@orolo:~/Desktop$ python3 argv.py poodle 123 -- hexagon
['argv.py', 'poodle', '123', '--', 'hexagon']
```
The values in the list `sys.argv` are available to be assigned to other variables and manipulated as we like.  This is a standard way of passing inputs into our script.


## Iteration in Python

Iteration refers to a set of instructions being executed a number of times.  It is where bioinformatics gets a lot of its power, by doing many things very quickly.  Recall that some Python objects are [iterable](Iterables.md) - they are made up of one or more members in an ordered sequence that can be indexed and sliced.  One way to create an iterable object is by declaring the literal representation, *e.g.*:
```python
>>> s = 'this is a string iterable'
>>> l = ['This', 'is', 'an', 'iterable']
```
However, this is not a convenient method when we are dealing with an iterable with a large number of members, or when the membership of the iterable object needs to change on the fly, *e.g.,* when we are working through a large data file.

A useful function that produces a generic iterable object is the function `range`:
```python
>>> r = range(10)
>>> r
range(0, 10)
>>> list(r)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> r[0]
0
>>> r[-1]
9
>>> r[:]
range(0, 10)
```
It isn't until we coerce `r` into a new List object that we see the contents of this iterable object.  However, we can index into it just like we would with a List.  To actually iterate over a range, we have to use a `for` command:
```python
>>> for i in r:
...     print(i)
... 
0
1
2
3
...  # skipping a bunch for compactness
9
```
We can iterate over `r` as many times as we like, just like a List object.  The key differences between `range` and `list` objects is that `range` objects are immutable and store information about the range as attributes:
```python
>>> r.start
0
>>> r.stop
10
>>> r.step
1
```
`start`, `stop` and `step` are the three arguments of `range`.  For example, if we want the sequence of integers from `11` to `203` in steps of `3`, we enter:
```python
>>> r = range(11, 203, 3)
>>> for i in r:
...     print(i)
... 
11
14
17
...  # skipping
197
200
```
We will explore how to build and use `for` loops in the next section, since these are tremendously useful structures in programming.



### *for* loops

Loops are a fundamental concept in programming where we instruct the computer to follow the same set of instructions a specific number of times, or forever until some condition is met.  A `for` loop in Python looks like this:
```python
>>> for i in range(3):
...     print('Underpants!')
... 
Underpants!
Underpants!
Underpants!
```
(This sort of thing really is how many of us got started with programming in the 80's.)  

What's going on here?  First of all, a `for` statement has three basic parts:
1. An iterable object that we're looping over.
  In this example, `range` is a built-in function that returns a sequence of integers that starts with `0` and ends with one less than the integer argument.  In Python 3, you can't see this sequence even if you specifically ask for it.  This is because Python 3 is returning a special object that will generate this sequence as numbers when you ask for them; this is more efficient than storing the entire sequence in memory.  I'm still getting used to this -- in Python 2, everything was immediately available to look at.
  ```python
  >>> range(3)
  range(0, 3)
  >>> thing = range(3)
  >>> list(thing)
  [0, 1, 2]
  ```

2. One or more variables for capturing the values being passed from the iterable object.  
  In our example, there's only one integer being passed at a time, so we only need one variable: `i`.  In our first pass through the loop, `i` has the value `0`.  On our second pass, it has the value `1`.  To illustrate:
  ```python
  >>> for i in range(3):
  ...   print(i)
  ... 
  0
  1
  2
  ```
  
3. A code block that is going to be executed every time we pass through the loop.
  This is where we have to get into another basic concept in Python.  A [code block](https://en.wikipedia.org/wiki/Block_(programming)) is a subset of instructions that we want to differentiate from the rest of the instructions.  When we write a `for` loop, for example, we usually don't want Python to execute the entire script multiple times.  A programming language needs to have some means of telling the computer which instructions are in the code block, and which ones are not.  Some languages enclose the code block in a special character.  For example, `C` uses curly brackets (`{` and `}`).  Python uses whitespace: a series of one or more spaces or tabs.  It's one of the defining (but not unique) characteristics of the language. 
  For example, deleting the spaces to the left of the `print` function in the previous example raises an error:
  ```
  >>> for i in range(3):
... print(i)
  File "<stdin>", line 2
    print(i)
        ^
IndentationError: expected an indented block
  ```
  All lines that begin with the same whitespace that come immediately after the `for` statement are included in the code block.  The next line to start with different whitespace closes the code block.  For example, this script:
  ```python
  for i in range(3):
    print(i)
  print('now stop')
  ```
  produces the following output:
  ```shell
  [Elzar:courses/GradPythonCourse/examples] artpoon% python foo.py
  0
  1
  2
  now stop
  ```
  Caveat: this example will raise a syntax error in interactive mode.  It's just [one of those quirks](https://docs.python.org/3/tutorial/interpreter.html#interactive-mode) of the interactive mode.
  
![](https://imgs.xkcd.com/comics/ducklings.png)


### `while` loops

Think of running a simple script as water running down a pipe.  We've covered for-loops; these are like pumps that send water upwards for a while.  Another control statement that has a similar effect is the `while` loop:
```python
>>> i = 0
>>> while i < 5:
...     print('pants!')
...     i += 1  # shorthand for `i = i + 1`
... 
pants!
pants!
pants!
pants!
pants!
```
There are a few structural differences between `for` and `while` loops.  In Python, a `for` loop is defined by an iterable object, such as a string or a list.  A `while` loop is defined by a stopping condition.  This can make it slightly more useful than a `for` loop when you need to do something repeatedly until some condition is met, and you can't anticipate how long the loop has to run.  For example, here's a `while` loop that repeats until we get a random integer that's divisible by 7:
```python
>>> import random  # load a module - we'll learn about these later
>>> while True:
...     y = random.randint(0,1000)
...     print(y)
...     if y % 7 == 0:  # modulus operator; 11%7 is 4, the remainder
...         break
... 
683
503
922
244
49
```
Note that the instructions that are being repeated by the `while` loop are indented by some whitespace, just like how we structure our `for` loops.  The whitespace defines the code block affected by the loop.  Off the top of my head, I can't think of a simple way to implement this with a `for` loop.  Also, this `while` loop can *conceivably* go on for a very long time -- I can't think of a simple way to implement a potentially infinite `for` loop.

![](https://imgs.xkcd.com/comics/loop.png)

So far the way we've written loops requires that every pass through the loop evaluates the same set of instructions (not withstanding instructions tucked into an `if` statement).  Some times we need to short-circuit the flow within a loop.  In the example above, I've used a `break` statement that exits out of a `while` loop that would otherwise run on forever.  A `break` will only exit its own loop - it won't affect an outer loop that it is nested within.  For example:
```python
>>> for word in ['one', 'two', 'three']:  # outer loop
...     for letter in word:  # inner loop
...         print(letter)
...         if letter in 'nwr':
...             break  # only exits the inner loop
...     print('')  # print tacks on line break onto empty string
... 
o
n

t
w

t
h
r

```

When we break out of a loop, none of the subsequent iterations get run.  Often, we want to jump back to the top of the loop when a certain condition is met, instead of breaking out of it entirely -- then the loop keeps chugging along as if nothing's happened.  The `continue` statement serves this purpose:
```python
>>> for i in range(10):
...     if i % 2 == 0:
...         continue  # jump to top of loop
...     print(i)
... 
1
3
5
7
9
```

One more thing - it's often useful to have a counter variable that's updated with the index of every item of the iterable object we're looping over.  (In other words, "This is the first thing!  This is the second thing!" and so on.)  This is simple enough to write:
```python
>>> counter = 0
>>> for pet in ['fish', 'dog', 'puppy']:
...     print(pet)
...     print(' bark'*counter)
...     counter += 1
... 
fish
 
dog
 bark
puppy
 bark bark
```
Since we often need to use a loop counter, however, Python provides a slightly simpler and more integrated way to do it:
```python
>>> for counter, pet in enumerate(['fish', 'dog', 'puppy']):
...     print(pet)
...     print(' bark'*counter)
```
The `enumerate` function returns tuples with two members:
1. The loop counter (an integer index for the iterable member currently assigned to our holding variable).
2. The holding variable itself.



## Conditional statements

If `for` and `while` loops are like pumps that recycle the water up to a higher section of the pipe, then `if` and `else` statements are like diverters in the pipe -- they split the flow in one direction or another.  Conditional statements are a fundamental component of programming languages, since we usually don't want to do *exactly* the same thing to every value that passes through our instructions.  There are different ways of structuring conditionals.  The simplest is a single `if` statement:
```python
>>> for i in range(5):
...     if i == 3:
...         print('Three.')
...     print(i)
... 
0
1
2
Three.
3
4
```
The second `print` statement is executed *every* time we pass through the loop, but the `if` statement is triggered only *once*.  When we get to the bottom of this `if` statement, we continue on through the rest of the loop as though nothing happened.

You might be wondering about the double-equals sign `==`.  This is different than the assignment operator that uses a single equals sign (`=`).  Instead, it is a test of whether the left side is equivalent to the right side, and returns a `True` or `False` value.  Here are some other tests and logical operators:
```python
>>> a = 5  # assignment
>>> a == 5  # equality test
True
>>> a != 5  # inequality test
False
>>> not a == 5  # inverting the equality test has the same effect
False
>>> a < 6  # is less than
True
>>> a > 6  # is greater than
False
>>> a <= 5  # is equal to or less than
True
>>> a == 'five'  # silly but valid
False
>>> a == 5 and False  # both tests must evaluate True
False
>>> a != 5 or True  # either test can evalute True
True
>>> a == 5 or (True and False)  # use brackets to determine order of operations
True
>>> (a == 5 or True) and False
False
```


Here is a slightly more complicated set of conditional statements:
```python
>>> for i in range(5):
...     if i == 3:
...         print('Three.')
...     else:
...         print(i)
... 
0
1
2
Three.
4
```
The `else` statement is triggered if *none* of the conditions are met -- in this case, there is only one condition.  This structure is more like a pipe diverter; the flow can only go one way or another.  Any instructions you want to be applied to all items in the `for` loop can be placed outside the conditional statements:
```
>>> for i in range(3):
...     print('before')
...     if i == 1:
...         print('One.')
...     else:
...         print(i)
...     print('after')
... 
before
0
after
before
One.
after
before
2
after
```

![](https://imgs.xkcd.com/comics/conditionals.png)

Finally, there are `if..elif..else` sequences.  `elif` is an abbreviation of `else if`:
```python
>>> for i in range(4):
...     if i == 0:
...         print('One!')
...     elif i == 1:
...         print('Two!')
...     else:
...         print('Anything else.')
... 
One!
Two!
Anything else.
Anything else.
```
Since `elif` is an abbreviation of `else if`, we can expand it out to this:
```python
>>> for i in range(4):
...     if i == 0:
...         print('One!')
...     else:
...         if i == 1:
...             print('Two!')
...         else:
...             print('Anything else.')
```
Note there are three levels of indentation here!  Every `elif` saves us a level of indentation.

If you're confused about the difference between these sets of conditional statements, it might help to draw out some flowcharts.

![](https://imgs.xkcd.com/comics/flowchart.png)


### Joint conditionals

Sometimes we need to check more than one condition.  For example, what if we want to run a specific code block if `i` is an integer that is both greater than 5 and less than 10?  We need to make use of an `and` operator:
```python
>>> if i > 5 and i < 10:
...     print('yes')
... 
```
What if we want to check if `i` is outside of this interval?  We could write two separate tests:
```python
>>> if i < 5:
...     print('yes')
... 
>>> if i > 10:
...     print('also yes')
... 
also yes
```
but it is more compact to use the `or` operator:
```python
>>> if i < 5 or i > 10:
...     print('simpler')
... 
simpler
```
Finally, we might need to chain together a combination of conditions where some nested conditions are evaluated first, before their results are evaluated at the next level.  We can nest conditions by enclosing them in round brackets:
```python
>>> ((i > 1 and i < 5) or (i > 7 and i < 9))
False
```
but beyond a certain level of complexity, you might save yourself a headache by breaking these conditional statements up into separate blocks of code.


## Functions

The last aspect of control flow that we need to cover is functions, which allow the user to direct the computer to run a set of instructions that is entirely separate from the main top-down flow of a particular script.  More importantly, this external set of instructions can be generic: as long as we supply the correct inputs, the function doesn't care where the inputs come from (whether it is one script or another).  

Here is the basic layout of a function in Python:
```python
>>> def silly_function(arg1):
...     return '!' + str(arg1) + '!'
... 
>>> silly_function(1)
'!1!'
>>> silly_function('booger')
'!booger!'
```

* `def` tells the interpreter that the following code block belongs to a user-defined function
* `silly_function` is an arbitrary name for our new function.  This name is what we use to invoke the function once it's been defined.  Like variables, Python has some strict rules and some general guidelines about function names:
  * function names must start with a letter
  * names should use underscores to separate words instead of camelCase
* `arg1`: within the parentheses following the function name is a series of one or more arguments, which are identified by variable names.  These variable names only apply to the code block within the function.  For example, we can define a variable at global scope (outside the function) and input this variable as the argument for our function:
  ```python
  >>> foo = 'bar'
  >>> silly_function(foo)
  '!bar!'
  ```
Thus, variables defined at the scope of a function won't be recognized outside the function:
```python
>>> arg1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'arg1' is not defined
```
Conversely, variables defined at global scope can be used within a function:
```python
>>> def silly_function(arg1):
...     return foo + str(arg1)
... 
>>> silly_function(1)
'bar1'
```

What happens if we change a globally-defined variable within a function?  Something special!
```python
>>> def silly_function(arg1):
...     foo = 'zip'
...     return foo + str(arg1)
... 
>>> silly_function(1)
'zip1'
>>> foo
'bar'
```
What happened here is that `foo` was redeclared at a local scope within the function `silly_function` and then used to generate the return value `zip1`.  Next, Python returned from the function back to global scope and continued along until we called `foo`, which retained its original value at this scope.

We're not done!  We stil need the following ingredients to complete our function definition:
* A code block.  Remember that blocks are defined by whitespace, and that the convention for Python is an indent of 4 spaces for every level.  Once we drop back to the original level, Python assumes that we are past the end of the function definition.
* A return value (not strictly necessary but typical).  A `return` statement exits the function and transmits one or more variables back to the point of the script where the function was called.  To return more than one variable, you can separate the variable names with commas.
  ```python
  def transfer(l1, l2):
    if type(l1) is not list or type(l2) is not list:
        return None
    l2 = [l1[-1]] + l2  # add last item of l1 to left of l2
    l1 = l1[:-1]  # drop the last item
    return l1, l2

  l1 = [1,2,3]
  l2 = [7,8,9]
  result = transfer(l1, l2)
  print(type(result))
  print(result)
  ```
  Running this script generates the following output:
  ```shell
  art@Kestrel:~/Desktop$ python3 example3.py 
  <class 'tuple'>
  ([1, 2], [3, 7, 8, 9])
  ```

### Positional and keyword arguments

So far we've only called functions with one or more *positional* arguments - the identity of an argument is determined by where it appears in the order of arguments (first, second, etc.).  A second approach is to call the function with keyword arguments.  If we modify the previous script as follows:
```python
result = transfer(l2=[7,8,9], l1=[1,2,3]) 
```
then we obtain the same results even though we've swapped the order of `l1` and `l2` arguments.  

It is possible to use a mixture of positional and keyword arguments in a function call, but the positional arguments have to appear before the keyword arguments.  


### Recursive functions

