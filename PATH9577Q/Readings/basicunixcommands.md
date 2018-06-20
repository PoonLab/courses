# A brief introduction to &#42;nix

## What is &#42;nix?
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

## You're a user!
UNIX was developed for networked computing environments where a single computer may be accessed remotely and concurrently by multiple users.  This feature was important earlier on when computing resources in academic and research environments were often scarce, and groups needed to maximize the use of their computers.  The very first thing you will do when you first access a UNIX-like system is to create a user account.  If the system is administrated by someone else, then you will need that person or someone else with administrative privileges to create a new account for you.  Every account has a unique username.  Since you will have to type your username frequently and in many contexts, I suggest keeping it as simple as possible.  For example, I prefer to use `art` on systems that I own and administrate.  

Next, you'll have to provide a password in order for your new user account to be activated.  I'm sure you're familiar with making passwords for social media and web services.  Although there are no universal rules for coming up with a password, some flavors of Linux have default requirements.  (These can later be bypassed on the command line, so if you *really* want to use `letmein` as your password, it is possible to make this change after creating your account.)  There are competing philosophies about what makes a good password:

![](https://imgs.xkcd.com/comics/password_strength.png)

When you log into your user account on a UNIX-like machine that is configured to use a desktop environment, you will most likely see a collection of icons and images displayed on the monitor.  You'll need to open a terminal application to see what would normally be rendered in the absence of a desktop: the command line.  In Ubuntu, you can click on the first icon to activate the search function and enter `terminal` to bring up a link to the default Terminal app.  In macOS, you can launch a similar application by activating Spotlight (&#8984;-`space`), typing `terminal` and hitting the `return` key.


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

### `ls` and wildcards
Let's start by entering a valid command by invoking a program that actually exists.
```shell
art@Misato:~$ ls
Desktop    examples.desktop                 Music     Public  Templates  work
Documents  git                              papers    R       Videos
Downloads  java_error_in_PYCHARM_14175.log  Pictures  src     wip
```

`ls` is a program that lists the files and folders in my home folder, which is my current "location" in the filesystem.  (UNIX was developed at a time where developers had to be extremely frugal with memory and storage; hence cryptic two-letter abbreviations were the norm.)  `ls` is an essential tool for getting the "lay of the land".

![](https://imgs.xkcd.com/comics/server_problem.png)

`ls` on its own (without any arguments) will display the entire contents of the directory.  This can be problematic when the directory contains hundreds of files or more!  We can restrict the scope of the directory listing by providing some information about what we're specifically looking for.  On the other hand, we can't simply write out a vague description of what we're looking for, and expect the UNIX command to interpret our request.  Nope, we have to learn how to write out a set of instructions in a strict language that `ls` is going to understand.  The simplest request is to ask `ls` to verify whether a file with a specific name is present in the directory:
```bash
[Elzar:courses/PATH9577Q/Readings] artpoon% ls foo
ls: foo: No such file or directory
[Elzar:courses/PATH9577Q/Readings] artpoon% ls basicunixcommands.md 
basicunixcommands.md
```
We can also chain together a list of filenames to search for, but it quickly gets tiresome writing these all out:
```bash
[Elzar:courses/PATH9577Q/Readings] artpoon% ls DateTime.md GoodCode.md Markdown.md
DateTime.md	GoodCode.md	Markdown.md
```
It would be really helpful if we use some kind of shorthand to denote a number of possible filenames.  This is what [UNIX wildcards](http://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm) are for.  A wildcard is a character that is reserved for a special purpose of representing more than one character.  Here is a brief summary of some wildcards:
* `*` stands for anything: any character can appear any number of times.  If you run `ls *`, it is the same as plain old `ls` - it will list all visible files in the directory.  If you run `ls z*`, then you are asking for a listing of all files with names that start with `z`.
* `?` stands for any character appearing once.  If you run `ls f?b`, the listing can include the filenames `fab` and `fib`, but not `fuz`.
* square brackets are used to restrict the wildcard to a specific subset of characters.  For example, if the directory contains the files `baz`, `bez` and `buz`, we can generate a listing of the first two files with the command `ls b[ae]z`.
* `\` causes the next character to be taken literally if it is a wildcard.  `ls \**` will return a listing of all files whose names start with an asterisk.  Which is a terrible idea.  Don't name your files with asterisks.  Anyhow, this is really useful when you're dealing with a filename that contains a space, which is reserved for separating arguments.
It's especially useful to learn wildcards because they apply not only to `ls` commands, but also to many other commands such as `rm` (deleting files).

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

`man` pages are a great resource when you don't have a network connection:
![](https://imgs.xkcd.com/comics/tar.png)


### File ownership and permissions

Running the `ls` program with the `-l` argument generates a long list format of the directory contents, which looks something like this:
```bash
art@orolo:~$ ls -l
total 60
drwxr-xr-x 2 art art 4096 Apr 30 13:11 Desktop
drwxr-xr-x 2 art art 4096 Apr  6 00:39 Documents
drwxr-xr-x 2 art art 4096 Apr 30 10:08 Downloads
```
The top of the list (`total 60`) reports the total number of blocks occupied by these contents.  A block is a fundamental unit of filesystem storage - on my Ubuntu system, the block size corresponds to 4096 bytes (note that my `ls` output is truncated).  The rest of the list contains one row for every file in the directory (since everything in UNIX is a file, the directories are also listed as files).  The fact that the `Desktop` file is a directory is encoded by the first character in the string `drwxr-xr-x`.  If the file is not a directory, then the `d` would be replaced by a dash `-`.  

The rest of the string is made up of three character triplets that encode the read/write/execute permissions for the file owner, group and everyone.  The owner of the file is given by the third item on the line - in this case, `art`.  Every user is automatically a member of their own group, which takes the same name.  So, I have read, write and execution (`rwx`) permissions for my `Desktop` file.  The act of executing a directory file corresponds to entering that directory and interfacing with its contents.  Any other user on the system can read (see) and execute (enter) my `Desktop` directory, but they can't enact *write* actions such as changing its name to `Sandwich`.

Now let's make a dummy file using the UNIX command `echo` and the redirection operator (we'll learn more about these later):
```bash
art@orolo:~$ echo boo! > dummy.txt
art@orolo:~$ cat dummy.txt
boo!
art@orolo:~$ ls -l
total 72
drwxr-xr-x 2 art art 4096 Apr 30 13:11 Desktop
drwxr-xr-x 2 art art 4096 Apr  6 00:39 Documents
drwxr-xr-x 2 art art 4096 Apr 30 10:08 Downloads
-rw-rw-r-- 1 art art    5 May  1 17:04 dummy.txt
```
According to this output, I have read/write permissions for this new file, but no execution permissions.  It's just a plain text file so I wouldn't expect to try running it as a program.  But what if I did?  For example, I've used the `vi` editor to make a file called `test.py` with the following contents:
```python
#!/usr/bin/env python  # This first line tells the computer that this is a Python script
print('hello world')
```
Here it is in my directory listing:
```bash
-rw-rw-r-- 1 art art   44 May  1 17:07 test.py
```
If I try to run this Python script, I get the following message:
```bash
art@orolo:~$ ./test.py
bash: ./test.py: Permission denied
```
To understand why I had to put an `./` in front of the file name, see the section on *path specifications* below.  Basically, I need to tell the computer where to find the file I want to execute.  `./` is the UNIX way of saying "right here!".

Now, let's change my user permissions on this script:
```bash
art@orolo:~$ chmod 764 test.py
art@orolo:~$ ls -l test.py
-rwxrw-r-- 1 art art 44 May  1 17:07 test.py
art@orolo:~$ ./test.py
hello world
```
What's going on here?  The `chmod` command allows me to set the permissions of a file.  But what is with the number `764`?  Each digit assumes a value between 0 and 7.  It is a compact representation of read/write/execute permissions that we can interpret by converting the digit into its binary representation.  For example, 7 is `111` (4 + 2 + 1) and is used to grant permissions to read, write *and* execute.  6 is `110` and gives members of the group permission to read and write only.  Finally, the binary representation of 4 is `100` and is used here to restrict anyone else to read-only access. 

![](https://imgs.xkcd.com/comics/1_to_10.png)

In this class, it is very unlikely that you will need to muck about with file permissions.  *However* it is useful to be aware of these because file permissions are a common stumbling block when working in a UNIX-like computing environment for the first time, or even when you've been doing it for years!


### Working with the shell

Before we get into some more UNIX commands, let's talk about a few things that are going to make your life easier.  
First of all, your shell remembers the commands that you've entered whether they worked or not.  To get a list of them, type `history`:
```shell
art@Misato:~/git/courses/GradPythonCourse/src$ history | tail
 1831  ls
 1832  cd ..
 1833  ls
```

The really handy thing is that you can retrieve previous commands using the `up` arrow key (and pressing `down` to return towards the bottom of the histoy list).  This can save you a lot of typing.  

The second thing that you should know is that the `tab` key will autocomplete a command or the name of a file or directory *if* there are no other possibilities.  For example, if I type `head b` and there is only one file or directory in my current location in the filesystem that starts with `b`, then the rest of that name will get autocompleted with `tab`.
 
Third, you can jump to the start of a line with `Control-A` and skip back to the end of the line with `Control-E`.  Hence,  even though you don't get to move your cursor around with the mouse pointer anymore (because the terminal application is not a GUI), you can still move around fairly quickly.


### `cd`
Okay, let's get back to business.  Look back at the output of `ls -a` --- do you see the `.` and `..`?  Every folder contains those.  These dots are not really files or folders --- they are symbols that enable the user to refer to the current folder, and to the parent of the current folder.  What do we mean by a parent?  A file system has a hierarchical structure; it is a tree that is made up of directed parent-child relationships.  So, each folder is "aware" of its parent folder that sits one level up in the hierarchy.  It's also aware of any child folders that sit at a lower level of the hierarchy, and refer to it as their parent.  

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

Typing `cd` by itself will return you to your home directory:
```shell
art@Misato:~/some/faroff/land$ cd
art@Misato:~$ 
```
and we can get the same result with `cd ~`.  The tilde `~` character is the [UNIX symbol for your home directory](https://www.gnu.org/software/bash/manual/html_node/Tilde-Expansion.html), and can save you some typing when you're writing out a relative path.  Note that the tilde appears in the prompt `art@Misato:~$` which was configured on that computer to remind the user about their location in the filesystem.

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

This is the root directory, which is represented by the forward slash `/`.  It has no parent --- we're at the base of the tree.  This is deep in the guts of the computer.  The wrong command can do a lot of damage here.  Fortunately, the OS has a child-safety cap on doing most of the bad things in the form of user/group privileges.

## Making and removing: `mkdir`, `rmdir` and `rm`

To create a new directory, you need to use the `mkdir` (make directory) command:
```shell
art@orolo:~/Desktop$ mkdir test
art@orolo:~/Desktop/test$ pwd
/home/art/Desktop/test
```
You can also submit a relative or absolute path as an argument to `mkdir` and it will create the directory at that location, so long as the rest of the path exists.  For example, if I had used:
```shell
art@orolo:~$ mkdir Desktop/test
art@orolo:~$ cd Desktop
art@orolo:~/Desktop$ cd test
art@orolo:~/Desktop/test$ pwd
/home/art/Desktop/test
```
then I will have achieved the same result, but if I tried:
```
art@orolo:~$ mkdir foobar/test
mkdir: cannot create directory ‘foobar/test’: No such file or directory
```
then the command fails because there was no directory `foobar` relative to my current location in the filesystem.

If you change your mind, then you can erase a directory using the `rmdir` (remove directory) command:
```shell
art@orolo:~/Desktop$ rmdir test
art@orolo:~/Desktop$ cd test
bash: cd: test: No such file or directory
```
However, this will only work if the directory does not contain any files or other directories.  If you are *absolutely certain* that you want to delete the directory and all of its contents, then you can nuke it from orbit with this command:
```shell
art@orolo:~/Desktop$ ls test
a_file.txt
art@orolo:~/Desktop$ rmdir test
rmdir: failed to remove 'test': Directory not empty
art@orolo:~/Desktop$ rm -rf test
```
**BE CAREFUL.**  Once you have run this command, there is no easy way to recover your directory or files.  This is **NOT** the same as moving these items into a "Trash" or "Recycling" folder like in Windows or macOS desktop operating systems. 

There are two options being set in this call to `rm`.  The `-r` flag means that we want to *recursively* remove files and directories starting from our location and all the way down to the last child directory.  The `-f` flag stands for *force* -- we are telling `rm` that we want to remove files and directories without the program repeatedly asking us "are you sure?".  The combination of these options makes this command exceedingly dangerous.

Since we're on the topic of `rm`, I want to finish off this section with a mention that `rm` can be used with UNIX wildcards just like we have done with `ls`.  If we want to delete a specific file (let's call it `foo`), we call:
```shell
art@orolo:~/Desktop$ rm foo
```
If we want to delete all files in the current directory that start with the letter `f`:
```shell
art@orolo:~/Desktop$ rm f*
```
and so on.

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


## The `$PATH` environment variable

So far we've run a few commands and used these commands to starting exploring the *nix filesystem. What are these commands? How does the computer know what to do when we type in these two-letter combinations? The basic answer is that in the *nix world, *everything is a file*. `ls` is a file. More specifically, it is a binary executable, a file made up of `0`s and `1`s that encode a set of instructions for the computer, and does not encode information that is meant to be decoded and displayed to the user in a readable format.

Where is this file? You can find this out with another command called `which` (and yes, `which` is also a file):
```shell
art@Kestrel:~$ which ls
/bin/ls
art@Kestrel:~$ ls -lh /bin/ls
-rwxr-xr-x 1 root root 124K Mar  2  2017 /bin/ls
```

Note that we didn't have to tell the computer where the program `ls` is. This is because *nix keeps track of a list of folders to look for executable files. This list is stored as an [environment variable](https://en.wikipedia.org/wiki/Environment_variable). You can think of these variables as the command-line version of the operating system preferences. When we call an executable, the operating system searches through the list of paths that is stored in the variable `PATH`. To look at the contents of `PATH`, we have to use a `$` symbol to tell the OS that we are referring to the environment variable and not the string:

```shell
art@Kestrel:~$ echo PATH
PATH
art@Kestrel:~$ echo $PATH
/home/art/bin:/home/art/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
```

This is a list of absolute paths that is delimited (separated) by `:` characters. The computer starts reading this list from left to right. The first path is in my home directory, `/home/art/bin`. The name of this folder implies that it would hold binary executables, but I'm pretty certain that I never installed any executables in my own home folder:
```shell
art@Kestrel:~$ ls /home/art/bin
ls: cannot access '/home/art/bin': No such file or directory
```

Fine. The computer doesn't mind that this directory doesn't exist. It just moves onto the next path in the list. Note that because the computer starts searching these paths from the left of the list, the leftmost path takes precedence over paths to the right. If you have two binary executable files with the same name, then the file in the leftmost path will get run first. For example, sometimes people have more than one copy of `python` installed on their computer -- these may be different versions of Python. With my `$PATH`, the `python` at `/usr/local/bin` would always be run instead of another copy at `/usr/bin` unless I specifically ask for the latter by invoking it with an absolute or relative path.


## File permissions

When we ran the `ls` command in long list mode with the flag `-l`, we saw some scary stuff. Here it is again:
```shell
art@Kestrel:~$ ls -l
total 80
drwxrwxr-x  2 art art  4096 Apr 14 22:17 Desktop
drwxr-xr-x  4 art art  4096 Apr 10 19:33 Documents
drwxr-xr-x  4 art art 12288 Apr 15 22:43 Downloads
drwxrwxr-x 19 art art  4096 Apr 15 22:40 git
```

Each line represents a file or directory. Again, since everything in *nix is a file, a directory is just a special kind of file. To really understand what each line means, let's drill down on `Desktop`:

* `d` means that this file is a directory. If it was just a regular file then we'd see a `-`.
* The first `rwx` means that the owner of this file has permissions to read, write or execute the file. For a directory, `x` sets the permission to access and view the contents of the directory.
* The second `rwx` specifies these same permissions for users in the group assigned to this file.
* The third `rwx` specifies the permissions for everyone else.
* `2` indicates the number of blocks taken up by this file. In *nix, space in the file system is allocated in 4 kilobyte blocks.
* `art` indicates that I am the owner of this file.
* The second `art` indicates that the file is assigned to a group called `art`. Every user in the system also has a group with their same name.
* `4096` gives the size of the file in bytes.
* `Apr 14 22:17` gives the date and time that this file was last modified.
* `Desktop` is the name of the file

Modifying the permissions of a file is a topic that is a bit outside the scope for this course. However, it is useful to be aware of permissions because they can occasionally cause problems for processing data and running scripts, especially when you are working with other users on the same system. To illustrate, I'm going to make a dummy file and then deny myself permission to edit it:

```shell
art@Kestrel:~$ echo "This is a fake file" > temp.txt
art@Kestrel:~$ cat temp.txt
This is a fake file
art@Kestrel:~$ ls -l temp.txt
-rw-rw-r-- 1 art art 20 Apr 16 00:04 temp.txt
art@Kestrel:~$ chmod -w temp.txt
art@Kestrel:~$ ls -l temp.txt
-r--r--r-- 1 art art 20 Apr 16 00:04 temp.txt
art@Kestrel:~$ echo "Let's try to write more" > temp.txt
bash: temp.txt: Permission denied
art@Kestrel:~$ chmod +w temp.txt
art@Kestrel:~$ echo "Please?" > temp.txt
art@Kestrel:~$ cat temp.txt
Please?
```



## Examining files (`wc`, `cat`, `head`, `tail`)

Okay, so now we're done looking around the filesystem.  We want to do some actual work here - let's inspect a file.  But we're not going to double-click on a file and wait for it to open up in some application like TextEdit or Excel.  The whole point of learning bioinformatics is (1) we are often dealing with files that are way too large to open in a standard application, and (2) we are often dealing with files that are too complex to deal with in a graphical user interface.  Bioinformatics exists in part because molecular technologies change so rapidly that every year brings a new *kind* of data, and a whole menagerie of competing formats.  

Let's start simple.  We're going to go to the `examples` directory, where there is a small text file named (out of a lack of creativity) `small-text-file.txt`.  Before we go right in there and view it, we want to have some idea of what we're dealing with.  For example, we can use `ls -s -h` to list files along with information about how much hard drive space they are taking up:
```shell
art@Misato:~/git/courses/GradPythonCourse/examples$ ls -s -h
total 12K
12K small-text-file.txt
```

Another useful tool is `wc`, which stands for word count.  This program calculates the number of lines, words and bytes that make up a file:
```shell
art@Misato:~/git/courses/GradPythonCourse/examples$ wc small-text-file.txt 
 4 16 74 small-text-file.txt
```

So we know that we're dealing with a small file with four lines, and that it's probably safe to display its full contents in the shell.  To do that, we use another program called `cat`.  
```shell
art@Misato:~/git/courses/GradPythonCourse/examples$ cat small-text-file.txt 
This is a small text file. 
There are many like it
but this one is mine.
```

What if we're dealing with a large file?  If we used `cat`, then our console would go bonkers with streaming text.  In this case, let's use some other commands that show the first and last few lines of the file.  The number of lines to display is controlled by the `-n` option.  Since our example file is tiny, we'll just display the first and last lines.
```shell
art@Misato:~/git/courses/GradPythonCourse/examples$ head -n1 small-text-file.txt 
This is a small text file. 
art@Misato:~/git/courses/GradPythonCourse/examples$ tail -n1 small-text-file.txt 

```
Something kind of goofy happened here - since I ended the file with an [end of line](https://en.wikipedia.org/wiki/Newline) character, the tail command is returning a blank.

This is still pretty limiting.  What if we're trying to find something specific, like a protein sequence motif or a diagnosis?  This is where `grep` comes in.  To *really* get mileage out of `grep`, you need to learn [regular expressions], which we're going to cover in a later session.  However, `grep` works just as well with a plain word:
```shell
art@Misato:~/git/courses/GradPythonCourse/examples$ grep mine small-text-file.txt 
but this one is mine.
```
This command returned all lines that contain the word "mine" - for this example, there is only one such line.  What do we do if we are running this command on an immense file, and an enormous number of lines is getting returned?   (For an answer, see the next section.)

One more thing about `grep`.  One of the most useful ways of using `grep` is recursively - that is, to search through *all* the files contained in the present working directory as well as all other directories nested within.


## Bringing things together with pipes

As I mentioned before, one of the philosophies behind UNIX is that we should be able to use the output of one command as the input for another.  This is accomplished with pipes, which are represented by the character `|`.  The question I ended the last section with was deliberately a segue into the use of pipes.  What if running a `grep` command produces too much output to be usefully displayed?  We can pipe this output to any of the commands that were introduced in the previous section to deal with large files.  To illustrate, I'm going to use an HIV-1 integrase data set that is in the public domain:
```shell
art@Misato:~/git/courses/GradPythonCourse/examples$ grep Canada IN.txt | wc
    795  236902 1186681
art@Misato:~/git/courses/GradPythonCourse/examples$ grep Canada IN.txt | head -n1
1770	71510	INT_3448	Canada	< 2003	B	None	-	-	--	-	-	-	-	-	-	-	-	-	--	-	-	-	-	RK	
```
Note I still had to truncate the output of `head` because there are so many variables for each record.

What if I want to save this output to a file so that I can do something with it later?  That's easy:
```shell
art@Misato:~/git/courses/GradPythonCourse/examples$ grep Canada IN.txt > Canada.txt
```
The `>` character tells UNIX to "redirect" the output stream to a file.  Note that if we use the same command but search for a different word, everything in `Canada.txt` will be erased and replaced with the new output.  To preserve the previous content and append the new output to the bottom of the file, we use the redirection symbol `>>`.  

![](https://imgs.xkcd.com/comics/cautionary.png)
