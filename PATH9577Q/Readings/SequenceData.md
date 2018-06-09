# Genetic sequence data

Bioinformatics is historically closely associated with the development of genetic sequencing technology.  Genetic sequences like nucleotides and proteins are structured data because the position of a residue is meaningful.  We can't reduce a nucleotide sequence down to the numbers of A's and retain the same amount of information.  Because these are structured data, it is usually not meaningful to represent sequences as tabular data.  It's possible, but then there's the temptation to rearrange columns.  If we restrict our representation of genetic sequences to single characters, then we don't need to worry about delimiters and can use more compact data formats.  We'll start with how nucleotides and amino acids are mapped to single characters before we talk about how this information is structured into some common sequence data formats.

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

> **Question:**  We can also edit out non-standard gap characters with `string.replace()` function calls.  Can you write a Python function to do this?

* Amino acids are encoded with A, C, D, E, *etc.*
* There are standardized charcaters for mixtures of amino acids but they are rarely used.  For example, a mixture of `D` (aspartic acid) and `N` (asparagine) is encoded by `B`
* Stop codons are encoded by `*` but `X` is sometimes used for this same purpose.  Unfortunately, `X` is also sometimes used to indicate that the amino acid encoded by the codon is ambiguous because of a nucleotide mixture.  For example, `ARA` could encode lysine (`AAA` to `K`) or arginine (`AGA` to `R`).  A question mark `?' is another symbol for an ambiguous amino acid that has less potential for confusion.

![](https://imgs.xkcd.com/comics/proteins.png)


### FASTA

The FASTA format is one of the most ubiquitous data formats for storing genetic sequence information.  It originates from a program that is no longer in use.  Every sequence record consists of a label (header) alnd the sequence.  A line contains a header if it starts with a `>` character.  Any subsequently lines can contain sequence associated with that record until we hit the next header.

The FASTA format is not trivial to parse because we have to accumulate information over multiple lines.  Let's learn about this format by parsing an example file that I've included in the `examples` folder of the repository called `Decapod.PEPCK.fa`.
```shell
art@Misato:~/git/courses/GradPythonCourse/examples$ head -n3 Decapod-PEPCK.fa
>EU427182.1 Albunea holthuisi phosphoenolpyruvate carboxykinase (PEPCK) gene, partial cds
GGCGTCCTGCGAGCCATCAACCCCGAGAACGGCTTCTTCGGCGTGGCGCCCGGCACCTCCATGAAGACCA
ACCCTGTGGCCATGACCACTGTGCTGACCAACACCGTCTTCACTAACGTGGCCAAGACCAGCGACGGCGG
```

For what it's worth, this is a decapod:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Ocypode_quadrata.jpg/320px-Ocypode_quadrata.jpg)

and [PEPCK](https://en.wikipedia.org/wiki/Phosphoenolpyruvate_carboxykinase) is an enzyme in the glucose-generating metaboilc pathway.

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
    """ leaving out block comment from now on """

    # prepare a couple of container variables
    header = ''
    sequence = ''

    handle = open(path)
    for line in handle:
        if line.startswith('>'):
            # line starts a new record
            if header:
                # output the current record if it exists
                yield (header, sequence)
            # start next record
            header = line.strip('>\n')
            sequence = ''
        else:
            # extend record with this line as sequence
            sequence += line.strip('\n')
```

The `yield` command causes the function to return some values, but instead of exiting our function persists and readies the next set of values to return.  By returning one record at a time, we avoid loading the entire set of records from the FASTA file into memory - this can help when we're dealing with a large file.

> **Question** This code doesn't work properly.  Why?  Try it out on the example file `Decapod-PEPCK.fa` to see.

```python
for h, s in parse_fasta('Decapod-PEPCK.fa`):
    print(h)
