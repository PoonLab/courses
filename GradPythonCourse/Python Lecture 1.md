# **Python Lecture 1**

## What is a scripting language?

A programming language provides a convenient way for a person to write a set of instructions for a computer to follow.  Put another way, a programming language adds a level of [abstraction](http://stackoverflow.com/questions/21220155/what-does-abstraction-mean-in-programming) that are converted into the low-level instructions that are actually being carried out at the level of the processor.  In general, the processing of converting human-readable instructions (source code) into computer-readable instructions (machine code) is compiling.  

[Compiled programming languages](https://en.wikipedia.org/wiki/Compiled_language) are far more convenient than direclty writing machine code -- the cost for this convenience, however, is that the end result is not necessarily the most optimal machine code for a given processor.  ([Programs that are written in assembly language](https://en.wikipedia.org/wiki/RollerCoaster_Tycoon_(video_game)#Development), which has a lower level of abstraction than compiled languages, can outperform the latter.)  You may have heard of several different compiled languages, such as C, BASIC, or Fortran.

Compiling can take a long time.  Before multi-core processors became commonplace, compiling your code was a good excuse to take a break.

![](https://imgs.xkcd.com/comics/compiling.png)

A scripting language provides an even higher level of abstraction than compiled languages, which enables them to be far more readable and concise.  Scripting languages are often implemented in a compiled language.  For example, the main Python interpreter was written in C.  Instead of being compiled into an executable binary program, however, a script is typically converted at [run-time](https://en.wikipedia.org/wiki/Run_time_(program_lifecycle_phase)) into a number of elementary tasks that have already been implemented in the compiled code.  Because of this additional layer of abstraction, a program written in a scripting language is generally going to be slower than one written in a compiled language.  On the other hand, the scripting language program is a lot easier to write.  (Like making macaroni and cheese with a Kraft Dinner mix instead of growing a wheat field, harvesting the grain, milling the grain into flour...)


## Why scripting?
Scripting languages have become an important part of bioinformatics, but why did this happen?  I don't think there's an obvious answer for this.  Part of it may have been historical contingency.  The scripting language [Perl](https://en.wikipedia.org/wiki/Perl) became associated with the [Human Genome Project](https://en.wikipedia.org/wiki/Human_Genome_Project).  There's a nice article about this historical development [here](https://web.stanford.edu/class/gene211/handouts/How_Perl_HGP.html), including a quote that encapsulates this association nicely:

>Some groups attempted to build large monolithic systems on top of complex relational databases; they were thwarted time and again by the highly dynamic nature of biological research. By the time a system that could deal with the ins and outs of a complex laboratory protocol had been designed, implemented and debugged, the protocol had been superseded by new technology and the software engineers had to go back to the drawing board.
- [Lincoln Stein](https://en.wikipedia.org/wiki/Lincoln_Stein)

In the post-genome era, this has remained true - the reduced one-time cost of developing a script tends to win over the performance advantage of compiled code that is more time-consuming to build.  There is a perpetually expanding range of biological applications for new molecular technologies.  The scale and complexities of data sets are constantly evolving.  In addition, scripting languages are simply easier for biologists to learn.  


## Perl, Python and Ruby

I think that for a long time, Perl was the [lingua franca](https://en.wikipedia.org/wiki/Lingua_franca) of bioinformatics.  However, [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) and [Ruby](https://en.wikipedia.org/wiki/Ruby_(programming_language)) are two slightly newer scripting languages that were directly influenced by Perl.  Recently, Python [has arguably displaced Perl](https://www.fastcompany.com/3026446/the-fall-of-perl-the-webs-most-promising-language) as the leading langauge for bioinformatics, as well as other industries and outside of academia.

Perl, Python and Ruby have different programming philosophies.
<script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/981_RC01/embed_loader.js"></script> <script type="text/javascript"> trends.embed.renderExploreWidget("TIMESERIES", {"comparisonItem":[{"keyword":"perl","geo":"","time":"all"},{"keyword":"ruby","geo":"","time":"all"},{"keyword":"python","geo":"","time":"all"}],"category":0,"property":""}, {"exploreQuery":"date=all&q=perl,ruby,python","guestPath":"https://trends.google.ca:443/trends/embed/"}); </script> 


# Base Objects
* Non-iterable 
  * Integers
    * Whole numbers
    * Example: 27
  * Floats
    * Have decimal
    * Example: `3.41`
* Iterable
  * Strings (not mutable)
    * Essentially an assortment of characters (ie. letters, numbers, punctuation)
    * Can be declared using single or double quotation marks
    * Example: `"apple"`
  * List (mutable)
    * Used for storing an assortment of data types (ie. integers, floats, strings, etc.)
    * Can be delcared using square brackets
    * Example: `[27, 3.41, ‘apple’]`
  * Tuple (not mutable)
    * Essentially an "unadjustable" list
    * Can be declared using parentheses 
    * Example: `(27, 3.41, 'apple')`
  * Dictionaries (mutable)
    * Used for pairing keys to objects
    * Can be declared using curly brackets
    * Example: 

```
    Sarah= {}
    Sarah["lunch"]= "salad"
    Sarah["dinner"]= "potroast"
    Sarah
    {'lunch':'salad', 'dinner':'potroast'}
```
 
 **Question** Sarah skipped her lunch break to run an experiment in lab, how do we change the dictionary?
 
```
    del Sarah["lunch"]
    {'dinner':'potroast'}
```

# Dynamic Typing
* a=7 (integer)
* Note: you are assigning the integer 7 to 'a'
* When you type 'a' into python, it will be defined as 7
* 'a' can also be a string, float, etc.

# Important Note: Python is a Zero-based Index
* What does this mean?
* Let's use this example to explain:
```
  a= "apple"
  a[0]...'a'
  a[3]...'l'
  a[0:2]...'ap'
  a[1:-1]... 'ppl'
```

# Manipulation of Strings:
* Combining two strings:
 * Concatenation
 ```
 a= "red" + "dog"
 'reddog'
 for a in "reddog"**:**
 print("z"+a)
```
 * *What do you get?* 
 
* Combining numbers and strings (aka Cast and Concatenate):
 * Example:
 ```
 a= 3 
 b= "cookies"
 c= a+b
 ```
 **Note**: You will receive an error.
 ```
 c= str(a) + b  
 c
 '3cookies'
 ```
* Using a place holder
```
 "%d" %NUM= substitute INTEGER
 "%f" %NUM= substitute FLOAT
 ```
 * Example:
 ```
 a= 1207
 b= "room%d"%a
 b
 'room 1207'
  ```

# Manipulation of Lists
* Adding values to the end of a list
 * Append(VALUE):
 * Example:
 ```
  a= [3, 'apple', 67.2]
  a.append('sheep')
  a
  [3, 'apple', 67.2, 'sheep']
  ```
 * Adding values to the middle of a list
  * insert(Location, VALUE):
  * Example:
  ```
  a= [3, 'apple', 67.2]
  a.insert(1, 'sheep')
  a
  [3, 'sheep', 'apple', 67.2]
  ```
  * **Note:** Remeber that python is a *zero-based index*!
 * Remove a value at a specific location
 ```
  pop(location)
  a= [3, 'sheep', 'apple', 67.2]
  a.pop(1)
  a
  [3, 'apple', 67.2]
  ```
 * Converting items to a list
 ```
  list(item)
  list("western university")
  ['w', 'e', 's', 't', 'e', 'r', 'n', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
```


# Operators
* Function that acts on objects
* Examples:
  * add +
  
    * Example: 
    ```
    a= 1+2=3
    a= "western"+"university"= "westernuniversity"
    ```
    
  * Subtract -
  * Divide /
  * Multiply *
    * Example: 
    ```
    a=3*4=12
    a= "bird"*3= 'birdbirdbird'
    ```
  * Power/Exponent **  
  
