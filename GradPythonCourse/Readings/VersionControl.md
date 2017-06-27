# Version control with git

## What is version control?

There are several situations where a script evolves through different versions of itself.  As you're developing the script, you will often need to spend time shaking out the bugs.  When you've written a script, you might need to adapt it to a related but slightly different computing problem.  In the latter case, it is tempting to keep multiple versions of the script on your computer as separate files with slightly different names.  

![](https://imgs.xkcd.com/comics/documents.png)

The situation gets even more difficult when you are collaboratively developing a script with someone else.  Suppose that you are both starting from the same copy.  You start to modify a part of the script, but unknown to you, your colleague is also modifying the same part of the script.  A number of problems can arise here:
* One developer accidently overwrites the work of the other
* There are multiple copies of a file with the same name on different computers
* Once we realize that there are multiple copies, it is difficult to go back and figure out who did what

If you're new to programming and working in UNIX-like systems, then you are probably most familiar with the concept of version control through some system like Microsoft Word's *Track Changes* feature.  In some ways, the version control systems that are used for programming are simpler because they are generally used on plain-text files where the differences between two versions of the same file are relatively clear.  However, this also allows for far more powerful and scaleable systems that can store years-long revision histories on large numbers of documents.  

In the context of bioinformatics, version control is important for reproducible science.  If you don't track the changes that you've made to a script, then you may have no way of reconstructing *exactly* how you processed your data!  Accredited clinical laboratories using bioinformatic pipelines to process next-generation sequence data are now required by the College of American Pathologists to record the specific version of the pipeline used to process a patient's sample, and other groups have issued similar recommendations, including the [American College of Medical Genetics and Genomics](https://www.acmg.net/) and the [US Centers for Disease Control and Prevention](https://www.cdc.gov/). 

In short, if you're going to get serious about doing bioinformatics then you need to learn how to use a version control system for your projects.


## git

The fact that you're reading this document implies that you're accessing the course materials online through GitHub, or that you've cloned this repository on your own computer and are reading it off-line.  In other words, you've already been working with a version control system called [git](https://en.wikipedia.org/wiki/Git)

![](https://imgs.xkcd.com/comics/git.png)
