# Understanding Basic Unix Commands

# What is *nix
* UNIX is an operating system developed int he 1960's
* UNIX has proven to be a reliable multi-user and multi-tasking system
* There are different types of UNIX
  * Sun Solaris
  * GNU/ **Linux**
  * MacOS X

# Basics of the Operating System
* **The Kernel**
  * Essentially the "Hub"
  * Works with **The Shell** by managing the filestore/communications involved in system calls
* **The Shell**
  * Serves as an interface between the user and the kernel
  * The Shell is a Command Line Interpreter (CLI)
  * Essentially, it will understand commands and carry out their function

# Directories
## Finding where files are kept
* The file system is arranged in a hierachial structure
* / is the **root** directory
* /bin is a subdirectory of the root directory that contains programs that are necessary for the most basic functions of the system (ie. starting and repairing the system)
* /usr is also a subdirectory of the root directory that can be broken down into two sub categories
  * /usr/bin are programs run by users and are necessary for the functions of the system
  * /usr/local/bin are where installed programs by the user are stored

# Basic Commands
* **ls**
 * Lists files in your current working directory
 * Exception: Unless you are very familiary with Unix, some files should not be changed and are kept hidden
 * These files begin with a period (.)
 * To find all files, use the **ls -a** command
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
 

