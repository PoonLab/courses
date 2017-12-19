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
* Understanding the differences between "good" code and "bad" code

## Prerequisites
* students must have a laptop to work on
* your laptop must have a UNIX-like computing environment, e.g., Linux, Apple OS-X.  If you are unable to install a UNIX-like environment, then you need to install [PuTTY](http://www.putty.org/) and arrange for a temporary user account on one of my Linux workstations.  See [instructions](RemoteComputing.md).
* install [PyCharm](https://www.jetbrains.com/pycharm/) or a similar IDE (integrated development environment) or plain-text editor (such as [gedit](https://wiki.gnome.org/Apps/Gedit)).
* install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).  This should already be installed on Linux and OS-X machines.  To confirm, open a [Terminal](https://en.wikipedia.org/wiki/Terminal_emulator) window and issue the following command: `git --version`.

## Grading

* **In-class quizzes (20%)**  
  Most classes will begin with a short (5-10 minute) quiz covering basic concepts from the preceding class.  Quizes will be self-graded by students immediately afterwards.  The purpose of these quizes is to help students identify and ask questions about concepts that they had trouble with.  Next, students will have the opportunity to revise their quiz answers before handing them in for grading.

* **Take-home assignments (40%)**
  
  The assignments are designed to help students review material from the associated lecture session by working through simple coding exercises.  Working in groups is encouraged.  Assignment files are distributed in Markdown format and should be edited directly in the same format and returned as e-mail attachments.  

* **Data parsing mini-project (40%)**
  
  Each student will be responsible for writing a script that processes a bioinformatic data file.  Students are encouraged to use data files from their own research project or lab, but this is not mandatory and will not influence the grade.  A successful mini-project will use multiple concepts from the course to parse and manipulate data from the file.  Complete mini-projects are to be submitted as one or more Python scripts.  Students should also provide an excerpt of the data file for evaluation.  If the data cannot be released because of ethical concerns or data sharing issues, then the student should provide a small mock-up data file that is sufficient to demonstrate the script.


## Syllabus

1. [In the beginning was the command line](http://cristal.inria.fr/~weis/info/commandline.html)
   * [UNIX-like systems](https://en.wikipedia.org/wiki/Unix-like)
   * [Working on the command-line](basicunixcommands.md)
   * Text editors
   * Markdown format
   * In-class assignment: UNIX games - download `src/learn-cli.py`
   * **Readings:** [basicunixcommands](Readings/basicunixcommands.md)

2. Working with Python
   * What is a scripting language?
   * Interactive mode
   * Working with shells
   * The built-in help system
   * Running scripts
   * Modules
   * Installing modules
   * **Readings:** [Scripting languages](Readings/ScriptingLanguages.md)
   
3. Variables
   * Variable assignment
   * Naming conventions
   * Numbers (integers, floats)
   * Lists
   * Dictionaries

4. Strings
   * `for`
   * What are the iterable types?
   * Indexing and slicing
   * Working with strings

5. Reading and parsing text data
   * File encodings: ASCII, Unicode
   * Opening files
   * **Readings:** [Tabular data](Readings/TabularData.md)
   * **Assignment:** [Parsing a tabular data set](Assignments/Assignment2.md)

6. Tabular data
   * Examples of tabular data in bioinformatics
   * control flow (`if`-`else`, `break`, `continue`)
   * composing and debugging a script
   * **Readings:** [TabularData II](Readings/TabularData2.md)

7. Genetic sequences.
   * Gathering information with dictionaries
   * Common sequence data formats
     * FASTA
     * FASTQ
     * [SAM, BAM](https://samtools.github.io/hts-specs/)
   * Formatted strings
   * **Assignment:** [Extracting quality score summaries](Assignments/Assignment3.md)
   * **Readings:** [SequenceData](Readings/SequenceData.md) and [Dictionaries](Readings/Dictionaries.md)

8. Regular expressions
   * Regular expressions with `re`
   * **Readings:** [Regular expressions](Readings/RegularExpressions.md)

9. Good code and bad code

