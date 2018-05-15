# Take-home assignment 1
## Building a project folder

In this assignment, you will need to use some basic UNIX commands that you've learned in class to build a project folder, which is simply a set of directories for storing files that are related to a specific project.  Building and maintaining a project folder is like flossing your teeth or keeping a tidy lab bench; it's important to do it routinely, but many people don't bother to do it consistently.  There are no universally accepted rules for how to put together a project folder, but it is important to decide on a consistent approach for yourself.  [Here](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424) is a paper (yes, an actual scientific paper!) that provides an accessible discussion into how the author goes about organizing her project folders.

1. The first decision you need to create a directory in the filesystem where you are going to store your projects.  The files in this directory are going to be owned by you -- only you as user should normally have read-write access to the project files.  Use the code block below to paste in the UNIX commands you used to carry out the following steps:
   ```bash
   # create the directory for storing your projects
   
   # move into this new directory
   
   # create a project folder with an arbitrary name
   
   # give the output of `pwd` to show your location in the filesystem
   
   ```

   In the section below, *briefly* explain why you chose this particular location in the filesystem:
   ```
   
   ```

2. Next, you need to populate your project folder with some default directories.  I like to use the following directories:
   * `data` for storing the unprocessed data files
   * `scripts` for storing Python and R scripts that act on files in `../data`
   * `results` for storing the outputs of the processing scripts
   * `doc` for storing plain text and PDF documents that relate to the project
   In the following code block, paste in *all* the commands that you used to create these folders.
   ```bash
   
   ```
   
3. Finally, it is helpful to create a `README` plain text or Markdown file at the top level of your project folder.  This file should contain a concise description of the project (*i.e.*, the data source, hypothesis, specific objectives).  It can also be used as a rough journal that you should update with regular entries describing what scripts you just wrote or modified, and the outputs they generated.  Using a text editor, create a `README` file, save it to your project folder, and then paste the output of `ls -l` below:
   ```bash
   # output of long list command here
   ```
   Briefly describe the characteristics of this file below, *i.e.*, read-write permissions, ownership, file size.
