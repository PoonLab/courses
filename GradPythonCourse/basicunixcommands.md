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

### `ls`
Let's start by entering a valid command by invoking a program that actually exists.
```shell
art@Misato:~$ ls
Desktop    examples.desktop                 Music     Public  Templates  work
Documents  git                              papers    R       Videos
Downloads  java_error_in_PYCHARM_14175.log  Pictures  src     wip
```

`ls` is a program that lists the files and folders in my home folder, which is my current "location" in the filesystem.  (UNIX was developed at a time where developers had to be extremely frugal with memory and storage; hence cryptic two-letter abbreviations were the norm.)  `ls` is an essential tool for getting the "lay of the land".

![](https://imgs.xkcd.com/comics/server_problem.png)

By default, `ls` doesn't display hidden files --- these are files with names that start with a dot `.` and are usually concealed because they are not meant to be accessed by the user.  Here's a truncated view of my output for an `ls -a` command:
```shell
.                   .gnome2                          R
..                  .gnupg                           .R
.AliView            .ICEauthority                    .remmina
.apport-ignore.xml  .java                            .Rhistory
.bash_history       java_error_in_PYCHARM_14175.log  .rstudio-desktop
.bash_logout        .kde                             src
.bashrc             .lesshst                         .ssh
```

The `-a` is an option, a prescribed way of modifying the command.  In this case, we are modifying the `ls` command to include hidden files in the output.  `ls` has a lot of options.  To learn about them, you should bring up its manual page with the command `man ls`:
```
LS(1)                            User Commands                           LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List  information  about  the FILEs (the current directory by default).
       Sort entries alphabetically if none of -cftuvSUX nor --sort  is  speci‐
       fied.

       Mandatory  arguments  to  long  options are mandatory for short options
       too.

       -a, --all
              do not ignore entries starting with .
```

### `cd`
Look back at the output of `ls -a` --- do you see the `.` and `..`?  Every folder contains those.  These dots are not really files or folders --- they are symbols that enable the user to refer to the current folder, and to the parent of the current folder.  What do we mean by a parent?  A file system has a hierarchical structure; it is a tree that is made up of directed parent-child relationships.  So, each folder is "aware" of its parent folder that sits one level up in the hierarchy.  It's also aware of any child folders that sit at a lower level of the hierarchy, and refer to it as their parent.  

Let's start calling folders "directories" from now on.  It's not as intuitive, but several UNIX commands are derived from this terminology.  To wit, `cd` is an acronym of "change directory".

We can move around in the filesystem using the command `cd`.  If you want to move to a child directory, you indicate this with its name:
```shell
art@Misato:~$ cd Desktop
art@Misato:~/Desktop$ 
```

If we want to move up to the parent directory, we use the following command:
```shell
art@Misato:~/Desktop$ cd ..
art@Misato:~$ 
```

Now let's keep inputting `cd ..` to go as far as we can!
```shell
art@Misato:~$ cd ..
art@Misato:/home$ cd ..
art@Misato:/$ cd ..
art@Misato:/$
```

Let's have a look around:
```shell
art@Misato:/$ ls
bin    dev   initrd.img      lib32       media  proc  sbin  sys  var
boot   etc   initrd.img.old  lib64       mnt    root  snap  tmp  vmlinuz
cdrom  home  lib             lost+found  opt    run   srv   usr  vmlinuz.old
```

This is the root directory, which is represented by the forward slash `/`.  It has no parent --- we're at the base of the tree.  This is deep in the guts of the computer.  The wrong command can do a lot of damage here.  Fortunately, the OS has a child-safety cap on doing most of the bad things. While we're here, let's point out some of the more important directories:
* `/home` is where users keep their own stuff.  It has subdirectories for every user account.  There are generally no limits to reading and writing files in your home directory, but you won't be allowed to modify (or even read) files in another user's directory without special permissions.
* `/usr` is where the OS keeps programs and resources that are meant for users.  
* `/usr/local` is where programs and resources that were installed by users *on this particular machine* are located.
* `/bin` is where binaries (executable files, i.e., programs) live.  These are generally low-level programs that define the OS.  `ls` and `cd` typically live here.
* `/sbin` stores binaries meant for the system, not the typical user.
* `/lib` contains [shared libraries](https://en.wikipedia.org/wiki/Library_(computing)#Shared_libraries), files with resources that can be used by multiple programs and loaded when the program is run.
* `/tmp` is an all-purpose space for temporary files that will probably get wiped when the system is restarted.
For more inforation, see this [wiki](https://en.wikipedia.org/wiki/Unix_filesystem#Conventional_directory_layout) page.


## `pwd` and path specifications
The Unix file system is a big place!  Fortunately, you can always warp back to your home directory by typing `cd` by itself.  Do that and start using `cd` to explore your home directory, then use the command `pwd` to get your bearings:
```shell
art@Misato:~/git/courses/MathJax/config$ pwd
/home/art/git/courses/MathJax/config
```
The sequence of directories returned by `pwd` goes all the way from my current directory `config` back to the root `/`.  This is called an *absolute path*.  I can be anywhere else in the file system and look at the contents of this `config` directory using the command `ls` followed by the absolute path:
```shell
art@Misato:~$ cd /etc
art@Misato:/etc$ ls /home/art/git/courses/MathJax/config
Accessible-full.js     Safe.js
Accessible.js          TeX-AMS_CHTML-full.js
```

Now what if we're feeling lazy and we don't want to do so much typing?  Suppose we happen to be sitting at `/home/art/git/courses`.  We can get the same output with the following, shorter, command:
```shell
art@Misato:~/git/courses$ ls MathJax/config
Accessible-full.js     Safe.js
Accessible.js          TeX-AMS_CHTML-full.js
```

This is a *relative* path because it is defined relative to our current location in the filesystem.  If I moved one level up and tried the exact same command, it won't work.  Hence, relative paths are convenient but fragile.


![](https://imgs.xkcd.com/comics/tar.png)


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
 
