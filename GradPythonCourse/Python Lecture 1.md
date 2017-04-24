# **Python Lecture 1**

## What is a scripting language?

A programming language provides a convenient way for a person to write a set of instructions for a computer to follow.  Put another way, a programming language adds a level of [abstraction](http://stackoverflow.com/questions/21220155/what-does-abstraction-mean-in-programming) that are converted into the low-level instructions that are actually being carried out at the level of the processor.  In general, the processing of converting human-readable instructions (source code) into computer-readable instructions (machine code) is compiling.  

[Compiled programming languages](https://en.wikipedia.org/wiki/Compiled_language) are far more convenient than direclty writing machine code -- the cost for this convenience, however, is that the end result is not necessarily the most optimal machine code for a given processor.  ([Programs that are written in assembly language](https://en.wikipedia.org/wiki/RollerCoaster_Tycoon_(video_game)#Development), which has a lower level of abstraction than compiled languages, can outperform the latter.)  You may have heard of several different compiled languages, such as C, BASIC, or Fortran.

Compiling can take a long time.  Before multi-core processors became commonplace, compiling your code was a good excuse to take a break.

![](https://imgs.xkcd.com/comics/compiling.png)

A scripting language provides an even higher level of abstraction than compiled languages, which enables them to be far more readable and concise.  Scripting languages are often implemented in a compiled language.  For example, the main Python interpreter was written in C.  Instead of being compiled into an executable binary program, however, a script is typically converted at [run-time](https://en.wikipedia.org/wiki/Run_time_(program_lifecycle_phase)) into a number of elementary tasks that have already been implemented in the compiled code.  Because of this additional layer of abstraction, a program written in a scripting language is generally going to be slower than one written in a compiled language.  On the other hand, the scripting language program is a lot easier to write.  (Like making macaroni and cheese with a Kraft Dinner mix instead of growing a wheat field, harvesting the grain, milling the grain into flour...)


## Why scripting?
Scripting languages have become an important part of bioinformatics, but why did this happen?  I don't think there's an obvious answer for this.  Part of it may have been historical contingency.  The scripting language [Perl](https://en.wikipedia.org/wiki/Perl) became associated with the [Human Genome Project](https://en.wikipedia.org/wiki/Human_Genome_Project).  There's a nice article about this historical development [here](https://web.stanford.edu/class/gene211/handouts/How_Perl_HGP.html), including a quote that encapsulates this association nicely:

>Some groups attempted to build large monolithic systems on top of complex relational databases; they were thwarted time and again by the highly dynamic nature of biological research. By the time a system that could deal with the ins and outs of a complex laboratory protocol had been designed, implemented and debugged, the protocol had been superseded by new technology and the software engineers had to go back to the drawing board.
- [Lincoln Stein](https://en.wikipedia.org/wiki/Lincoln_Stein)

In the post-genome era, this has remained true - the reduced one-time cost of developing a script tends to win over the performance advantage of compiled code that is more time-consuming to build.  There is a perpetually expanding range of biological applications for new molecular technologies.  The scale and complexities of data sets are constantly evolving.  In addition, scripting languages are simply easier for biologists to learn.  


## Perl, Python and Ruby

I think that for a long time, Perl was the [lingua franca](https://en.wikipedia.org/wiki/Lingua_franca) of bioinformatics.  However, [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) and [Ruby](https://en.wikipedia.org/wiki/Ruby_(programming_language)) are two slightly newer scripting languages that were directly influenced by Perl.  Over the years, Python [has gradually displaced Perl](https://trends.google.ca/trends/explore?cat=174&date=all&q=%2Fm%2F05zrn,%2Fm%2F06ff5,Python) as the predominant langauge for bioinformatics, as well as other industries and outside of academia.

For today, at least, a fair case can be made that Perl, Python and Ruby are the three dominant general-purpose scripting languages.  Besides their differences in [syntax](https://en.wikipedia.org/wiki/Syntax_(programming_languages)), these languages have different programming philosophies.  Perl is designed to be 


