## Prerequisites
* students must have a laptop to work on
* your laptop must have a UNIX-like computing environment, e.g., Linux, Apple OS-X
* install [PyCharm](https://www.jetbrains.com/pycharm/)
* install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).  This should already be installed on Linux and OS-X machines.  To confirm, open a [Terminal](https://en.wikipedia.org/wiki/Terminal_emulator) window and issue the following command: `git --version`.

## Grading

| Percent | Assessment |
|---------|------------|
| 10% | Participation (including computing skills survey) |
| 30% | Assignments (8) |
| 10% | Project proposal |
| 50% | Coding project |


## Syllabus

1. [In the beginning was the command line](http://cristal.inria.fr/~weis/info/commandline.html)
   * Computing skills survey 
   * What is bioinformatics?  The biology-statistics-computer science triangle
   * [UNIX-like systems](https://en.wikipedia.org/wiki/Unix-like)
   * [Working on the command-line](basicunixcommands.md)
   * Running a Python script
   * In-class assignment: UNIX games - download `src/learn-cli.py`
   * Markdown
   * Assignment: Project proposal in [Markdown](http://daringfireball.net/projects/markdown/basics) (deadline May 16)


2. Scripting languages.  Tabular data I.
   * [Levels of programming languages](https://en.wikipedia.org/wiki/Low-level_programming_language)
   * Scripting languages and their philosophies
   * The Python interpreter - interactive mode
   * tabular data (CSV, TSV)
   * File I/O in Python
   * for-loops
   * indexing and slicing
   * basic string operations:
     * `print` (built-in function)
     * `startswith`, `endswith`
     * `in`, `find`
     * `count`
     * `strip`, `lstrip`, `rstrip`
     * `split`
   * assignment: parsing a tabular data set

3. Tabular data II.  
   * more examples of tabular data
     * [SAM](https://samtools.github.io/hts-specs/)
     * [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/)
     * [COSMIC](http://cancer.sanger.ac.uk/cosmic)
   * iterable objects (strings, lists, tuples, file handles)
   * control flow (if-else, break, continue)
   * composing and debugging a script


4. Genetic sequences.
   * Sequence data formats
     * FASTA
     * FASTQ
     * [SAM, BAM, VCF](https://samtools.github.io/hts-specs/)
     * Genbank, BLAST
   * Biopython
   * Formatted strings
   * Gathering information with dictionaries

5. More complex text processing
   * Python modules
   * Regular expressions with `re`
   * Date fields with `datetime`

6. Numbers
   * arithmetic operators
   * the `math` module
   * the `random` module
   * basic statistics: mean, median, quantiles

7. Batch processing
   * Calling one script on many files with `bash`
   * Calling many scripts - pipelining
   * Calling other programs - subprocessing
   * Harnessing multiple cores with MPI

8. Final project help session

9. Maintainability
   * Version control with git
   * Documentating your code
   * the `argparse` module