```

> How can we fix this problem?


### FASTQ

FASTQ is a popular format for short read sequence data.  It is similar to the FASTA format, but also contains base quality information.  First, let's have a look at a FASTQ file.  Here is the first record of the NCBI Short Read Archive (SRA) entry SRR5261740:
```
@SRR5261740.1 1 length=295
AAGCAGTGGTATCAACGCAGAGTACATGGGGACAGTGACCCTGATCTGGTAAAGCTCCCATCCTGCCCTGACCCTGCCATGGGCACCAGCCTCCTCTGCTGGATGGCCCTGTGTCTCCTGGGGGCAGATCACGCAGATACTGGAGTCTCCCGGGGAACACGTTGTTCAGGTCCTCCAAGACAGAGAGCTGGGTTCCACTGCCAAAAAACAGTTTTTCAGGAGCGACTGTGGTGCTGGCACAGAGATACATGGCCGAGTCCCCCTGCTCTGTGCGCTGGATCTCCAAGGTGGAGAA
+SRR5261740.1 1 length=295
BBBBBFFFBFFFGGGGGGGGGGHHHHHHHHGGGGGHHHHGHHHGHHHHHHHHGHHHHHGHHHHHHHHHHHHHHHHHHHHHHHHHHGGHHHGHHHHHHHHHHHHHHGGHHHHHHHHHHHHHHGGGGGGGHHHHGHGGGHHHHHHHHHHHHHHABBBBBBGGGGGGGGGGHHHFHHHHHHHHHHHHHHGGHHHGHGHHHHHHHHHHHHHFGHHHHHHGHGHHHGGGGGGGHHHHGHHHGGHHHHFHHHHHHHHHHHGGGGHHHHGGEHHHHHHHHGGGGGHHHHHHHGHGHHGHHHG
```
I've uploaded a truncated version of this file to the repository at `examples/SRR5261740.trunc.fastq`.  The original data came from an RNA-Seq experiment in [a study of human hematopoietic stem cells](https://www.ncbi.nlm.nih.gov/pubmed/28369043).

Each record comprises four lines:
1. A header line that contains some information that is unique to the read:
   ```
   @SRR5261740.1 1 length=295
   ```
   For example, some platforms will report the x- and y-coordinates of the sequencing-by-synthesis cluster associated with the read on this line.  This line is identified by a `@` character instead of `>`.
2. The nucleotide sequence:
   ```
   AAGCAGTGGTATCAACGCAGAGTACATGGGGACAGTGACCCTGATCTGGTAAAGCTCCCATCCTGCCCTGACCCTGCCATGGGCACCAGCCTCCTCTGCTGGATGGCCCTGTGTCTCCTGGGGGCAGATCACGCAGATACTGGAGTCTCCCGGGGAACACGTTGTTCAGGTCCTCCAAGACAGAGAGCTGGGTTCCACTGCCAAAAAACAGTTTTTCAGGAGCGACTGTGGTGCTGGCACAGAGATACATGGCCGAGTCCCCCTGCTCTGTGCGCTGGATCTCCAAGGTGGAGAA
   ```
   This sequence should not span multiple lines.
3. A plus symbol:
   ```
   +SRR5261740.1 1 length=295
   ```
   In this particular example, the header has been duplicated on this third line.  However, I usually see this line containng only the `+` symbol with no additional information.
4. Lastly, a sequence of base quality scores that are encoded with symbols:
   ```
   BBBBBFFFBFFFGGGGGGGGGGHHHHHHHHGGGGGHHHHGHHHGHHHHHHHHGHHHHHGHHHHHHHHHHHHHHHHHHHHHHHHHHGGHHHGHHHHHHHHHHHHHHGGHHHHHHHHHHHHHHGGGGGGGHHHHGHGGGHHHHHHHHHHHHHHABBBBBBGGGGGGGGGGHHHFHHHHHHHHHHHHHHGGHHHGHGHHHHHHHHHHHHHFGHHHHHHGHGHHHGGGGGGGHHHHGHHHGGHHHHFHHHHHHHHHHHGGGGHHHHGGEHHHHHHHHGGGGGHHHHHHHGHGHHGHHHG
   ```

### Quality scores
What do all these `B`s and `F`s mean?  They are encodings of base quality scores.  A quality score is an estimate of the probability that the base call is incorrect.  The standard representation of this probability is based on a base calling program called [Phred](), which took the log10 transformation of this probability and then multiplied by -10.  For example, if the probability that the base is incorrect is estimated to be 0.001, then the quality score is 30.  Furthermore, quality scores are almost always rounded to the nearest integer value.

This still doesn't answer our question, though.  Suppose that we have a vector of quality scores:
```
16,30,25,40,40,...
```
We could simply put this sequence of integers into our record.  However, there are a couple of issues with this.  First, this sequence of quality scores is longer than the nucleotide sequence, so we can't look between these lines of the record and know which score is associated with which base.  Second, we can represent this same information more compactly.  For example, there are up to three characters being used for every quality score in the above example, partly because we need to have some sort of delimiter to separate different scores.

We can make this line more compact by replacing every integer value with a unique one-letter symbol.  For example, we could replace every `10` with `A`.  Instead of coming up with some arbitrary map from quality scores to symbols, FASTQ makes use of the ASCII encoding.  Here is a useful text-diagram that I've copied from the [Wikipedia entry on FASTQ](https://en.wikipedia.org/wiki/FASTQ_format), which nicely visualizes this mapping:
```
  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
  |                         |    |        |                              |                     |
 33                        59   64       73                            104                   126
  0........................26...31.......40                                 Sanger
                           -5....0........9.............................40  Solexa
                                 0........9.............................40  Illumina 1.3+
                                    3.....9.............................40  Illumina 1.5+
  0.2......................26...31........41                                Illumina 1.8+
