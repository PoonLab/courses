# Writing good code

We've spent most of the course covering basic concepts and methods in Python that are relevant to data processing for bioinformatics.  To cap this off, we should talk about how to use what we've learned to make *good* code.  I'm going to focus on two aspects of making good code: writing code that is easy to *maintain*, and writing code that is easy to *use*.  These topics are known as [code maintainability](https://softwareengineering.stackexchange.com/questions/134855/what-characteristics-or-features-make-code-maintainable) and [user experience](https://en.wikipedia.org/wiki/User_experience).  

I'm *not* going to address the performance aspect of writing good code.  As students in biology and medical sciences who are just starting out with programming, learning how to write maintainable and user-friendly code is far more important than learning how to optimize your code for maximal performance.  (However, this hasn't stopped me from pointing out some easy steps for improving code performance, like [using dictionaries for searches](Dictionaries.md#performance) or [processing file streams line by line](SequenceData.md#fasta)).


## What is maintainable code?

Maintainable code can be read by another person, who will be able to:
1. use your code with confidence that it is doing what they expect it to;
2. not have to spend days picking apart the code to understand it;
3. understand it well enough to modify it without breaking something.

Even if you don't intend for anyone else to use your code, you will always be writing it for someone else: *you*.  Months from now when you return to your code, if your code hasn't been written to be maintainable then you will have created a "black box" for yourself.  So do yourself a big favour and write clean, readable code with sufficient commenting and documentations, or you'll be creating more work for your future self.

![](https://imgs.xkcd.com/comics/future_self.png)

Code maintainability is subjective - that doesn't mean that it doesn't exist, or that we can't generally agree on what constitutes "maintainable" code and what doesn't.  There are a few simple things that you can do to make sure that your code will be useable by yourself, or by others, for months or even years to come.  We'll cover a few of these things during this class.


## Style

Talking about "style" in relation to coding may seem frivolous, but it is actually an important part of writing maintainable code.  When you write code, there are a number of decisions that you make that make no difference to the computer, but can make a significant difference to how easily others can read and understand what you've written.  How you tend to make these decisions defines your coding style.  

Python is notorious for placing style front and centre, to the point that a script won't run properly if you've been inconsistent with indenting blocks of code.  One of the defining documents of the Python language is the [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/): a set of recommendations or conventions about these decisions you'll have to make.  In this section, I will constantly refer to PEP 8 - if you don't feel very strongly about writing in one style or another, why not try to adhere to a style that your colleagues have agreed upon?

![](https://imgs.xkcd.com/comics/standards.png)

Google also has a [style guide](https://google.github.io/styleguide/pyguide.html) for Python that is worth reading.

Here is a Python that will calculate and output nucleotide frequencies from a FASTA file:

```python
import sys
a='ACGT'
z=open(sys.argv[1],'rU')
b=dict(map(lambda x:(x,0),a))
for x in z:
 if x[0]=='>': continue
 jj = filter(lambda xx:xx in a,x)
 for j in jj: b[j]+=1
print(b)
```
To save you from having to type this out, I've added this script to the repo as `examples/badcode.py`.

This script works, but it's difficult to read.  I consider this to be an unmaintanable implementation.  When I run it on a file, I get the following output
```shell
[Elzar:courses/GradPythonCourse/examples] artpoon% python badcode.py Decapod-PEPCK.fa 
{'G': 10262, 'C': 11992, 'A': 9009, 'T': 7845}
```

![](https://imgs.xkcd.com/comics/code_quality_3.png)

Here is a rather different implementation that accomplishes exactly the same task (you can find it at `examples/goodcode.py`):

```python
"""
Calculate nucleotide frequencies from a FASTA file
"""

import sys

nucleotides = 'ACGT'  # which symbols to count

def count_bases(path):
    """
    Open a FASTA file that contains nucleotide sequences, count the total numbers of 
    nucleotides (defined globally above), and return the result as a dictionary.
    """
    # prepare results container
    freqs = {}
    for nuc in nucleotides:
        freqs.update({nuc: 0})
    
    # iterate through file contents
    handle = open(path, 'rU')
    for line in handle:
        if line.startswith('>'):
            # this line contains a record header, ignore
            continue
        
        # otherwise the line contains sequence
        for char in line:
            if char in nucleotides:
                freqs[char] += 1  # increment this base count
    handle.close()
    
    return(freqs)


def main():
    # check number of arguments
    if len(sys.argv) != 2:
        print ("Usage: python nucfreqs.py [input FASTA]")
        sys.exit()
    
    path = sys.argv[1]
    freqs = count_bases(path)
    
    # send formatted output to console
    print ("Base\tCount")
    for nuc, count in freqs.items():
        print ("{}\t{}".format(nuc, count))

if __name__ == '__main__':
    main()
```

Running this script on the same FASTA file produces the following output:
```shell
[Elzar:courses/GradPythonCourse/examples] artpoon% python goodcode.py Decapod-PEPCK.fa
Base    Count
A       9009
C       11992
T       7845
G       10262
```
(Note that I've padded the whitespace with spaces because the GitHub interface doesn't support tabs.  Also, the order of rows in this output table can change every time you run the script because a dictionary is not an ordered collection.)

The second version is substantially longer -- in fact, there are more than **five** times as many lines of code (51 versus 10).  To some, this may seem horribly inefficient.  However, a script will rarely occupy a substantial amount of space on your hard drive.  In fact, a single Python script probably shouldn't take up much more than a thousand lines.  If you're getting way over that number, then you might want to think about splitting that script up into two or more scripts and building a module.  

Even if you just *have* to write a script that takes tens of thousands of lines of code, you're *still* not going to consume a lot of space on your hard drive.   You'd have a really hard time making the script take up much more than a megabyte of space - about a tenth the size of a typical MP3 audio file.  Why bother making your script smaller?  The benefit you get from making your code more readable *vastly* outweighs the cost of making a longer script, especially now that nowadays your typical hard drive has its capacity measured in *terabytes* (roughly a million megabytes).  

Let's go through the PEP8 style guide and skim over some of the differences between these two scripts.

### Indentation

Python is notorious for enforcing strict rules about indenting your code.  In the first case, I skirted this issue by indenting blocks of code with the bare minimum (a single space) or by keeping code on the same line to avoid the issue altogether.  This is succinctly illustrated by these two lines:
```python
for x in z:
 if x[0]=='>': continue
```

In the second example, I adhered to [PEP8](https://www.python.org/dev/peps/pep-0008/) recommendations and used four spaces for each level of indentation.  A decent text editor or [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) will take care of this for you, so you're not constantly tap-tapping away at your space bar.  Why spaces and not tabs?  The most persuasive argument I've heard for spaces is that different operating systems and applications will have different interpretations of tab characters.  If you open a tab-indented script in some text editors then you may see lines indented the equivalent of *8* spaces instead of 4, which can get messy real fast!  

### Whitespace

[PEP 8](https://www.python.org/dev/peps/pep-0008/) has some specific recommendations about whitespace.  I don't feel strongly about many of these recommendations, but you would probably agree that this:
```python
b = dict(map(lambda x: (x,0), a))
```
is easier to read than this:
```python
b=dict(map(lambda x:(x,0),a))
```

### Variable naming conventions

In my "bad" script, I used a lot of single- and double-letter variable names that had no clear association with their intended role.  (This actually made it difficult to write the code, because I kept forgetting what specific variables were supposed to represent.)  This line is particularly horrible:
```python
jj = filter(lambda xx:xx in a,x)
```
Even if I expand this code out to use a simpler for-loop structure, it's still not clear what's going on:
```python
j = ''
for xx in x:
    if xx in a:
        j += xx
```  

Here is the same code with more reasonable variable names:
```python
new_string = ''
for char in old_string:
    if char in nucleotides:
        new_string += char
```
Doesn't this make a huge difference?  I certainly think so!

Every programming language has to enforce some rule about variable names, or else it may get confused about where the variable name ends and the code begins.  In Python, a variable name may contain any letters, numbers or underscores, and cannot start with a number.  [PEP 8](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles) goes further with suggestions about how to format more complex variable names.  For example, my `old_string` variable name uses an underscore to separate words.  Another acceptable approach is known as *camelcase*: `oldString`.  You are free to choose whatever naming style you want, but you *should* be consistent!

![](https://imgs.xkcd.com/comics/sigil_cycle.png)


### Shortcuts

One of the [core philosophies](https://www.python.org/dev/peps/pep-0020/) of the Python language is that:
> There should be one-- and preferably only one-- way to do it

Even so, there are certainly many ways of writing the same code.  For this class, we've been focusing on the most basic, generic approaches to getting something done with Python.  However, there are other methods that are more succinct and even more visually appealing -- on the other hand, they can lead to code that is difficult to read, and they can involve more advanced concepts in programming such as [anonymous functions](https://en.wikipedia.org/wiki/Anonymous_function).  I think that the decision of whether or not to use some of these "shortcut" methods is a question of code style, so I've placed a brief explanation on some of (what I think are) the more common shortcuts here.

#### List comprehensions

Here is a generic approach to building up a list:
```python
squares = []  # start with an empty list
for i in range(1, 11):  # iterate over something
    squares.append(i*i)
```
which yields the following list object:
```python
>>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
If you've covered [List objects](Iterables.md), [`for` loops](ControlFlow.md) and basic [arithmetic operations](Variables.md#python-as-a-calculator) in Python, then you should be able to get a handle on what is going on.  

However, there is a more compact way of making this List:
```python
squares = [i*i for i in range(1, 11)]
```
This one-line approach is called a *list comprehension*.  (This statement doesn't *have* to be on one line.  Some times you might want to add some line breaks to make the statement more readable.  This is okay as long as the line breaks occur within the square brackets.)  It is a popular shortcut in Python and you'll encounter it pretty often.  Each element in the list is the result of some *operation* that has been applied to every member of some iterable object.  The basic structure of a list comprehension is as follows:
* All statements are contained within square brackets.
* An operation on the loop variable(s), *e.g.*, `i*i`.
* A series of one or more loop variables to assign values from every iteration, *e.g.*, `i`.
* An iterable object, *e.g.*, `range(1,10)`.
* *optional* A conditional statement that filters entries from the iterable object.  For example, we could amend the above example to output only integers divisible by 3: `squares = [i*i for i in range(1,11) if i%3==0]`

Instead of writing out the operation component of a list comprehension, we could call some function and send the loop variable as the argument.


#### `map` and `lambda` functions

Applying the same operation to a sequence of inputs is a very common task in computing, and there is an even *more* concise way to generate the `squares` list that we produced in the above section:
```python
>>> squares = map(lambda i: i*i, range(1, 11))
>>> squares
<map object at 0x7f5110e45ba8>  # in Python 2, map() used to return a list but now it is a special iterable
>>> list(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
This is even more concise if we have already defined a function elsewhere:
```python
def square(i):
    return i*i

squares = map(square, range(1, 11))  # yields the same result
```
However, we're now starting to make things more and more cryptic.  For example, we can save a bunch of space if `square` is an operation with many lines of code, or requires several arguments; but if the function definition is written somewhere else in the code or imported from another script, then we might have no idea of what's going on.


#### `with`..`as` statements

The `with` statement [defines a context](https://docs.python.org/3/reference/datamodel.html#context-managers) for a block of code, within which a variable holds the value of some expression and does not outside the block.  I usually come across `with` statements used for briefly opening and working with the contents of a file stream.  For example:
```python
with open('file.txt') as handle:
    print(next(handle))
```
instead of:
```python
handle = open('file.txt')
print(next(handle))
handle.close()
```
One of the benefits of using `with` for file streams is that the stream is automatically closed upon exiting the nested code block.  It also results in slightly more concise code!  Other advantages of using `with` statements depend on using [context management] programming of Python classes, which is a topic that is too advanced for this class.


### Modular programming

Modular programming is an aspect of programming style that isn't really spelled out in PEP 8.  Modularity means that we want to break tasks down to components that are self-contained and portable.  The opposite approach is [monolithic] programming where everything is subsumed under a single massive script.  In the above example, I've broken the second script down into two functions, `main` and `count_bases`:

* `count_bases` opens the FASTA file at a given path and computes the overall nucleotide frequencies.
* `main` handles the input/output actions: taking an argument from the command-line, passing this argument to `count_bases`, and then reporting the results to the console.  

There are a number of benefits to breaking down your code this way.  First, if something breaks then you can zero in on a shorter function to diagnose the problem.  Second, this immediately makes `count_bases` function portable so that it can be called from another script.  For example, if I saved my second script as `second.py`, then:
```python
from second import count_bases
```
would enable me to run the `count_bases` function from that other script, which is what I mean by *portability*.

Taking a modular programming approach to a script is useful for thinking about how a complex problem should be broken down into component tasks, and usually produces a more maintainable script than a single "monolithic" one.  Of course, it is possible to take this too far: for example, you *could* make a separate function for checking whether a line of a FASTA file contains a header:
```python
def is_header_line(line):
    """ Check whether a line indicates the start of a new FASTA record """
    return line.startswith('>')
```
and you could continue to break down the script this way into dozens of little functions, but I think you'd end up making your script *less* readable by doing so.  


## Documenting your code

There are two types of documentation: external and internal.  External documentation are contained in separate files that can be distributed with the code, or made available online or even as as print publication.  I generally wouldn't start thinking about external documentation unless the project starts to get big, or if it is likely to be used by other people outside my immediate group.  For example, [MiCall](http://cfe-lab.github.io/MiCall/) is a next-generation sequencing pipeline for clinical genotyping of virus samples, and has a good amount of Markdown documentation that gets rendered into a nice website on GitHub.  

Internal documentation is contained within the source code files themselves.  Since we're focusing on learning how to write data processing and pipelining scripts in Python, we'll focus on internal documentation.  Because internal documentation means writing information right into the source code, we're making use of comments: a comment is a chunk of text that we tell the Python interpreter to ignore by using one or more special characters.  There are generally two types of comments in Python: inline and block comments, and documentation (doc) strings.

An **inline** comment is just that - it occupies a single line of source code.  It should either occupy the line by itself, or it can come *after* (to the right of) a piece of source code, but in Python it never appears to the left of some code.  An inline comment in Python is generally declared with the `#` special character:
```python
a = 1  # this is an inline comment in Python
```
[PEP 8](https://www.python.org/dev/peps/pep-0008/#inline-comments) recommends using inline comments "sparingly" and separating the `#` from the end of any preceding source by at least two spaces.  What qualifies as sparing use of inline comments?  Who knows?  In my opinion, you generally don't want inline comments to outnumber lines of actual code.  Even a 1:3 ratio (25% inline comments) may seem a little excessive - however, there are also times when extensive commenting is called for (like a tricky bit of code).

A **block** comment is simply a bunch of consecutive inline comments:
```python
# This starts the block comment
# ----------------------------------
# We can add whatever we want like the underscore on the previous line.
# And we're expected to keep using the `#` symbol if we want to have a blank
# line separating paragraphs.
# 
# Like that!
```

A **docstring** makes use of a special method in Python for declaring strings that span multiple lines:
```python
'This is a string'  
"This is also a string'
""" Yep, still a string.  It can contain single quotes (') and double quotes ("). """
"""And now 
we're breaking
lines!"""
```

Personally, I prefer using docstrings to block comments because you don't have to keep up with the `#` symbols on every line and I think they look cleaner.
```python
"""
This is how we would use a docstring to create a block of 
comments in the code.  
"""
```

### How do I write documentation?  

When I was in my first highschool computer science class, I struggled a bit with the concept of writing documentation as a formal topic.  Pedagogically, I think it makes as much sense as teaching the [five paragraph structure](https://en.wikipedia.org/wiki/Five-paragraph_essay) for writing essays.  If you're new to coding, however, it's worth covering a few suggestions out there on how to write effective comments.

1. Don't use comments to verbally describe the code.  I lifted this example from the [Google Python style guide](https://google.github.io/styleguide/pyguide.html#Comments):
```python
# BAD COMMENT: Now go through the b array and make sure whenever i occurs
# the next element is i+1
```
This is essentially a word-for-word conversion of the source code; it doesn't actually help me understand what is going on.  If the reader is Python-literate, then they should be able to deduce for themselves what is happening at a low level.  What is not obvious is what you're trying to do at a higher level - the specific objective for that piece of code.

2. Comments should describe what you're trying to do.  In fact, sometimes I write out comments before I start in with the actual source code.  This can be helpful because it lays out the thought process of how the problem can be broken down into pieces, and how those pieces relate to each other.  

3. Have fun with your docstrings!  You can either approach the task of commenting your code as a chore, or you can decide to have fun with it; I advocate the latter.  I'm not alone in this mindset.  There's a lot of programmer humour buried in source code (for example, here is a massive, locked StackOverflow [thread](https://stackoverflow.com/questions/184618/what-is-the-best-comment-in-source-code-you-have-ever-encountered) where users have contributed their favorites -- warning, contains profane language).  This is one of my favourites (it came from a C source file where comments can be enclosed in `/*` and `*/` tags):
  ```C
  /* Emits a 7-Hz tone for 10 seconds.
     True story: 7 Hz is the resonant frequency of a
     chicken's skull cavity. This was determined
     empirically in Australia, where a new factory
     generating 7-Hz tones was located too close to a
     chicken ranch: When the factory started up, all the
     chickens died.
     Your PC may not be able to emit a 7-Hz tone. */
  ```
  Here's a [link](https://stackoverflow.com/a/193705) to the original post.


### Comment tags

Comment tags are an informal standard that has gradually emerged to address a need that wasn't being met otherwise.  Tags allow programmers to annotate comments from a narrowly defined set of labels.  For instance, this can help locate troublesome spots of code that need further work at a later stage of development, because you can search through a large source file for these tags using `grep` or some other utility.  Some IDEs even recognize the standard tags and apply tag-specific [syntax highlighting](https://en.wikipedia.org/wiki/Syntax_highlighting).

| Tag | Usage |
|-----|-------|
| TODO | Identify some feature or enhancement to be implemented at a later stage | 
| FIXME | Identify some section of the code that is broken or incomplete | 
| BUG | Identify a section of code that is broken and ideally provide a minimal reproducible example |
| XXX | Identifies a section of code that is pathologically broken and/or misleading and needs to be replaced |

This rejected Python Enhancement Proporsal, [PEP 350](http://legacy.python.org/dev/peps/pep-0350/#mnemonics), has a fairly comprehensive list of tags.  However, the only two that I've ever used are `TODO` and `FIXME`.  


## User experience

So far we've covered [style](MaintainableCode.md#style) and [documentation](MaintainableCode.md#documenting-your-code).  These are important concepts for making your code maintainable for developers, including yourself.  The last topic we need to cover is how to make your code accessible for users (including yourself!).  Our objective is to improve the [user experience](https://en.wikipedia.org/wiki/User_experience) -- code that is not essential for the program to function properly, but exists to make the code easier and more enjoyable to use.

For example, if we try to run the first example script (that calculates nucleotide frequencies) from the command line *without* providing a second argument (other than the name of the script), then we get an uninformative error:
```shell
[Elzar:courses/GradPythonCourse/examples] artpoon% python badcode.py 
Traceback (most recent call last):
  File "badcode.py", line 3, in <module>
    z=open(sys.argv[1],'rU')
IndexError: list index out of range
```
In order to figure out why this script returns an error, the user would have to open the script in a text editor and peruse line `3`.  This is far too much to expect of someone who doesn't know Python but wants to run your script, and it's a waste of your *own* time in the future when you forget how to run the script.  

The second script is a little more helpful:
```shell
[Elzar:courses/GradPythonCourse/examples] artpoon% python goodcode.py
Usage: python nucfreqs.py [input FASTA]
```
It provides a hint about what went wrong by explaining what additional arguments the script is expecting to receive from the command line.  It also suppresses the unhelpful and intimidating traceback text that Python produces by default.  This is an example of building a helpful interface for your script.  

We're not going to go as far as building a rich graphical user interface with windows and buttons to click on.  (It *is* possible to do this with Python, but unless the script is mature and has a significant population of non-expert users, it's not worth your time to build.)  What we *are* going to do is learn about how to provide some useful information for the user trying to run your script from the command line.

![](https://imgs.xkcd.com/comics/computer_problems.png)

### Helpful interfaces

As usual, this is a frequent need that is met with a standard Python module.  In this case, we are going to learn about the `argparse` module.  I'll illustrate by modifying my "good" script to use this module:
```python
"""
Calculate nucleotide frequencies from a FASTA file
"""
import argparse

nucleotides = 'ACGT'  # which symbols to count

def count_bases(path):
    """
    Open a FASTA file that contains nucleotide sequences, count the total numbers of 
    nucleotides (defined globally above), and return the result as a dictionary.
    """
    # prepare results container
    freqs = {}
    for nuc in nucleotides:
        freqs.update({nuc: 0})
    
    # iterate through file contents
    handle = open(path, 'rU')
    for line in handle:
        if line.startswith('>'):
            # this line contains a record header, ignore
            continue
        
        # otherwise the line contains sequence
        for char in line:
            if char in nucleotides:
                freqs[char] += 1  # increment this base count
    handle.close()
    
    return(freqs)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Calculate nucleotide frequencies from a FASTA file."
    )
    parser.add_argument('path', help='<input> Relative or absolute path to a FASTA file')
    return parser.parse_args()


def main():
    args = parse_args()
    freqs = count_bases(args.path)
    
    # send formatted output to console
    print ("Base\tCount")
    for nuc, count in freqs.items():
        print ("{}\t{}".format(nuc, count))

if __name__ == '__main__':
    main()
```

The first thing you should notice is that we've imported the `argparse` module:
```python
import argparse
```
Also note that I've dropped the `sys` module because I'm not using it anymore.  

> You should always keep your imports at the top of the file so that you can expect to see them in one place.  While it is possible to load modules at other locations of the code, this makes your code more difficult to maintain.  It is extremely annoying to have to hunt around for an `import` statement in the code.


Next, we've added a new function that I called `parse_args`:
```python
def parse_args():
    parser = argparse.ArgumentParser(
        description="Calculate nucleotide frequencies from a FASTA file."
    )
    parser.add_argument('path', help='<input> Relative or absolute path to a FASTA file')
    return parser.parse_args()
```
This function is where we are making use of functions from the `argparse` module.  First, I've constructed an `argparse.ArgumentParser` object that is responsible for processing arguments from the command line.  When I call the constructor for this class, I'm passing a string with the `description` keyword that should provide exactly that - a brief description of what this script is for. 

> Note that I've broken lines in calling this constructor function.  I *could* have kept this function call on a single line, but I like breaking it up to span multiple lines when I'm entering more than a few keyword arguments, or entering a long string as a keyword argument.  This is consistent with the [PEP 8](https://www.python.org/dev/peps/pep-0008/#maximum-line-length) recommendation to limit lines to 79 characters in length, but I also do it because I think it looks nice :)

Next, we're calling the class function `add_argument` to define a command-line argument for the script.  The first argument of this function is postional (no keyword) and is a name that we will use to retrieve this command-line argument once the arguments have been parsed.  By default, this command-line argument is required.  If we want to make an optional argument, we just have to prefix the name with a single dash `-` or two dashes `--`.  The convention is to use a single dash for a one character argument, and double dashes for a word argument:
```python
    parser.add_argument('-z', help="<optional> This does absolutely nothing useful.")
    parser.add_argument('--foobar', help="<optional> This also does absolutely nothing useful.")
```
Note that you should add these lines after declaring your `ArgumentParser` object, and before calling its `parse_args` function.

Optional arguments are identified by their flag (*e.g.,* `-z`) and can be called anywhere in the command-line invocation.  For example, this is fine:
```shell
python good2.py Decapod-PEPCK.fa -z 1 --foobar foofus
```
and this is just as fine:
```shell
python good2.py --foobar foofus -z 1 Decapod-PEPCK.fa
```
but this is not okay:
```shell
python -z 1 good2.py --foobar foofus Decapod-PEPCK.fa
```
Any arguments that are *not* optional are treated as positional arguments on the command line.  Their order of appearance matters because there is nothing else to indicate that which value should be passed as which argument.  

> These examples assume that you want to pass some string or number as a optional keyword argument.  Sometimes you don't want to pass *anything* - you just want to tell Python to do something differently.  To do this, you can change the default `action` from `store` (store the value) to another setting like `store_true`, which causes the `True` value to be assigned if the option is used.

Calling `parse_args` parses the positional and optional keyword arguments from the command-line and assigns them to a `Namespace` object.  All that we need to know about this kind of object is that we can retrieve the parsed arguments from the command line by referring to them by name:
```python
>>> args.path
'Decapod-PEPCK.fa'
>>> args.z
'1'
>>> args.foobar
'foofus'
```
Note that these are all string objects by default.

Now if we run our script without the required argument, we get some feedback that's a bit more helpful:
```shell
[Elzar:courses/GradPythonCourse/examples] artpoon% python good2.py 
usage: good2.py [-h] [-z Z] [--foobar FOOBAR] path
good2.py: error: the following arguments are required: path
```
and if we pass the optional `-h` argument, we get more information in a nice format:
```shell
[Elzar:courses/GradPythonCourse/examples] artpoon% python good2.py -h
usage: good2.py [-h] [-z Z] [--foobar FOOBAR] path

Calculate nucleotide frequencies from a FASTA file.

positional arguments:
  path             <input> Relative or absolute path to a FASTA file

optional arguments:
  -h, --help       show this help message and exit
  -z Z             <optional> This does absolutely nothing useful.
  --foobar FOOBAR  <optional> This also does absolutely nothing useful.
```
This immediately improves user experience - instead of having to peruse the contents of the script, the user is rewarded for naively entering `python <name of script>` with helpful information instead of an error-laden blerp.


### Sanity checks

What happens if a user tries to run our script on a JPEG of an alignment instead of a plain-text FASTA file?  In the help document, all that we've asked them for is to specify a path to a FASTA file, but what if the user isn't sure what a FASTA file is?  What if someone else corrupted the FASTA file, or overwrote it with a recipe for brownies?  The problem is that our script doesn't care whether the file is legitimately a FASTA file or not - it will happily count up the number of nucleotide symbols no matter what kind of file it is!  For example, I ran our script on a bowtie2 index binary file and there were no complaints:
```shell
Base	Count
A	170898
C	194198
T	202566
G	156730
```
Just as a reminder, here are the first two lines of this binary file:
```shell
is2882:examples art$ head -n2 chr7.1.bt2
??B	
????gC|	'etO???4t{???8x?I?A?yA???I|,??05????A??t?[ ???????Y$;???i???T   2?J?3	Ax4AP@?0
                                                                                        DE@@1@@?EP@P?LP?@0?@-D
```
*Not* a FASTA file.

This is dangerous behaviour - if we ran our script on the wrong kind of file, we would have no idea that the results are complete bogus.  We need to add some checks to our script to prevent the user from getting caught by this kind of mistake.  I refer to these as [sanity checks](https://en.wikipedia.org/wiki/Sanity_check).  A sanity check is a very simple test to determine whether some part of the system is working as expected.  

A nice clean way of implementing sanity checks is with a Python `assert` statement, which comprises a test and a message to be sent to the console before throwing an exception, which will cause the script to exit prematurely if it's being run in non-interactive mode.  For example:
```python
>>> assert 1==0, "This won't work!"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: foo
```
Since a failed assertion will exit a running script, you want to make the failure message as informative as possible -- for example, it's helpful to use a formatted string to embed the relevant variables:
```python
s = 'door'
assert s.startswith('f'), "String '{}' did not start with expected 'f' character".format(s)
```

> The `assert` statement is meant to be used for debugging code in development.  Consequently, there is extra information reported in the form of a [traceback](https://en.wikipedia.org/wiki/Stack_trace), which displays where we were in code execution in relation to (potentially nested) routines encoded by the script.   We're discouraged from retaining it in polished (production-level) code.  If you want to exit more cleanly, you can use the `sys.exit()` command after printing some helpful information.


Checking whether a file is plain text or binary is more complicated than we can fit into an `assert` statement, so I'm going to borrow a function from this [StackOverflow thread](https://stackoverflow.com/questions/898669/how-can-i-detect-if-a-file-is-binary-non-text-in-python).  I've made a couple of modifications to make this function run faster by checking less of the file:
```python
def is_binary(filename, max_chunks=100):
    """Return true if the given filename is binary.
    @raise EnvironmentError: if the file does not exist or cannot be accessed.
    @attention: found @ http://bytes.com/topic/python/answers/21222-determine-file-type-binary-text on 6/08/2010
    @author: Trent Mick <TrentM@ActiveState.com>
    @author: Jorge Orpinel <jorge@orpinel.com>"""
    fin = open(filename, 'rb')
    try:
        CHUNKSIZE = 1024
        chunk_count = 0
        while 1:
            chunk = fin.read(CHUNKSIZE)
            chunk_count += 1
            if '\0' in chunk: # found null byte
                return True
            if len(chunk) < CHUNKSIZE or chunk_count > max_chunks:
                break # done
    finally:
        fin.close()
    return False
```
This function opens the file in binary mode and scans pieces for a [null byte](https://en.wikipedia.org/wiki/Null_character) that is diagnostic of many, but not all, binary files.   

Next, we need a function that predicts whether the contents of a file are consistent with the FASTA format and contain nucleotide sequences.  This is a bit tricky because the number of lines containing sequence information per record may vary, and there are not clean-cut methods for classifying a sequence as nucleotide or amino acid.  Here is a crack at it:
```python
def is_fasta(filename, maxline=100):
    """ Try to guess if the file is a valid FASTA file with nucleotide sequences """
    pat = re.compile('^[ACGTWRKYSMBDHVN?-]+$')  # regex for nucleotide sequence
    nrecords = 0
    with open(filename, 'rU') as handle:
        for ln, line in enumerate(handle):
            if line.startswith('>'):
                nrecords += 1
                continue
            if not pat.findall(line.upper()) and len(line.strip()) > 0:
                # non-header lines should contain valid nucleotide sequence
                return False
            if ln > maxline:
                break
    if nrecords == 0:
        return False
    return True
```
The `maxline` argument with a default value of `100` tells Python to stop iterating through the file after it's processed 100 lines.  This keeps this function running fast and should give us a fair guess about the content of this file.  We don't want to invest much more effort into diagnosing the file -- if we work harder then we might as well count the nucleotides while we're at it!

Finally, we're going to call these two functions with `assert` statements in the `main` function:
```python
def main():
    args = parse_args()
    
    assert not is_binary(path), "This looks like a binary file - I can't process it."
    assert is_fasta(path), "This doesn't look like a nucleotide FASTA file :-/"
    
    freqs = count_bases(args.path)
    
    # send formatted output to console
    print ("Base\tCount")
    for nuc, count in freqs.items():
        print ("{}\t{}".format(nuc, count))
```


### Feedback

I really don't like it when I run a program on the command line and nothing happens.  (Applications with fancy graphical user interfaces can be just as guilty of this.  How often have you clicked a button and been left wondering if the program froze?)  This problem results from a lack of feedback, and it can often happen when you're processing a lot of data and/or asking the program to accomplish something that's very time-consuming.  (I don't know whether *feedback* is the correct term for this, but it seems reasonable to me!)  For example, imagine if you ran an unfamiliar script and waited for five minutes with nothing happening on the screen.  I don't know about you, but I'd start to wonder what was going on.  

![](https://imgs.xkcd.com/comics/estimation.png)

There are different ways of reporting the progress of a job back to the user.  For example, there is a rather nice [module](https://pypi.python.org/pypi/progressbar2) for implementing a progress bar in your script, but this is probably overkill in most cases.  Instead, I suggest interspersing `print` statements in your script to provide some crude progress monitoring.

> Python 3's `print` function is definitely an improvement on Python 2.  For example, you can now tell Python to print strings to the console without automatically appending a line break by setting the `end` keyword argument to an empty string `''`.  You can also tell Python to update the console by setting `flush=True`.  We used to have to do this by importing the `sys` module and running `sys.stdout.write()` and `sys.stdout.flush()`.


First, we need to identify the most time-consuming section of the script.  This should be the main loop in the `count_bases` function.  
```python
def count_bases(path, wait=1e4):
    """
    Open a FASTA file that contains nucleotide sequences, count the total numbers of 
    nucleotides (defined globally above), and return the result as a dictionary.
    """
    # prepare results container
    freqs = {}
    for nuc in nucleotides:
        freqs.update({nuc: 0})
    
    # iterate through file contents
    handle = open(path, 'rU')
    for ln, line in enumerate(handle):  # <-- `ln` = line number
        if ln % wait == 0:
            print('.', end='', flush=True)  # provide feedback on progress
        
        if line.startswith('>'):
            # this line contains a record header, ignore
            continue
        
        # otherwise the line contains sequence
        for char in line:
            if char in nucleotides:
                freqs[char] += 1  # increment this base count
    handle.close()
    print('')  # send a line break to console
    
    return(freqs)
```

Running this script on a FASTA file containing a human chromosome 7 sequence consumed about 18 seconds on my Mac desktop - long enough to make me wonder whether an unfamiliar script is functioning properly.  Now that we've modified `count_bases` to provide some visual feedback, I immediately know that the script is still running:
```shell
is2882:examples art$ time python3 good2.py chr7.fa
...............................................................................................................................................................................................................................................................................................................................
Base    Count
A       23318807
T       23314359
G       15510293
C       15532642

real	0m17.760s
user	0m17.526s
sys	0m0.164s
```
Note that `wait` controls the number of lines represented by each `.` symbol.  In this case, I've set the default value to 10,000 lines, which corresponds to about a 1/20th of a second on my computer.

Another nice way to improve the user experience is to expose options like `wait` to the user through `argparse`.  For instance, we can add the following line to `parse_args`:
```python
parser.add_argument('--wait', default=10000, type=int, help="<optional> Number of FASTA lines represented by '.'")
```
and update the corresponding line in the `main` function:
```python
    freqs = count_bases(args.path, wait=args.wait)
```
Now we can tinker with this setting from the command line:
```shell
is2882:examples art$ time python3 good2.py --wait 100000 chr7.fa
................................
Base	Count
T	23314359
G	15510293
A	23318807
C	15532642

real	0m17.437s
user	0m17.256s
sys	0m0.131s
```


### Writing output

The last aspect of user experience that we'll cover is writing output to a file.  We've already talked about [how to prepare output as formatted strings](SequenceData.md#formatted-output) to be written out.  Is there some way to make this process better for the user?  

One thing to consider is *where* we are going to write output to.  In the scripts above, we've used the `print` function to stream output to the console instead of a file, although that output can be [redirected to a file](basicunixcommands.md#bringing-things-together-with-pipes).  In some circumstances, it would be nicer to be able to specify a specific file to write output to - this is especially true if we want to write output to more than one file.  The `argparse` module provides a nice interface for specifying output files:
```python
def parse_args():
    parser = argparse.ArgumentParser(
        description="Calculate nucleotide frequencies from a FASTA file."
    )
    parser.add_argument('path', help='<input> Relative or absolute path to a FASTA file')
    parser.add_argument('out', type=argparse.FileType('w'), help='<output> Path to write output.")
    parser.add_argument('--wait', default=10000, type=int, help="<optional> Number of FASTA lines represented by '.'")
    return parser.parse_args()
```
Passing a `argparse.FileType` object to the keyword argument `type` tells `argparse` that we want to treat the string argument from the command line as a path for opening a file stream in write mode.  Since this new line is the second required (not optional) argument that we added to `parser`, then it is the third positional argument (remember, the first positional argument is the name of the script we're running).  Here is the current help page for our script:
```shell
[Elzar:courses/GradPythonCourse/examples] artpoon% python good2.py -h
usage: good2.py [-h] [--wait WAIT] path out

Calculate nucleotide frequencies from a FASTA file.

positional arguments:
  path         <input> Relative or absolute path to a FASTA file
  out          <output> Path to write output.

optional arguments:
  -h, --help   show this help message and exit
  --wait WAIT  <optional> Number of FASTA lines represented by '.'
```

We always have to be careful about opening a file stream in write mode (`'w'`), because this will automatically create an empty file.  If there was already a file with the same name and location, then its contents have been completely wiped out!  This is not necessarily user-friendly behaviour, so let's talk about how we might prevent this from happening.  How can we do this?  

According to the `argparse` [documentation](https://docs.python.org/3/library/argparse.html), the `type` keyword argument of the `add_argument` function can accept *any* function that takes a single string argument and returns a converted value.  So, let's make a function that will take a string as a path and throw an exception (exit the script) if a file already exists at that path.  In order to do the latter, we need to import yet another module called `os`.
```python
import os

def protectedFileType(path):
    """ Returns an open handle in write mode if the given path does not already have a file """
    assert not os.path.exists(path), "{} exists, no overwrite permitted".format(path)
    return open(path, 'w')
```
Now we can pass this function as our `type` argument:
```python
parser.add_argument('out', type=protectedFileType, help='<output> Path to write output.')
```
The next time we pass the same file as our `out` argument on the command line, Python gets really mad!
```shell
[Elzar:courses/GradPythonCourse/examples] artpoon% python good2.py Decapod-PEPCK.fa temp.out
Traceback (most recent call last):
  File "good2.py", line 115, in <module>
    main()
  File "good2.py", line 102, in main
    args = parse_args()
  File "good2.py", line 98, in parse_args
    return parser.parse_args()
  File "/opt/local/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/argparse.py", line 1726, in parse_args
    args, argv = self.parse_known_args(args, namespace)
  File "/opt/local/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/argparse.py", line 1758, in parse_known_args
    namespace, args = self._parse_known_args(args, namespace)
  File "/opt/local/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/argparse.py", line 1967, in _parse_known_args
    stop_index = consume_positionals(start_index)
  File "/opt/local/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/argparse.py", line 1923, in consume_positionals
    take_action(action, args)
  File "/opt/local/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/argparse.py", line 1816, in take_action
    argument_values = self._get_values(action, argument_strings)
  File "/opt/local/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/argparse.py", line 2257, in _get_values
    value = self._get_value(action, arg_string)
  File "/opt/local/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/argparse.py", line 2286, in _get_value
    result = type_func(arg_string)
  File "good2.py", line 86, in protectedFileType
    assert not os.path.exists(path), "{} exists, no overwrite permitted".format(path)
AssertionError: temp.out exists, no overwrite permitted
```

The downside of this approach is that we can't turn it off.  Unfortunately, I can't think of a way to modify the behaviour of the `protectedFileType` function with a command-line option.  An alternative approach is to capture the output path as a string and add an `--overwrite` option to the parser:
```python
def parse_args():
    parser = argparse.ArgumentParser(
        description="Calculate nucleotide frequencies from a FASTA file."
    )
    parser.add_argument('path', help='<input> Relative or absolute path to a FASTA file')
    parser.add_argument('out', help='<output> Path to write output.')  # plain string type
    parser.add_argument('--wait', default=10000, type=int, help="<optional> Number of FASTA lines represented by '.'")
    parser.add_argument('--overwrite', action='store_true')

    return parser.parse_args()
```
and then modify our `main` function to use these arguments to create output file handles:
```python
def main():
    args = parse_args()
    
    if os.path.exists(args.out) and not args.overwrite:
        print("Error: File exists at path {}.  Use --overwrite option to erase.")
        sys.exit()
    
    assert not is_binary(args.path), "This looks like a binary file - I can't process it."
    assert is_fasta(args.path), "This doesn't look like a nucleotide FASTA file :-/"
    
    freqs = count_bases(args.path, wait=args.wait)
    
    # send formatted output to file
    with open(args.out, 'w') as outfile:
        outfile.write("Base\tCount\n")
        for nuc, count in freqs.items():
            outfile.write("{}\t{}".format(nuc, count) + '\n')
```
