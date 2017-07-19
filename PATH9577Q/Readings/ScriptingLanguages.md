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

In the post-genome era, this has remained true - the reduced one-time cost of developing a script tends to win over the performance advantage of compiled code that is more time-consuming to build.  There is a perpetually expanding range of biological applications for new molecular technologies.  The scale and complexities of data sets are constantly evolving.  In addition, scripting languages are usually easier to learn when you're just getting started with computer programming.  

I've mentioned that scripting languages tend to be slower than compiled languages, because the additional layer of abstraction takes you further away from the underlying hardware.  As a result, scripting languages are also considered to be useful for *prototyping*, where you can quickly implement an idea to see how it works, or how to go about doing it, before commiting time and resources to re-implement a faster, optimized version of the method in a compiled language.


## Perl, Python and Ruby

For a long time, Perl was the [lingua franca](https://en.wikipedia.org/wiki/Lingua_franca) of bioinformatics.  This might be attributable, at least in part, to the role it played in the [Human Genome Project](https://web.stanford.edu/class/gene211/handouts/How_Perl_HGP.html).  However, [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) and [Ruby](https://en.wikipedia.org/wiki/Ruby_(programming_language)) are two slightly newer scripting languages whose designs were directly influenced by Perl.  Over the years, Python [seems to have gradually displaced Perl](https://trends.google.ca/trends/explore?cat=174&date=all&q=%2Fm%2F05zrn,%2Fm%2F06ff5,Python) as the predominant langauge for bioinformatics, as well as other industries and outside of academia.  This does not mean that Python is a "better" language than Perl or Ruby.  Arguing about the superiority of the different languages is like arguing about whether a pickup truck is better than a sports car or a mini van.  [They all get you from point A to point B](http://users.cms.caltech.edu/~mvanier/hacking/rants/cars.html), have different strengths and weaknesses, and even different cultures associated with their developer and user communities.

![](https://imgs.xkcd.com/comics/11th_grade.png)

For today, at least, a fair case can be made that Perl, Python and Ruby are the three dominant general-purpose scripting languages.  Besides their differences in [syntax](https://en.wikipedia.org/wiki/Syntax_(programming_languages)), these languages have different programming philosophies, which tend to reflect the preferences and personalities of their original developers.  (An interesting aspect of programming languages is that they are often designed by a single person instead of a group.)  


### Perl

Perl was designed to be concise and flexible, removing many of the finer details of writing code that can consume a developer's time, such as allocating memory, working with basic objects such as strings and [associative arrays](https://en.wikipedia.org/wiki/Associative_array), and providing easy access to [regular expressions](https://en.wikipedia.org/wiki/Regular_expression).  Many of these design principles, such as [dynamic typing] and getting memory allocation for free, were inherited by Python and Ruby.  

Perl is often criticized as resulting in opaque code that is difficult to maintain.  Like many criticisms, some aspects of this are unfair.  You can write clear, well-documented code just as readily in Perl as in other programming languages.  One hurdle to this, however, is that there are often many ways of accomplishing the same task in Perl.  I haven't done much work with Perl, so to provide a code example I am using a snippet from some code published by [Illumina](https://www.illumina.com/science/education/truseq/scripts.html) that scans through a file containing genome sequence and marks which positions contain an ambiguous base (`N`):

```perl
my $a=();
my $start=0;
#====finding Ns in the specified genomic range=====
open(IN, "$ARGV[0]"); #genome fasta
my @lines = <IN>;
close IN;
my $pos = $start;
my %Ns = ();
for($i=1;$i<@lines;$i++) #The 1st line is header
{
  chomp $lines[$i];
  @a = split //,$lines[$i];
  for($j=0;$j<@a;$j++)
  {
    if($a[$j] eq 'N')
    {
      $Ns{$pos} = 1;
    }
    $pos++;
  }
}
```


### Python

I do most of my day-to-day coding in Python.  Part of the reason why is that it was the scripting language in use in the bioinformatics lab that I trained in as a postdoctoral fellow.  However, I also simply like the language.  Python is notorious for its use of whitespace to define code blocks, and for the guiding principle that "[there should be only one way to do it](https://www.python.org/dev/peps/pep-0020/)".  This means that I should be able to look at a Python script that someone else wrote and immediately get the general idea of what's supposed to happen.  More importantly, I should be able to look at my *own* scripts weeks after writing them and understand what I had intended to do.  

![](https://imgs.xkcd.com/comics/python.png)

Here is my attempt at translating the Perl code example into Python:
```python
import sys

# read filename from command line
infile = sys.argv[1]

handle = open(infile, 'rU')
_ = handle.readline()  # discard header line

Ns = []  # span multiple lines
for line in handle:
    # we assume that the line consists entirely of nucleotide sequence
    seq = line.strip('\n')
    for base in seq:
        Ns.append(1 if base == 'N' else 0)
```

There are two ways of working with Python.  First, you can launch an interactive shell by simply typing `python` on the command line.  This is alright for small tasks or for calling functions from modules (something we'll learn about later), but it's not convenient when you need to write a lot of code.  It is possible to compose your script in a text editor and then copy-paste the text into an interactive shell, but at that point you might as well run the script in a non-interactive mode (in addition, whitespace can become an issue when copy-pasting code blocks into the shell).

In a non-interactive mode, the Python interpreter processes the entire contents of a file.  You have to indicate which file you want to run with an absolute or relative path as the first argument on the command line.  If the script is in your present working directory, then you can simply provide the filename:
```shell
python foobar.py
```

A script often takes additional arguments and options from the command line; for example:
```shell
python foobar.py -h
python foobar.py filename1 filename2
```

### Ruby

Ruby is widely known in association with Rails, which has been a popular framework for web applications including GitHub, Hulu, and (originally) Twitter.  As a scripting language, Ruby is generally distinguished from Perl and Python for being more "object oriented".  In object-oriented programming, we are creating a class of objects - any object that belongs to that class inherits the attributes and "abilities" (methods) of the class.  For example, I might create a `Pizza` class with the attributes `topping` and `slices` and the method `eat`, and then generate several objects from the class that I call `Pepperoni`, `Hawaiian` and `Margherita`.  We could set the `Pizza` object `Hawaiian` to have `topping="pineapple"` and then call its function `eat` to subtract `1` from its value `slices`.  Neither action affects the other `Pizza` objects - they belong only to `Hawaiian`.

For example, the number `2` is an object of the `Integer` class in Ruby:
```ruby
irb(main):001:0> 2.even?
=> true
irb(main):002:0> 2.odd?
=> false
irb(main):003:0> 2.round(1)
=> 2.0
```

Here's my attempt at translating the Illumina code into Ruby:
```ruby
infile = ARGV[0]
Ns = Array.new
File.open(infile, 'r') do |handle|
  lines = handle.lines
  lines.next
  lines.each do |line|
    seq = line.chomp  # remove line break
    seq.each_char do |b|
      if b=='N'
        Ns << 1 
      else
        Ns << 0
      end
    end
  end
end
```
Caveat: I've worked a bit with Ruby but I wouldn't list it on my resume.  [YMMV](https://en.wiktionary.org/wiki/your_mileage_may_vary).


