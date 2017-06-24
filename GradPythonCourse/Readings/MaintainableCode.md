# Writing maintainable code

## What is maintainable code?

Maintainable code can be read by another person, who will be able to:
1. use your code with confidence that it is doing what they expect it to;
2. not have to spend days picking apart the code to understand it;
3. understand it well enough to modify it without breaking something.

Code maintainability is subjective, but like 

Even if you don't intend for anyone else to use your code, you will always be writing it for someone else: *you*.  Months from now when you return to your code, if your code hasn't been written to be maintainable then you will have created a "black box" for yourself.  So do yourself a big favour and write clean, readable code with sufficient commenting and documentations, or you'll be creating more work for your future self.

![](https://imgs.xkcd.com/comics/future_self.png)


## Style

Talking about "style" in relation to coding may seem frivolous, but it is actually an important part of writing maintainable code.  For example, here is a Python that will calculate and output nucleotide frequencies from a FASTA file:

```python
import sys
a = 'ACGT'
z = open(sys.argv[1],'rU')
b=dict(map(lambda x: (x,0), a))
for x in z:
 if x[0]=='>': continue
 jj = filter(lambda xx: xx in a, x)
 for j in jj: b[j]+=1
print(b)
```

This script works, but I don't 


## Documenting your code


### Inline comments

### Block comments


## Writing helpful prompts with `argparse`


