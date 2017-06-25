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

Here is a better implementation that accomplishes the same task:

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
Base	   Count
A	      9009
C      	11992
T      	7845
G	      10262
```
(Note that I've padded the whitespace with spaces because the GitHub interface doesn't support tabs.  Also, the order of rows in this output table can change every time you run the script because a dictionary is not an ordered collection.)

The second version is substantially longer -- in fact, there are more than **six** times as many lines of code (62 versus 10).  To some, this may seem horribly inefficient.  However, a script will rarely occupy a substantial amount of space on your hard drive.  In fact, a single Python script probably shouldn't take up much more than a thousand lines.  If you're getting way over that number, then you might want to think about splitting that script up into two or more scripts and building a module.  

Even if you just *have* to write a script that takes tens of thousands of lines of code, you're *still* not going to consume a lot of space on your hard drive.   You'd have a really hard time making the script take up much more than a megabyte of space - about a tenth the size of a typical MP3 audio file.  Why bother making your script smaller? 

I argue that the benefit you get from making your code more *readable* vastly outweighs the cost of making a longer script.  


## Documenting your code

I haven't bothered to write any comments or documentation strings.  I haven't bothered to give variables informative names (this actually made it difficult to write the code, because I kept forgetting what specific variables were supposed to represent).  I've deliberately used `lambda` functions that allow me to write more compact code that might also be less accessible to a beginning coder in Python. 



### Inline comments

### Block comments


## Writing helpful prompts with `argparse`


