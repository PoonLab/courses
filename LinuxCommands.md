# Linux Commands:
## man
* man is the interface used to view the system's reference manuals.
* Syntax: ```man [command name]```
* Example: ```man mv```
## pwd
* Print the name of the working directory.
* Syntax: ```pwd```
* Example: ```pwd```
## ls
* Lists the contents of a directory.
* Syntax: ```ls [OPTION]... [FILE]...```
* Option ```-a``` can be used to view hidden files.
* Example: ```ls -a```
## cd
* Changes directory.
* Syntax: ```cd [DIRECTORY NAME]```
* Example: ```cd Desktop```
## history
* Prints the history of the commands used.
* Syntax: ```history```
* Example: ```history```
## ..
* Parent directory.
## .
* Current directory.
## wc
* wc, or "word count," prints a count of newlines, words, and bytes for each input file.
* Syntax: ```wc [OPTION]... [FILE]...```
* Option ```-l``` can be used to view line count.
* Example: ```wc example.txt```
## cat
* cat stands for "catenate." It reads data from files, and outputs their contents. 
  It is the simplest way to display the contents of a file at the command line.
* Syntax: ```cat [FILE NAME]```
* Example: ```cat example.txt```
## head
* head makes it easy to output the first part of files.
* Syntax: ```head [OPTION]... [FILE]...```
* Option ```-n#```, where # is an integer, can be used to view a specific number of lines.
* Example: ```head example.txt```
## tail
* tail makes it easy to output the last part of files.
* Syntax: ```tail [OPTION]... [FILE]...```
* Option ```-n#```, where # is an integer can be used to view a specific number of lines.
* Example: ```tail example.txt```
## grep 
* grep, which stands for "global regular expression print," 
  processes text line by line and prints any lines which match a specified pattern.
* Syntax: ```grep [OPTIONS] PATTERN [FILE...]```
* Example: ```grep examplePattern example.txt```
## touch
* If you specify a FILE that does not already exist, touch creates an empty file with that name.
* Syntax: ```touch [OPTION]... [FILE]...```
* Example: ```touch example.txt```
## cp
* The cp command is used to make copies of files and directories.
* Syntax: ```cp [OPTION]... [SOURCE]... [DIRECTORY]...```
* Option ```-r``` can be used to copy directories.
* Example: ```cp example.txt ~/Desktop```
## mv
* The mv command is used move files and directories.
* Syntax: ```mv [OPTION]... [SOURCE]... [DIRECTORY]...```
* Option ```-r``` can be used to move directories.
* Example: ```mv example.txt ~/Desktop```
## rm
* The rm command is used to delete files and directories.
* Syntax: ```rm [OPTION]... [SOURCE]... [DIRECTORY]...```
* Option ```-r``` can be used to delete directories.
* Example: ```rm example.txt```
## mkdir
* Short for "make directory", mkdir is used to create directories on a file system.
* Syntax: ```mkdir [OPTION]... [DIRECTORY]...```
* Example: ```mkdir exampleDirectory```
## rmdir
* Short for "remove directory", rmdir is used to remove directories from a file system.
* Syntax: ```rmdir [OPTION]... [DIRECTORY]...```
* Example: ```rmdir exampleDirectory```
