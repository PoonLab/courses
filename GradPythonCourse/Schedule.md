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
     * SAM/BAM
     * Genbank
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
   * Calling one script on many files
   * Calling many scripts - pipelining
   * Calling other programs - subprocessing
   * Harnessing multiple cores with MPI

8. Final project help session

9. Maintainability
   * Version control with git
   * Documentating your code
   * the `argparse` module





  * [GenBank](https://www.ncbi.nlm.nih.gov/genbank/)
  * [FASTQ](https://en.wikipedia.org/wiki/FASTQ_format)
  * [SAM, BAM, VCF](https://samtools.github.io/hts-specs/)
  * [BioPython](https://github.com/biopython/biopython)
  
  
## May 16, 2017 - Control flow and output
* What is an iterable object in Python?
* Indexing and slicing
* Loops again (for, while)
* Conditionals (if-else statements)
* Parsing tabular data
* File output
* [Formatted strings](https://en.wikipedia.org/wiki/Printf_format_string)
* Assignment: Parsing a file 
* Deadline: Project proposal in Markdown


## May 23, 2017 - ** NO CLASS **


## May 30, 2017 - [Regular expressions](https://en.wikipedia.org/wiki/Regular_expression)
* Regular languages
* Special characters
* Group capture
* Substitutions
* Start project pending review of proposal (deadline June 27)


## June 1, 2017 - Numbers and math
* Integer arithmetic
* Floats
* The `math` library
* The `random` library
* Building strings (concatenation)
* Dictionaries
* Assignment: Filtering a file by entries


## June 6, 2017 - Debugging
* Exception handling
* Debugging strategies
* Testing your code


## June 13, 2017 - Workflow integration
* bash scripting
* pipes
* Python [subprocess](https://docs.python.org/3/library/subprocess.html) module
* stream redirection


## June 20, 2017 - Code maintenance
* [PEP8](https://www.python.org/dev/peps/pep-0008/)
* documentation
* version control
* [learning Git](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
* Collaborative coding exercise
* Assignment: Python script archeology


## June 27, 2017 - Packaging your code
* sys - reading arguments from the command line
* argparse
* refactoring
* unit testing
* releasing your code - GitHub, open source licenses
* survey