```

So to answer our own question, `B` means a quality score of 33 and `F` a score of 37.
We can use some base functions in Python to do this conversion as follows:
```python
>>> ord('B')-33
33
>>> ord('F')-33
37
```
So we can write a function that will take a line encoding quality scores in a FASTQ file into a vector of integer values:
```python
def convert_quality(line):
    line = line.strip('\n')  # just in case we forgot
    result = []  # prepare a container
    for letter in line:
        score = ord(letter)-33
        if score < 0 or score > 41:
            print ("ERROR: Unexpected integer value in convert_quality(): ", score)
            return None
        result.append(score)
    return(result)
```
We could also do this conversion in a single line of code:
```python
scores = [ord(c)-33 for c in line.strip('\n')]
```
or even:
```python
scores = map(lambda c: ord(c)-33, line.strip('\n'))
```
but these versions are slightly more difficult to read and to implement checks like I did in the first version.

Parsing a FASTQ file is a little more involved than a FASTA file because we have four lines per record instead of two, three lines with real information.  It helps that we've written a function that will handle parsing the quality score line, and it also helps that sequences aren't supposed to span multiple lines.  Let's write a simple parser that relies on the assumption that there are four lines per record:
```python
def parse_fastq(path):
    """
    Parse a FASTQ file.  We assume the file contains unpaired reads.
    Generates tuples of (header, sequence, quality scores) from an open file.
    :param path: Absolute or relative path to a FASTQ file.
    """
    # prepare containers
    header = None  # an empty value
    sequence = ''
    quality = []

    handle = open(path, 'rU')
    for ln, line in enumerate(handle):
        position = ln % 4
        if position == 0 and line.startswith('@'):
            # header, start of next record
            if header:
                yield (header, sequence, quality)
            header = line.strip('@\n')
        elif position == 1:
            sequence = line.strip('\n')
        elif position == 2 and line.startswith('+'):
            continue  # do nothing
        elif position == 3:
            quality = convert_quality(line)
        else:
            print ('ERROR: Failed to parse FASTQ at line:\n', line)

    # return last record
    yield (header, sequence, quality)
