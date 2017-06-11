# Scraping

## What is scraping?

[Scraping](https://en.wikipedia.org/wiki/Data_scraping) is a technique that enables a computer to extract information from a source that is not meant to be readily processed by a computer, such as a scanned image.  You can think of scraping as parsing on steroids.  Up till now, we've talked a lot of about parsing as a fundamental tool in bioinformatics, where we read data from a file that is in a standard format.  We can even use regular expressions to repair broken formats.  However, if there is *no* standard format, then things get more challenging!  [Web scraping](https://en.wikipedia.org/wiki/Web_scraping) is used to describe the scenario where scraping is applied to web content.  This is typically an HTML page that has been transmitted from the server to your web browser, which "knows" how to interpret that HTML to render the page contents on your screen.  

There are now a *lot* of data resources online for biological and biomedical research.  [Genbank] is one of the oldest such resources and has been open access for decades, with a sophisticated interface and the ability to download massive data sets.  However, not all online resources are as accessible, either because they do not have the assets (*e.g.*, webservers, bandwidth) to handle large data transactions - this takes a lot of money! - or because they have some reason for limiting access to data.  These limits can be imposed by paginating the results from a database query (in other words, displaying a large number of results one page at a time, requiring you to follow links through successive pages).  The user is not able to download the results into a local file.  In other cases, access to the database is limited to users with an account on the server, which may have to be arranged with the database curators.  

It is common for users to painstakingly copy-and-paste information from a webpage into a text editor or word processor.  This can be extremely time-consuming!  In some situations, web scraping offers a way to circumvent the limitations set by the database website and automatically extract the entire contents of a database query with a scripting language like Python.  

![](https://imgs.xkcd.com/comics/reassuring.png)


## Scraping etiquette

Before we get into some of the techniques of web scraping, we should recognize that this is generally not a nice thing to do to a website, especially if we get it wrong.  Remember, computers are both extremely fast and extremely stupid.  If you tell your computer to go to a webpage, grab all its contents, follow a link to the next page and repeat, then the computer will do exactly that *very, very fast*.  This is essentially the same as launching a [denial of service attack](https://en.wikipedia.org/wiki/Denial-of-service_attack) on the remote server - you're sending multiple (potentially hundreds) of page requests to the server in the span of milliseconds.  

There are some "best practices" recommendations that have emerged in the developer community around the etiquette of web scraping.  For example, some recommend checking the website's `robots.txt` file, more formally known as the [robots exclusion protocol](https://en.wikipedia.org/wiki/Robots_exclusion_standard), which contains a set of instructions for automated web crawlers that index web sites for search engines such as Google.  You can read more about such recommendations in this [StackOverflow thread](https://stackoverflow.com/questions/2022030/web-scraping-etiquette).

![](https://imgs.xkcd.com/comics/a_new_captcha_approach.png)

In my opinion, one thing that you should *absolutely* make sure is part of your scraping script is to build in some sort of time delay between requests.  This will help prevent your computer from firehoseing requests at the remote server.  You should also be careful when implementing and testing your script to make sure that it is working correctly before letting it loose in the wild.  If you *don't* take such steps, then you risk having your IP address blocked by the web server (or even worse, an entire IP address range that may affect your entire university!).  

To throttle down your Python script, you can make use of the `sleep` function that's available in the `time` module:
```python
>>> import time
>>> time.sleep(10)  # waits for ten seconds
```

You should also check whether the website has a [web API](https://en.wikipedia.org/wiki/Web_API) (application programming interface), which provides a set of tools for automating (scripting) transactions with its database.  For example, NCBI has a web API that you can read more about [here].  It's generally good etiquette to use the website API instead of scraping.


## Web browsing with Python

In order to scrape web content, we first need to get Python to browse the web.  I prefer using the Python module [`mechanize`](https://pypi.python.org/pypi/mechanize/), but it is not included in the standard distribution of Python and is apparently no longer supported by Python 3, so let's proceed with the base Python module `urllib`.  To illustrate how we can open a web site through Python using this module, let's access the university website:
```python
>>> from urllib import request
>>> response = request.urlopen('http://uwo.ca')
>>> src = response.read()
>>> len(src)  # how much HTML are we dealing with?
46566
>>> src[:500]  # let's get a snapshot
b'<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" lang="en">\n<head>\n<meta charset="UTF-8"/>\n<title>Western University</title>\n<meta content="Western University delivers an academic experience second to none. Western challenges the best and brightest faculty, staff and students to commit to the highest global standards.  Our research excellence expands knowledge and drives discovery with real-world application." name="description"/>\n<meta content="Western University, Western, london onta'
```
Wow, Western has a pretty beefy meta content attribute!  

`urllib.request` provides a means of viewing websites with Python, but we're still missing a lot of tools.  First, we need some way of getting Python to parse (interpret) this HTML source into a format that is easier for us to extract information from.  Second, we need to interact with the web page other than submitting URL strings.  For example, how do we follow a link or submit a form, like we would for entering a database query?  Let's deal with our first problem.  To do this, we're going to have to install a non-standard Python module.


## Installing a Python module

The default distribution of Python comes with a *lot* of really great stuff that can be imported from a fairly comprehensive library of modules.  However, there are far more modules out in the wild that make it easy for users and developers to accomplish even more diverse tasks with Python.  Since these modules aren't packaged up with Python, however, we need to [install them ourselves](https://packaging.python.org/installing/).  There are a few approaches to installing modules yourself.  In the long run, the easiest approach by far is to use `pip`, which is essentially a package manager for Python modules that automates a lot of the tedious and at times complex process of compiling and installing modules.  Unfortunately, `pip` usually doesn't come installed along with Python in your operating system.  

Installing `pip` is pretty simple on Linux using a package manager like `apt-get` or `yum`.  On Ubuntu, for example, you can simply enter the command `sudo apt install python3-pip` (assuming you're using Python 3).  If you're using a package manager on a Mac like [MacPorts](https://www.macports.org/) or [Homebrew](https://brew.sh/) that you've already used to install a Python interpreter, then you can install `pip` alongside it.  For example, if you're used MacPorts to install Python 3.5, then you can use the command `sudo port install py35-pip`.  Since this class assumes that you're only starting out with programming and working on the command line, I will generally recommend using a package manager on OS-X because it can be a pain to compile complex packages from source.

If you already have *pip* or have just installed it, then you can install the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) module.  On OS-X, you can do this as follows:
```shell
[Elzar:~] artpoon% sudo pip-3.5 install bs4
The directory '/Users/artpoon/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/artpoon/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting bs4
  Downloading bs4-0.0.1.tar.gz
Collecting beautifulsoup4 (from bs4)
  Downloading beautifulsoup4-4.6.0-py3-none-any.whl (86kB)
    100% |████████████████████████████████| 92kB 1.1MB/s 
Installing collected packages: beautifulsoup4, bs4
  Running setup.py install for bs4 ... done
Successfully installed beautifulsoup4-4.6.0 bs4-0.0.1
```
Note that `pip` was installed as `pip-3.5` on my Mac.  Similarly, `pip` was installed by `apt` on my Ubuntu system as `pip3`, so to install BeautifulSoup we run this command:
```shell
art@Nagisa:~$ sudo pip3 install bs4
[sudo] password for art: 
The directory '/home/art/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/art/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting bs4
  Downloading bs4-0.0.1.tar.gz
Requirement already satisfied (use --upgrade to upgrade): beautifulsoup4 in /usr/lib/python3/dist-packages (from bs4)
Installing collected packages: bs4
  Running setup.py install for bs4 ... done
Successfully installed bs4-0.0.1
You are using pip version 8.1.1, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```
In both cases, we had to use a `sudo` command.  This might be the first time you've encountered this command.  If you're using Apple OS-X, then you should have an administrator account (if this is your own laptop) and the `sudo` password is just the same password that you use to log into your machine.  The same applies to a laptop running Ubuntu or another flavour of Linux.

If you *don't* want to use a package manager on OS-X. then you may have to compile the BeautifulSoup module from source.  Here I'm going to run through the process on my Mac.  First, I download the current source code release from the BeautifulSoup website [here](https://www.crummy.com/software/BeautifulSoup/bs4/download/4.6/).  This is a tarball (a gzipped tape archive) that we can decompress as follows:
```shell
[Elzar:~/src] artpoon% mv ~/Downloads/beautifulsoup4-4.6.0.tar.gz .  # move into ~/src
[Elzar:~/src] artpoon% gunzip beautifulsoup4-4.6.0.tar.gz
[Elzar:~/src] artpoon% tar -xf beautifulsoup4-4.6.0.tar 
[Elzar:~/src] artpoon% cd beautifulsoup4-4.6.0
[Elzar:~/src/beautifulsoup4-4.6.0] artpoon% sudo python setup.py install
```

## Parsing HTML with BeautifulSoup

Let's get back to business.  So far, we've loaded the university homepage in Python:
```python
>>> from urllib import request
>>> response = request.urlopen('http://uwo.ca')
>>> src = response.read()
```
Now let's bring in bs4.  
```python
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(src)
/opt/local/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 1 of the file <stdin>. To get rid of this warning, change code that looks like this:

 BeautifulSoup(YOUR_MARKUP})

to this:

 BeautifulSoup(YOUR_MARKUP, "html.parser")

  markup_type=markup_type))
```
We got a slap on the wrist!  



