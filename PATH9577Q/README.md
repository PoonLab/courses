## Learning objectives
* To acquire some basic command-line literacy:
  * understanding the limitations and advantages of command-line interfaces
  * how to navigate a file system
  * how to invoke a command
* Basic programming concepts
  * variables
  * iteration
  * conditional statements (control flow)
* Learning to read and modify the contents of a file

## Prerequisites
* students must have a laptop to work on
* your laptop must have a UNIX-like computing environment, e.g., Linux, Apple macOS.  On Windows 10, you can install a Linux subsystem by following [these instructions](https://docs.microsoft.com/en-us/windows/wsl/install-win10) -- when you have a choice of Linux distributions, I suggest using Ubuntu.
* install a plain-text editor (such as [gedit](https://wiki.gnome.org/Apps/Gedit)) or an [integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment) (IDE) for Python such as [PyCharm](https://www.jetbrains.com/pycharm/).
* (optional) install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).  This should already be installed on Linux and macOS machines.  To confirm, open a [Terminal](https://en.wikipedia.org/wiki/Terminal_emulator) window and issue the following command: `git --version`.

## Grading

* **In-class assignments (40%)**  
  Students will be guided through basic coding techniques during the class.  This instruction will be structured by an in-class assignment that students will complete while they are participating in the class.  Each assignment will consist of a small number of questions or tasks that will be demonstrated in class.  Students will be required to submit their completed assignment by e-mail to the instructor at the end of class.

* **Take-home assignments (40%)**
  
  The assignments are designed to help students review material from the associated lecture session by working through simple coding exercises.  Working in groups is encouraged.  Assignment files are distributed in Markdown format and should be edited directly in the same format and returned as e-mail attachments.  

* **Data parsing mini-project (20%)**
  
  Each student will be responsible for writing script(s) that processes a bioinformatic data file.  Students are encouraged to use data files from their own research project or lab, but this is not mandatory and will not influence the grade.  A successful mini-project will use multiple concepts from the course to parse and manipulate data from the file.  Complete mini-projects are to be submitted as one or more Python scripts.  Students should also provide an excerpt of the data file for evaluation.  If the data cannot be released because of ethical concerns or data sharing issues, then the student should provide a small mock-up data file that is sufficient to demonstrate the script.


## Syllabus

1. Linux and the command line
   * Basic UNIX commands
   * Navigating the file system
   * File permissions
   * Dealing with many files, UNIX wildcards
   * Dealing with massive files: `less`, `grep` and `gunzip`
   * **In-class assignment** Map the file system - see [basicunixcommands](Readings/basicunixcommands.md)
   * **Take-home assignment** [Building a project folder](Assignments/takehome1.md).
   * **Readings:** [basicunixcommands](Readings/basicunixcommands.md), [Markdown](Readings/Markdown.md)

2. Variables
   * Python's interactive mode
   * `help()` and getting out of the help shell
   * Numeric types: `int`, `float`
   * Basic math
   * Declaring a variable
   * Special types: `bool`, `NoneType`
   * Learning about an object with `dir()`
   * Strings
     * Indexing and slicing
   * Lists and tuples
     * Mutable versus immutable types
     * Sorting
   * Sets
     * set operations
   * Dictionaries
   * Casting between types
   * **In-class assignment** Built-in types worksheet
   * **Take-home assignment** String and list operations
   * **Readings:** [Variables](Readings/Variables.md), [Strings](Readings/Strings.md), [Iterables](Readings/Iterables.md), [Dictionaries](Readings/Dictionaries.md)

3. Control flow
   * Code blocks with indents in Python
   * Running Python script mode
   * `print` statements
   * `if`, `elif`, `else` statements
   * Logical operations
   * `for` and `while` loops
   * iterable types: `range`, `map`, `filter`
   * Combining conditional and loop statements: `break` and `continue`
   * Defining functions
   * **In-class assignment** Drawing a flowchart
   * **Take-home assignment** [Your first script](Assignments/takehome3.md)
   * **Readings:** [Control flow](Readings/ControlFlow.md)

4. Parsing data
   * File encodings: ASCII, Unicode
   * Opening files, `File` types
   * Parsing tabular data
   * **In-class assignment** [Splitting a column](Assignments/inclass4.md)
   * **Take-home assignment** [Row-column index script](Assignments/takehome4.md)
   * **Readings:** [Tabular data](Readings/TabularData.md)

5. Review session
   * Going over the material we have covered so far
   * Discuss final projects
   * **In-class assignment** [Single-cell expresssion data](Assignments/inclass5.md)
   * **Take-home assignment** [Unwinding a dense CSV matrix](Assignments/takehome5.md)
  
6. Writing and debugging scripts
   * What is coding style?
   * Concise code:
     * List comprehensions
     * `lambda` functions and `map`, `filter` and `reduce`
     * 
   * Good coding practices
   * Documenting your code
   * Debugging
     * `print` statements
     * `assert` statements
     * Catching and handling exceptions with `try` and `except`
   * **In-class assignment** [Debugging scripts](Assignments/inclass6.md)
   * **Take-home assignment** [Refactoring a bad script](Assignments/takehome6.md)
   * **Readings:** [Writing "good" code](Readings/GoodCode.md)

7. Advanced text processing
   * Regular expressions with `re`
   * Old-style string formatting (C-style placeholders)
   * `format`
   * **In-class assignment** [Sequence motifs](Assignments/inclass7.md)
   * **Take-home assignment** [Nuclear localization signals](Assignments/takehome7.md)
   * **Readings:** [Regular expressions](Readings/RegularExpressions.md), [String formatting](Readings/FormattedStrings.md)

8. Modules
   * Date and time data with `datetime`
   * Genetic sequences with `Bio`
     * Working with RNASeq data (FASTQ)
   * **In-class assignment** [Zika virus](Assignments/inclass8.md)
   * **Take-home assignment** [Lung microbiome](Assignments/takehome8.md)
   * **Readings:** [Date-time objects](Readings/DateTime.md), [Sequence Data](Readings/SequenceData.md)

9. Batch processing
   * UNIX wildcards and `glob`
   * Pipelining
   * Calling other programs with `subprocess`
   * **Readings:** [Pipelining](Readings/Pipelining.md)

