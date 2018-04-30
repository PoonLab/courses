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

`man` pages are a great resource when you don't have a network connection:
![](https://imgs.xkcd.com/comics/tar.png)


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
