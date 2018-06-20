
## Explore the filesystem (In-class assignment 1)

It's useful to develop a general sense of how your filesystem is laid out.  One way to go about this is to use the `cd`, `ls` and `pwd` commands that we've just covered to move around and get to know what goes where!  Using the worksheet distributed in class, I want you to draw a partial map/outline of your filesystem.  At each branch, you should write a brief note about the role/contents of the corresponding directory.

1. Start in your home directory (remember how to get there?).  You'll start mapping from the house on the worksheet.
2. Move up to the top of the filesystem using the command `cd ..`.  At each level, draw a short line from the current directory upwards and label it with the name of the parent directory.  
3. Repeat step 2 until you reach the root, *i.e.,* running `cd ..` fails to change the present working directory.
4. Now we want to start exploring one level down from the root.  Draw branches downwards for `/usr` and at least 3 other child directories under `/`.  Some of these directories will contain binary executables, such as `/bin`.  Here are some brief descriptions of what you might encounter:
  * `/bin` contains binaries that are needed to boot or repair the system in single user mode.
  * `/sbin` contains binaries that are similar in function to those in `/bin` but are not normally executed by users.
  * `/usr` contains resources that are required by users.  These files are generally read-only (not to be modified by users) and meant to be accessed by all users.
  * `/home` is where users keep their own stuff.  It has subdirectories for every user account.  There are generally no limits to reading and writing files in your home directory, but you won't be allowed to modify (or even read) files in another user's directory without special permissions.
  * `/lib` contains [shared libraries](https://en.wikipedia.org/wiki/Library_(computing)#Shared_libraries), files with resources that can be used by multiple programs and loaded when the program is run.
  * `/tmp` is an all-purpose space for temporary files that will probably get wiped when the system is restarted.
For a more complete explanation, [The Linux Documentation Project](https://www.tldp.org/LDP/Linux-Filesystem-Hierarchy/html/the-root-directory.html) has an excellent guide to the filesystem.
5. Since there are a very large number of directories two levels down from the root, let's focus on the `/usr/local` branch.  Draw branches for all child directories under `/usr/local` and a brief description of each.
  * `/usr/local` is where programs and resources that were installed by users *on this particular machine* are located.
6. Use the command `which python` or `which python3` to locate your default Python executable (more on this later).  Label this location on your map.  
