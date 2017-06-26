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

* do the inputs exist?
* are the inputs what the script was expecting?


### Feedback

* Progress monitoring
* Verbosity


### Writing output

* Writing to lines to file during processing instead of at the end
* Disruption of process, loss of work
* `flush` to make clean output
* preventing overwrites (don't do unexpected things)

