# Genetic sequence data

Bioinformatics is historically closely associated with the development of genetic sequencing technology.


## Sequence data formats

### IUPAC characters

* Nucleotides are encoded with `A`, `C`, `G` and `T`
* Ambiguous base calls or nucleotide polymorphisms are encoded as follows:

| Symbol | Bases | Symbol | Bases | Symbol | Bases |
|--------|-------|--------|-------|---------|-------|
| W | A,T | B | A,C,T | N | A,C,G,T |
| R | A,G | D | A,G,T | X | A,C,G,T |
| K | G,T | H | A,C,T |
| Y | C,T | V | A,C,G |
| S | C,G |
| M | A,C |

* Gaps (indels) are usually encoded by `-` but non-standard characters `.`, `~` and `X` are also used.
* Here is a bit of Python to replace every non-standard gap charcater with a `-`.   Later on we'll learn how this can be done more efficiently with regular expressions:
  ```python
  def standardize_gaps(seq):
      """ Replace non-standard gap characters with '-' symbol """
      symbols = list(seq)
      for i, symbol in enumerate(symbols):
          if symbol in '.~X':
              symbols[i] = '-'
      return ''.join(symbols)
  ```
  
* Amino acids are encoded with A, C, D, E, *etc.*
* There are standardized charcaters for mixtures of amino acids but they are rarely used.  For example, a mixture of `D` (aspartic acid) and `N` (asparagine) is encoded by `B`
* Stop codons are encoded by `*`


### FASTA

The FASTA format is one of the most ubiquitous data formats for storing genetic sequence information.  It originates from a program that is no longer in use.  Every sequence record consists of a label (header) alnd the sequence.  A line contains a header if it starts with a `>` character.  Any subsequently lines can contain sequence associated with that record until we hit the next header.

The FASTA format is not trivial to parse because we have to accumulate information over multiple lines.  Let's learn about this format by parsing an example file that I've included in the `examples` folder of the repository.  (Tumour clonal sequences?)

Let's write a function that will take a path to a FASTA file as its only argument, and returns parsed sequence records one at a time.  This kind of function is called a *generator*.  Generators are more efficient because we aren't parsing the entire file all at once and mashing the entire contents into a single return value.

First of all, we need to declare that we're defining a new function:
```python
def parse_fasta(path):
    """
    A generator function that parses records from a FASTA file
    :param    path:  Relative or absolute path to a FASTA file.
    :returns  (header, sequence) tuples
    """

```

I've taken some time here to write some documentation for this function.  Usually when I've been inserting comments into my Python code examples, I've been using *inline comments*:
```python
 # like this
```
Inline comments are fine for brief one-line descriptions or notes about an adjacent piece of code, but they're a bit clumsy if we want our comment to span multiple lines.  For these situations, we use a *block comment*.  Python happens to allow the user to declare a string using three types of notation:
* single quotes: `'dog'`
* double quotes: `"cat"`
* triple double quotes: `"""platypus"""`
String literals that are declared but not assigned to a variable are perfectly legit code but also have no effect - thus, it's perfectly okay to intersperse your code with unassigned strings as comments.  Strings within triple double quotes are special because they can break lines.  For example:
```python
" this raises
 an error  "
""" but
this is
  totally
 OK
 """
```

Okay, we need to open the file and iterate over its lines.  This should be pretty familiar to you by now:
```python
def parse_fasta(path):
    ```leaving out block comment from now on```

    # prepare a couple of container variables
    header = ''
    sequence = ''

    handle = open(path)
    for line in handle:
        if line.startswith('>'):
            # line starts a new record
            if header:
                yield (header, sequence)
```
