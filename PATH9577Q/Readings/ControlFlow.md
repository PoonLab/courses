# Control flow

[Control flow](https://en.wikipedia.org/wiki/Control_flow) determines how the computer moves through a set of instructions. Like many scripting languages, Python generally starts at the top of an instruction set and progresses downwards.  This downward flow can be interrupted by an instruction for Python to repeat a specific block of code a number of times (iteration).  It can also be diverted into separate streams depending on whether one or more specific conditions are met ([conditional branching](https://en.wikipedia.org/wiki/Branch_(computer_science))).  Finally, the program can be temporarily switched to a completely different set of instructions before continuing on the original flow ([subroutines](https://en.wikipedia.org/wiki/Subroutine)). 

In Python, these aspects of contorl flow are accomplished by iteration (with `for` and `while`), conditional statements (`if` and `else`), and by defining and calling functions (`def`).  


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
Since this comes up so often, however, Python provides a slightly simpler and more integrated way to do it:
```python
>>> for counter, pet in enumerate(['fish', 'dog', 'puppy']):
...     print(pet)
...     print(' bark'*counter)
```
The `enumerate` function returns tuples 



## if-else conditionals

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

## Functions

