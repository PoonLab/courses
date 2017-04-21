# A brief introduction to *nix

## What is *nix?
* This is as common way of referring to Unix-like operating systems
* Unix was developed at [Bell Laboratories](https://en.wikipedia.org/wiki/Bell_Labs) starting 1969
* Due to antitrust ruling in 1956, AT&T could not sell it for a profit, making it affordable for universities
* Many students learned by modifying and enhancing UNIX
* A core tenet - the output of any command could be the input for another
* In 1980, [ARPA](https://en.wikipedia.org/wiki/DARPA) issued a recommendation in favour of Berkeley UNIX
[Source: A History of Modern Computing, 2nd ed. Paul E.  Ceruzzi.  MIT Press, Cambridge.]

## UNIX-like OSs today
* [Linux](https://en.wikipedia.org/wiki/Linux) was developed to be a free UNIX-like kernel
* It became a complete operating system by incorporating free software from the [GNU Project](https://en.wikipedia.org/wiki/GNU_Project)
* Linux has since evolved into [thousands of derived versions](https://en.wikipedia.org/wiki/Linux_distribution#/media/File:Linux_Distribution_Timeline.svg)
* The [Android OS](https://en.wikipedia.org/wiki/Android_(operating_system)) is based on the Linux kernel.
* [Mac OS-X](https://en.wikipedia.org/wiki/MacOS) is also a Unix-like operating system, but it was built on the Berkeley Software Distribution (BSD) kernel, and includes proprietary and closed-source software.

## The command line
A shell is a program that interprets commands, enabling the user to interface with files, other programs that comprise the operating system, and applications.  Starting the shell will give you something that looks like this:
```shell
art@Misato:~$
```
This is a prompt.  It's the program's way of telling me to type something.  It's also telling me a few other things:
1. I am current interfacing with the OS with the user account `art`.  
2. The computer has the hostname `Misato`
3. My current location is `~`, which is shorthand for my home directory `/home/art`.  (More on this later.)

I can type anything I want into this prompt:
```shell
art@Misato:~$ eat kleenex
No command 'eat' found, but there are 16 similar ones
eat: command not found
```

Clearly, my OS is not impressed (your output will vary with OS's).  It doesn't recognize my random words as a valid command.  A command has to start by invoking a program.  (Invoke is a [D'n'D](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons) way of saying that we type the name of a program.)  

Let's start by entering a valid command by invoking a program that actually exists.
```shell
art@Misato:~$ ls
Desktop    examples.desktop                 Music     Public  Templates  work
Documents  git                              papers    R       Videos
Downloads  java_error_in_PYCHARM_14175.log  Pictures  src     wip
```



# Directories
## Finding where files are kept
* The file system is arranged in a hierachial structure
* / is the **root** directory
* /bin is a subdirectory of the root directory that contains programs that are necessary for the most basic functions of the system (ie. starting and repairing the system)
* /usr is also a subdirectory of the root directory that can be broken down into two sub categories
  * /usr/bin are programs run by users and are necessary for the functions of the system
  * `/usr/local/bin` are where installed programs by the user are stored

# Basic Commands
* **ls**
 * Lists files in your current working directory
 * Exception: Unless you are very familiary with Unix, some files should not be changed and are kept hidden
 * These files begin with a period (.)
 * To find all files, use the **ls -a** command: for example,
 ```
 # ls -a
 .
 ..
 .hidden_file
 something_else.txt
 ```
* **mkdir**
 * Allows you to make a subdirectory in your home directory
 * Example: % mkdir PoonLab
* **cd**
 * Allows you to change directory from the current working directory
 * Example: % cd PoonLab

* **(.)**
 * The current directory
 * Example: % cd .
* **(..)**
 * Considering the hierachal structure of the files, the parent directory command will bring you directly up the hierarchy
* **pwd**
 * Present working directory
 * Will give the full pathname of the current directory that you are in

* **cp**
 * Allows you to copy files
 * Example: cp file file1 allows you to copy file in your current working directory and name it file1
* **mv**
 * Allows you to move files
 * Example: mv file file1 allows you to move file to file1
* **rm** and **rmdir**
 * Allows you to remove a file (rm) or remove a directory (rmdir)

# Access Rights to Directories and Files
* Each file has access rights associated with it
* These right can be found using the **ls -l** command, which essentially gives you the "long" listing of the file name
* Example: 
  ```
  -rwxrw-r-- 1 echadwi 562 Dec 2nd 2016 PoonLab
  ```
 * The 9 letter symbol at the beginning gives the access rights
* Access rights on files
 * **r**
  * Read permission
 * **w**
  * write permission
 * **x**
  * execution permission
* Access rights on directories
 * **r**
  * Allows users to list files in directory
 * **w**
  * Allows users to delete or move files
 * **x**
  * Allows users the right to access files in directory

# Changing Access Rights to Directories and Files
* **chmod**
 * Allows owner to change permissions of a file
 * Options:
  * **u** user
  * **g** group
  * **o** other
  * **a** all
  * **r** read
  * **w** write and delete
  * **x** execute and access directory
  * **+** add permission
  * **-** remove permission
 