```

In class I'll show you how to write these functions into a text file and call them in non-interactive mode.


### SAM format
The SAM (sequence alignment/map) format has become a standard format for recording output from programs that align short read data against one or more reference genome sequences.  Even NCBI BLAST results can be downloaded in SAM format!  It is a tabular data format with tab-separated values and comments prefixed with `@` characters.  Since we've covered parsing tabular data sets, the SAM format makes a nice opportunity to review what we've learned.

I've taken the truncated FASTQ file from the previous section and mapped those short reads to chromosome 7 of a standard human genome assembly, and saved the result to `examples/SRR5261740.trunc.sam`.  Here are the first few lines:
```
@HD	VN:1.0	SO:unsorted
@SQ	SN:chr7	LN:159138663
@PG	ID:bowtie2	PN:bowtie2	VN:2.2.8	CL:"/usr/local/bin/bowtie2-align-s --wrapper basic-0 -x chr7 -S SRR5261740.trunc.sam --local -U SRR5261740.trunc.fastq"
SRR5261740.1	16	chr7	142247517	2	168S96M31S	*	00	TTCTCCACCTTGGAGATCCAGCGCACAGAGCAGGGGGACTCGGCCATGTATCTCTGTGCCAGCACCACAGTCGCTCCTGAAAAACTGTTTTTTGGCAGTGGAACCCAGCTCTCTGTCTTGGAGGACCTGAACAACGTGTTCCCCGGGAGACTCCAGTATCTGCGTGATCTGCCCCCAGGAGACACAGGGCCATCCAGCAGAGGAGGCTGGTGCCCATGGCAGGGTCAGGGCAGGATGGGAGCTTTACCAGATCAGGGTCACTGTCCCCATGTACTCTGCGTTGATACCACTGCTT	GHHHGHHGHGHHHHHHHGGGGGHHHHHHHHEGGHHHHGGGGHHHHHHHHHHHFHHHHGGHHHGHHHHGGGGGGGHHHGHGHHHHHHGFHHHHHHHHHHHHHGHGHHHGGHHHHHHHHHHHHHHFHHHGGGGGGGGGGBBBBBBAHHHHHHHHHHHHHHGGGHGHHHHGGGGGGGHHHHHHHHHHHHHHGGHHHHHHHHHHHHHHGHHHGGHHHHHHHHHHHHHHHHHHHHHHHHHHGHHHHHGHHHHHHHHGHHHGHHHHGGGGGHHHHHHHHGGGGGGGGGGFFFBFFFBBBBB	AS:i:143	XS:i:136	XN:i:0	XM:i:7	XO:i:0	XG:i:0	NM:i:7	MD:Z:13G8T0G0C12C12A3A41	YT:Z:UU
```
How many comment lines are there?  One of the comment lines contains information about the reference sequences.  In this example, we've only used one reference sequence `chr7`, which is about 159 Mbp long.  

Each line in a SAM corresponds to a read and contains the following information:

| # | Name  | Description          | #  | Name  | Description          |
|---|-------|----------------------|----|-------|----------------------|
| 1 | QNAME | Read label           | 7  | RNEXT | Ref. seq. of mate    |
| 2 | FLAG  | Bitwise flags        | 8  | PNEXT | Map location of 1st  |
| 3 | RNAME | Reference seq.       |    |       | base in mate         |
| 4 | POS   | Map location of 1st  | 9  | TLEN  | Insertion length     |
|   |       | base in read         | 10 | SEQ   | Read sequence        |
| 5 | MAPQ  | Mapping quality      | 11 | QUAL  | Read quality string  |
| 6 | CIGAR | Compact idiosyncratic    |    |       |                      |
|   |       | gapped alignment report |  |  |  |

Note that there can be additional fields in a SAM file, but I usually only use the first 11.


> **Question:** Where did the first read map in chromosome 7?


### BAM files

A BAM file is simply a binary compressed SAM file.  One way to convert from BAM to SAM and back is to use *samtools*, a collection of programs for working with SAM-type data that can be obtained [here](https://github.com/samtools/samtools/releases).


### Reconstituting FASTQ from SAM
Let's practice working with formatted strings by writing a script that will parse the information in a SAM file and write the header, sequence and quality scores in a new FASTQ file.  We've already written a FASTQ parser in Python in a previous section.  I've provided a small SAM file (`zika.sam`) in the `examples` folder.  First, we need to open this file and parse it as a tabular data set:
```python
handle = open('zika.sam', 'rU')
for line in handle:
    if line.startswith('@'):
        # skip comment
        continue
    items = line.strip('\n').split('\t')
    qname = items[0]
    seq = items[9]
    qual = items[10]

    print("@{} {} {}".format(qname, seq[:10], qual[:10]))

handle.close()  # clean up
```

This is an intermediate script with a `print` function that will help us check that we are getting the correct information from the file.  Run it to make sure that the output makes sense.

Next, we need to modify our script to write to an output file.  This time I'm going to use direct indexing to compose the formatted string from a list argument.
```python
handle = open('zika.sam', 'rU')
outfile = open('zika.fastq', 'w')  # CAREFUL: write mode erases the file!
for line in handle:
    if line.startswith('@'):
        continue
    items = line.strip('\n').split('\t')

    # compose formatted string from list
    output = "@{0}\n{9}\n+\n{10}\n".format(items)
    outfile.write(output)

# clean up
outfile.close()
handle.close()
```

## Additional exercise
Try writing a script that converts the `zika.fastq` file back to a FASTA file.
