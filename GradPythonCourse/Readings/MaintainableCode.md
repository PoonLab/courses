# Writing maintainable code

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

This script works, but it's difficult to read.  I consider this to be an unmaintanable implementation.  When I run it on a file, I get the following output
```shell
[Elzar:courses/GradPythonCourse/examples] artpoon% python badcode.py Decapod-PEPCK.fa 
{'G': 10262, 'C': 11992, 'A': 9009, 'T': 7845}
```

![](https://imgs.xkcd.com/comics/code_quality_3.png)

Here is a rather different implementation that accomplishes exactly the same task:

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
[Elzar:courses/GradPythonCourse/examples] artpoon% python good.py Decapod-PEPCK.fa
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

Internal documentation is contained within the source code files themselves.  Since we're focusing on learning how to write data processing and pipelining scripts in Python, we'll focus on internal documentation.  Because internal documentation means writing information right into the source code, we're making use of comments: a comment is a chunk of text that we tell the Python interpreter to ignore by using one or more special characters.  There are generally two types of comments in Python: inline and **block** comments.

An **inline** comment is just that - it occupies a single line of source code.  It should either occupy the line by itself, or it can come *after* (to the right of) a piece of source code, but in Python it never appears to the left of some code.  An inline comment in Python is generally declared with the `#` special character:
```python
a = 1  # this is an inline comment in Python
```


## Writing helpful prompts with `argparse`


