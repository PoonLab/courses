# Scraping

## What is scraping?

[Scraping](https://en.wikipedia.org/wiki/Data_scraping) is a technique that enables a computer to extract information from a source that is not meant to be readily processed by a computer, such as a scanned image.  You can think of scraping as parsing on steroids.  Up till now, we've talked a lot of about parsing as a fundamental tool in bioinformatics, where we read data from a file that is in a standard format.  We can even use regular expressions to repair broken formats.  However, if there is *no* standard format, then things get more challenging!  [Web scraping](https://en.wikipedia.org/wiki/Web_scraping) is used to describe the scenario where scraping is applied to web content.  This is typically an HTML page that has been transmitted from the server to your web browser, which "knows" how to interpret that HTML to render the page contents on your screen.  

There are now a *lot* of data resources online for biological and biomedical research.  [Genbank](https://www.ncbi.nlm.nih.gov/genbank/) is one of the oldest such resources and has been open access for decades, with a sophisticated interface and the ability to download massive data sets.  However, not all online resources are as accessible, either because they do not have the assets (*e.g.*, webservers, bandwidth) to handle large data transactions - this takes a lot of money! - or because they have some reason for limiting access to data.  These limits can be imposed by paginating the results from a database query (in other words, displaying a large number of results one page at a time, requiring you to follow links through successive pages).  The user is not able to download the results into a local file.  In other cases, access to the database is limited to users with an account on the server, which may have to be arranged with the database curators.  

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

### Caveat: Problems with installing BeautifulSoup with `apt` on Ubuntu

When I attempted to install BeautifulSoup using the Ubuntu package manager `apt`, it appeared to be successful; however, firing up an interactive session of Python and loading this module proved otherwise:
```python
>>> import bs4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
AttributeError: module 'html5lib.treebuilders' has no attribute '_base'
```
This is a [known issue](https://bugs.launchpad.net/beautifulsoup/+bug/1603299) that is apparently caused by a change in newer versions of the module `html5lib` that is a requirement for running BeautifulSoup.  The workaround is to install an older version of `html5lib`:
```shell
sudo pip3 install html5lib==0.9999999
```


## Understanding HTML

In order to use Python to scrape web content, you're going to need at least a basic understanding of HTML.  [HTML](https://en.wikipedia.org/wiki/HTML) stands for hypertext markup language.  Yes, it's a markup language like [Markdown](https://en.wikipedia.org/wiki/Markdown), but a lot more complex and a lot older!  Like Markdown, HTML uses special characters to express context for what would otherwise be plain text.  HTML accomplishes this with *tags*.  A tag is a string enclosed in angle brackets, like this:
```html
<b>This will rendered in bold typeface.</b>
```
Here, `<b>` is the opening tag and `</b>` is the closing tag for an HTML bold element.  If you're reading this in a web browser, then you'll see the result of rendering this HTML here:
<b>This content will rendered in bold typeface.</b>

![](https://imgs.xkcd.com/comics/tags.png)

In order to get correctly rendered by a web browser, an HTML document needs to conform to a [specification](https://developer.mozilla.org/en/docs/Web/HTML/Element).  In very broad terms, an HTML document should have the following high-level structure:
```html
<html>
 <head>
   <!-- contains general information about the document -->
   <meta charset="utf-8">
   <title>This content is displayed at the top of the window or tab.</title>
 </head>
 <body>
   <!-- generally the content of the page that is displayed -->
   <p>This content is rendered as a paragraph.</p>
 </body>
</html>
```
Note that the start and end tags `<!--` and `-->` enclose are used to enclose hidden content (comments) in HTML.  They won't get displayed when the HTML source is rendered by a web browser.

Nowadays, HTML source is seldom written by hand.  For instance, there are several "what you see is what you get" ([WYSIWYG](https://en.wikipedia.org/wiki/WYSIWYG)) word processors and graphics editors that will automatically convert a document into HTML source.  However, this results is enormous source files that are extremely difficult for a person to read.  To illustrate, here is an excerpt from the source file that is generated when I opened a Word document, typed in `Boo.` and saved it as an HTML file:
```html
<html xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta name=Title content="">
<meta name=Keywords content="">
<meta http-equiv=Content-Type content="text/html; charset=macintosh">
<meta name=ProgId content=Word.Document>
<meta name=Generator content="Microsoft Word 15">
<meta name=Originator content="Microsoft Word 15">
<link rel=File-List href="test.fld/filelist.xml">
<!--[if gte mso 9]><xml>
 <o:DocumentProperties>
```

This file is 766 lines long!  Now, one can argue that the vast majority of this source is enclosed in the `head` portion of the document - the `body` portion is only a few lines long.  However, if we try something simple like this table:
<table>
<tr><td>A</td><td>1</td></tr>
<tr><td>B</td><td>2</td></tr>
<tr><td>C</td><td>3</td></tr>
</table>
in Word, we get an enormous wall of source in the `body` of the document - here are the first 10 lines of about fifty:

```html
<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width=130
 style='width:130.0pt;border-collapse:collapse;mso-yfti-tbllook:1184;
 mso-padding-alt:0in 5.4pt 0in 5.4pt'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:16.0pt'>
  <td width=65 nowrap valign=bottom style='width:65.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:16.0pt'>
  <p class=MsoNormal><span style='mso-ascii-font-family:Calibri;mso-fareast-font-family:
  "Times New Roman";mso-hansi-font-family:Calibri;mso-bidi-font-family:"Times New Roman";
  color:black'>A<o:p></o:p></span></p>
  </td>
```

Source generated by online web hosting services are no better.  Here's a nice snippet from a website hosted on WordPress:

```html
<div class="c-largeScreenSearch__icon__wrapper">
<span class="c-largeScreenSearch__helper"><svg xmlns="http://www.w3.org/2000/svg" width="54"
height="20" viewBox="0 0 54 20"><path fill="#BCBCBC"
fill-rule="evenodd"                                                                                                         d="M1223.43929,48.228 C1225.49545,48.228 1226.61463,47.2649863 1226.61463,44.9745753
L1226.61463,44.0636164 C1226.61463,41.6951233 1225.75573,40.2115616 1224.55847,37.5567671 C1223.33518,34.8759452
1222.94477,34.2252603 1222.94477,32.7156712 L1222.94477,32.2732055 C1222.94477,31.5704658 1223.12696,31.3362192
1223.49134,31.3362192 C1223.85573,31.3362192 1224.03792,31.5444384 1224.03792,32.1690959 L1224.03792,33.7047123
L1226.51052,33.7047123 L1226.51052,32.1690959 C1226.51052,30.2430685 1225.52148,29.228 1223.51737,29.228 C1221.48723,29.228
1220.39408,30.2430685 1220.39408,32.3773151 L1220.39408,32.8458082 C1220.39408,35.1101918 1221.12285,36.4115616
1222.29408,39.0143014 C1223.5434,41.6951233 
```

and source generated by dynamic web frameworks such as Ruby on Rails or Django can be even worse:

```html
<div class="container_1tvwao0" data-reactid="97"><div class="container_mv0xzc" style="width:33.3333%;" data-reactid="98"><!-- react-text: 99 --><!-- /react-text --><button type="button" class="button_1b5aaxl" data-reactid="100"><span class="icon_12hl23n" data-reactid="101"><svg viewBox="0 0 24 24" role="presentation" aria-hidden="true" focusable="false" style="display:block;fill:currentColor;height:18px;width:18px;" data-reactid="102"><path fill-rule="nonzero" d="M3.83 9.4a7.75 7.75 0 1 0 15.342 2.198A7.75 7.75 0 0 0 3.83 9.401zm16.825 2.412A9.25 9.25 0 1 1 2.343 9.186a9.25 9.25 0 0 1 18.312 2.626zM16.97 18.03a.75.75 0 0 1 1.06-1.06l5 5a.75.75 0 0 1-1.06 1.06" data-reactid="103"></path></svg></span><span class="copy_14aozyc" data-reactid="104"><span data-reactid="105">Anywhere</span></span></button><div class="focusUnderline_7131v4" data-reactid="106"></div></div><div class="container_mv0xzc-o_O-borderLeft_1ujj4hk-o_O-borderRight_1x9yfnn" style="width:33.3333%;" data-reactid="107"><!-- react-text: 108 --><!-- /react-text --><button type="button" class="button_1b5aaxl" data-reactid="109"><span class="icon_12hl23n" data-reactid="110"><svg viewBox="0 0 24 24" role="presentation" aria-hidden="true" focusable="false" style="display:block;fill:currentColor;height:18px;width:18px;" data-reactid="111"><path d="M22 9.5V3h-4.75V1a.75.75 0 1 0-1.5 0v2H8.249l.001-2a.75.75 0 1 0-1.5 0l-.001 2H2v19.008a1 1 0 0 0 .992.992h18.016a1 1 0 0 0 .992-.992V9.5zm-18.5-5h3.248V5a.75.75 0 0 0 1.5 0v-.5h7.502V5a.75.75 0 0 0 1.5 0v-.5h3.25V8h-17V4.5zm0 17v-12h17v12h-17z" fill-rule="evenodd" data-reactid="112"></path></svg></span>
```

Again, you can argue that this is unfair because I am zeroing in on graphic or layout-based elements.  However, in most cases we are grappling with a wall of text that comprises all kinds of elements, where it is extremely difficult to orient yourself to retrieve specific pieces of information.  This is why Python modules like BeautifulSoup have become necessary.  


## Parsing HTML with BeautifulSoup

Let's get back to business.  So far, we've learned about loading a web page in Python.  Instead of mucking about with the university homepage, let's try to work with something a bit more useful.  Here is a website from the Public Health Agency of Canada that reports the leading causes of death in 2008:
```python
>>> from urllib import request
>>> response = request.urlopen('http://www.phac-aspc.gc.ca/publicat/lcd-pcd97/table1-eng.php')
>>> src = response.read()
```
If I copy-and-paste the contents of the table into a plain-text editor, the result is not very useful; here is an excerpt:
```
1st	Perinatal
1,092
(292.7)	Unintentional injuries
55
(3.8) Table 1 Footnote •	Unintentional injuries
70
(3.9) Table 1 Footnote •	Unintentional injuries
```
You can actually get a bit further by pasting this particular table into Excel, but there are embedded hyperlinks that causes problems and this is a course on bioinformatics, so we're going to learn how to do this for real.  Let's bring in bs4.  
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
We got a slap on the wrist!  What happened?  Actually, this wasn't an error, it was a warning.  BeautifulSoup is able to use one of several approaches to convert HTML code into more convenient objects in Python.  

So what did we just assign to our `soup` variable?
```python
>>> type(soup)
<class 'bs4.BeautifulSoup'>
```
Well, it's an instance of a module-specific class that does a *lot* of things.  We don't have the time to work through all of these, so let's focus on just a few functions of this class.  

If you type `soup` by itself, then Python will display the entire HTML source on the console, but you might as well open the webpage in a browser and view the source there.  What we are looking for is a `<table>` element to extract from this source.  This is a good point to introduce BeautifulSoup's `findAll` function, which searches through the HTML for tags that match a string argument.  (From now on, let's refer to BeautifulSoup as `bs4` for short.)  We want to look for `<table>` tags:
```python
>>> tables = soup.findAll('table')
>>> len(tables)  # BS found exactly one table in the HTML source
1
```
`findAll` returns a Python list.  If it doesn't find any tag matching our argument, then it returns an empty list:
```python
>>> soup.findAll('puppies')
[]
```
Of course, `<puppies>` is not a recognized HTML tag (and sadly will likely never be).


### Tables *again*?
Now we need to parse the contents of this table.  Parsing a `bs4` table is much like [parsing a tabular data set](TabularData.md) from text, but some of the work has already been done for us -- each row is enclosed in table row tags `<tr>` and each element within a row is enclosed in table data tags `<td>`.  For example, here is a very small table in HTML:
```html
<table>
  <tr>
    <td>Breakfast</td>
    <td>A waffle and sausages</td>
  </tr>
  <tr>
    <td>Lunch</td>
    <td>Watermelon and ice coffee</td>
  </tr>
  <tr>
    <td>Dinner</td>
    <td>Lamb skewers</td>
  </tr>
</table>
<!-- Yeah.  That's what I ate today. -->
```
and here is what the table looks like rendered in a web browser:
<table><tr><td>Breakfast</td><td>A waffle and sausages</td></tr><tr><td>Lunch</td><td>Watermelon and ice coffee</td></tr><tr><td>Dinner</td><td>Lamb skewers</td></tr></table>
(Assuming you're actually viewing this in a web browser.  Just in case you aren't, I've removed the line breaks to minimize annoyance.)

Let's write a function in Python that will extract the text from a table encoded by a `bs4` object:
```python
def soup2table(element):
    """ A simple function for extracting text from an HTML table in BeautifulSoup """
    for row in element.findAll('tr'):
        data = row.findAll('td')
        yield ([datum.text for datum in data])  # use list comprehension
```
What's going on here?  First, I am iterating over every table row (`tr`) element in the table by using `findAll` to generate an iterable list of rows.  Next, I'm using the same function to generate a list of table data (`td`) elements in a given row.  Finally, I am accessing the `text` attribute of each `td` element in the list that I assigned to `data`, and  using Python list comprehension to assign the results into a new list.  As a result, this `soup2table` is a generating function that should return each row in the table without storing the entire content of the table in memory.

Let's look at the first few rows:
```python
>>> for result in soup2table(tables[0]):
...   print(result)
... 
[]
['Table 1 Footnotes\n\nFootnote *\n\nSuppressed due to small number of cases or value of zero.\n\nFootnote •\n\nUnintentional injuries\n\nFootnote †\n\nSuicide\n\nFootnote ‡\n\nHomicide\n\n\nSource: Injury Section analysis of mortality data from Statistics Canada.']
['1st', 'Perinatal\r\n        1,092\r\n        (292.7)', 'Unintentional injuries\r\n        55\r\n        (3.8) Table 1 Footnote •', 'Unintentional injuries\r\n        70\r\n        (3.9) Table 1 Footnote •', 'Unintentional injuries\r\n        80\r\n        (4.0) Table 1 Footnote •', 'Unintentional injuries\r\n        397\r\n        (17.6) Table 1 Footnote •', 'Unintentional injuries\r\n        513\r\n        (22.4) Table 1 Footnote •', 'Unintentional injuries\r\n        791\r\n        (17.6) Table 1 Footnote •', 'Cancer\r\n        1,370\r\n        (28.1)', 'Cancer\r\n        5,636\r\n        (106.8)', 'Cancer\r\n        12,244\r\n        (309.2)', 'Circulatory system diseases\r\n        60,280\r\n        (1,322.8)', 'Cancer\r\n        71,948\r\n        (215.9)']
```
The first two rows that we've parsed from the `bs4` table object don't conform to the structure of the table, which should have 13 columns.  Let's add an `if` statement to exclude these rows:
```python
for result in soup2table(tables[0]):
    if len(result) < 13:
        continue  # go to next row
```


### Text processing
Now we can start dealing with the text within each `td` element.  I can see that there are generally two Windows-style line breaks and extraneous whitespace within most elements separating useful items:
```python
'Perinatal\r\n        1,092\r\n        (292.7)'
```
Let's break these strings up into three substrings.  From viewing the table online, I know that these items correspond to:
1. a specific cause of death,
2. the number of cases in Canada in 2008, and 
3. the age-specific death rate by that cause per 100,000.  
However, we need to be careful about how we split these strings up.  We need to split on whitespace, but some entries contain spaces that we need to leave intact; for example:
```python
'Circulatory system diseases\r\n        60,280\r\n        (1,322.8)'
```
and other entries contain extra items that we want to exclude:
```python
'Unintentional injuries\r\n        55\r\n        (3.8) Table 1 Footnote •'
```
or non-standard characters, like this entry:
```python
'Endocrine,\r\n        nutr.\xa0& metab. diseases\r\n        12\r\n        (0.8)'
```
where `\xa0` is a special character encoding that represents a non-breaking space.  

This is getting complicated, so I decide to bring in regular expressions:
```python
import re
pat = re.compile("^([A-Za-z,\s.]+)([0-9]+)\s+\(([0-9]+\.[0-9]+)\)$")
```
This is a beastly regex!  With this expression, I am attempting to capture three groups, where the first group contains all alphabet and whitespace characters at the start of the string, the second group contains some integer, and the third group is a floating point number enclosed in round brackets.  

My complete scraping script looks like this:
```python
from urllib import request
from bs4 import BeautifulSoup
import re

def soup2table(element):
    """ A simple function for extracting text from an HTML table in BeautifulSoup """
    for row in element.findAll('tr'):
        data = row.findAll('td')
        yield ([datum.text for datum in data])  # use list comprehension
        

# regex to extract content from <td> elements
pat = re.compile("^([A-Za-z,\s.\&]+)([0-9,]+)\s+\(([0-9,]+\.[0-9]+)\)")
pat2 = re.compile("^([A-Za-z,\s.\&]+)Table")

def get_data(txt):
    """ Extract items from the text field of a <td> element """
    # replace non-breaking space with a regular one
    txt = txt.replace(u'\xa0', ' ')
    
    # apply regex
    matches = pat.findall(txt)
    if not matches:
        # some entries contain a footnote instead of count/rate data
        matches = pat2.findall(txt)
        if not matches:
            return None, None, None
        cause = re.sub("\s+", '', matches[0])
        return cause, None, None
        
    cause, count, rate = matches[0]
    
    cause = re.sub("\s+", ' ', cause)  # remove extra whitespace
    count = int(count.replace(',', ''))  # convert 1,000 to 1000
    rate = float(rate.replace(',', ''))
    
    return cause, count, rate


response = request.urlopen('http://www.phac-aspc.gc.ca/publicat/lcd-pcd97/table1-eng.php')
src = response.read()
soup = BeautifulSoup(src, 'html.parser')

tables = soup.findAll('table')

# store the results as a list
results = []

for row in soup2table(tables[0]):
    if len(row) < 13:
        continue  # go to next row
        
    rank = row[0]  # e.g., "1st"
    result = [get_data(txt) for txt in row[1:]]
    results.append(result)
        
print (results)
```
To save you some typing, I've uploaded this script to this repo as `scraper.py`.

## What's going on?
Let's go through this script one section at a time to explain what's going on.

```python
from urllib import request
from bs4 import BeautifulSoup
import re
```
Here we are importing three modules:
1. `request` is a submodule of `urllib` that handles HTTP requests from a specific URL.  
2. `BeautifulSoup` is a class in the `bs4` module that parses HTML source into a tree-like data structure.
3. `re` is Python's regular expressions module.



### Tree data structures

```python
def soup2table(element):
    for row in element.findAll('tr'):
        data = row.findAll('td')
        yield ([datum.text for datum in data])
```
This code declares a function in Python called `soup2table` that takes a single argument.  It assumes that the argument is some type of `bs4` object that has a defined `findAll` function.  We're being sloppy so we're not bothering to check that this is true.  Hopefully you got the general idea of how this function works from the previous section of this Markdown document.  However, to really get a concrete understanding of what's going on, we need to talk about how `bs4` converts HTML source into a set of objects that are arranged in a tree-like data structure.  

The result of parsing the byte string that contains the HTML source is a nested or hierarchical (tree-like) data structure.  An HTML document necessarily has a hierarchical structure.  The `<html>` tags enclose the entire document, which splits from this main trunk into two major branches enclosed by `<head>` and `<body>`.  As we've seen above, a table is organized into a hierarchy of HTML tags, with `<table>` tags at its root, `<tr>` tags defining the first level of splits into rows, and `<td>` tags defining a second level of splits within each row. 

Why does it matter that this document is hierarchical?  When we loop over the list returned by calling `findAll` on a `tr` element, we don't end up with *all* the `td` elements in the document - we only get the `td` that are "children" of the specific `tr` we are working with at a given iteration of the outer loop.  

Note that we have two loops in this function.  This is the loop that I just referred to as the outer loop:
```python
for row in element.findAll('tr'):
```
and list comprehension contains the inner loop:
```python
yield ([datum.text for datum in data])
```
I'm calling it the inner loop because it is nested within the outer loop.  We have to complete iterating over the inner loop before we can proceed to the next iteration of the outer loop.  Put another way, think of these nested loops as the "hours" and "minutes" hands of a clock.  Or moons.

![](https://imgs.xkcd.com/comics/galilean_moons.png)


### Regular expressions!
```python
pat = re.compile("^([A-Za-z,\s.\&]+)([0-9,]+)\s+\(([0-9,]+\.[0-9]+)\)")
pat2 = re.compile("^([A-Za-z,\s.\&]+)Table")
```
As I said before, these are brutal-looking regexes (shorthand for regular expressions).  Let's work through the first regex one group at a time, which should give you the concepts you need to understand how the second regex works.

The first group captures all substrings that contain upper- and lowercase letters (`A-Za-z`), commas `,`, any form of whitespace (including spaces, tabs and line breaks), periods `.` and ampersands `&`.  (Reminder: because `.` is used within a character set definition - enclosed in square brackets - it is taken literally and does not represent any character.)  I built up this group by looking over the text fields corresponding to causes of death in the HTML source, and using trial and error until I was able to capture all values in this field.

The second group captures all integers including commas, which are commonly used as the thousands separator - *e.g.*, `1,789`.  Between the second and third groups, our regex has to accommodate some whitespace - this is accomplished with the pattern `\s+`.  Finally, we know that the third group should be a floating point number enclosed in round parentheses.  We escape the first set of parentheses using the notation `\(` and `\)` and then capture floating point numbers with this pattern: `[0-9,]+\.[0-9]+`, where we are allowing for thousands separators in the integer part of the number.  Since the decimal separator `.` is not contained in a character set, we have to escape it with `\.`.  

### Exception handling

My regex is far from perfect, partly because these are noisy strings that we scraped from a website and contain non-standard characters.  Fortunately there is only one such character `\xa0` which encodes a non-breaking space.  Instead of attempting to accommodate this character in my regex, I'm just going to delete it from the string:
```python
txt = txt.replace(u'\xa0', ' ')
```
Note that I've added a `u` prefix to the first argument of my string `replace` function call.  This tells Python to interpret the argument as Unicode.  

```python
    matches = pat.findall(txt)
    if not matches:
        # some entries contain a footnote instead of count/rate data
        matches = pat2.findall(txt)
        if not matches:
            return None, None, None
        cause = re.sub("\s+", '', matches[0])
        return cause, None, None
```
If my regex fails to match the string contained in the `txt` argument, then `pat.findall` returns an empty list that is assigned to my `matches` variable.  I check if `matches` is an empty list with the condition `not matches`.  An important feature of Python objects is that they can be used directly for logical tests:
```python
>>> bool(2)
True
>>> bool(not 2)
False
>>> bool(-2)  # maybe counter-intuitive!
True
>>> bool(not -2)
False
>>> bool(0)
False
>>> bool(not 0)
True
>>> bool([])
False
>>> bool(not [])  # this is my test
True
```

If this test returns a `True`, then I know that my first regex failed.  While writing this script, I printed out these exceptions to the console to get an idea of what's going on:
```python
if not matches:
    print (txt)
```
This modifications coughs up the following text:
```
Perinatal Table 1 Footnote *
Infectious & parasitic diseases Table 1 Footnote *
```
These strings don't contain any count or frequency data, but we still want to capture the "cause of death" value, so I wrote a second regex `"^([A-Za-z,\s.\&]+)Table"` that exploits the appearance of the substring `Table` in both cases to mark the end of the "cause of death" field.

What if this second regex doesn't work?  Then we want to follow up with some default return values, which in this case I set to the `None` object:
```python
        matches = pat2.findall(txt)
        if not matches:
            return None, None, None
        cause = re.sub("\s+", '', matches[0])
        return cause, None, None
```


### String operations

```python
    cause, count, rate = matches[0]
    
    cause = re.sub("\s+", ' ', cause)  # remove extra whitespace
    count = int(count.replace(',', ''))  # convert 1,000 to 1000
    rate = float(rate.replace(',', ''))
```
If we have a successful match from the first regex, then we can assign the captured groups as strings to three variables:
* `cause` - the cause of death
* `count` - the number of cases in a given year
* `rate` - the incidence of cases per 100,000 

One of the first issues we need to deal with is that some of the `cause` values *still* contain extra line breaks and whitespace; for example:
```
Endocrine,\r\n        nutr.  metab. diseases\r\n        
```
I'm using the `re.sub` function to match any sequence of whitespace characters and replace every occurrence with a single space:
```python
cause = re.sub("\s+", ' ', cause)
```

In the other two statements, I am removing any commas before casting the string as integer or floating point numbers, respectively.


### Web server transactions

```python
response = request.urlopen('http://www.phac-aspc.gc.ca/publicat/lcd-pcd97/table1-eng.php')
src = response.read()
soup = BeautifulSoup(src, 'html.parser')
```
`request.urlopen` sends an HTTP request to the webserver at the URL `http://www.phac-aspc.gc.ca`, asking for a PHP document.  PHP is yet *another* scripting language that specializes in dynamically generating HTML source from the content of a database in response to an HTTP request.  

![](https://imgs.xkcd.com/comics/server_attention_span.png)

> What do I mean by *dynamic*?  Suppose that we need to make a webpage that displays a list of classes offered by a university department.  I could write an HTML source file including this list.  However, if any of the classes was changed, such as a class that is no longer offered, a new class, or a class with a new course number, then I'd have to go in and manually revise my HTML source file.  No one does it this way anymore - most institutions have a [database](https://en.wikipedia.org/wiki/Database) that tracks information about courses and then use some server-side scripting language like PHP to query the database for the pertinent information whenever someone requests the webpage.  This means that the content of the webpage will change along with the database.  More importantly for developers, it means that we can work with a single centralized database, instead of manually maintaining potentially hundreds of HTML source files.

The HTTP response from the server is captured in a special object defined by the `request` submodule and assigned to the variable `response`.  This object has a number of special functions including `read`, which we use to stream its content as a byte string to a variable we call `src`.  Finally, we construct an instance of the `BeautifulSoup` class using this byte stream as the first argument, and the option `html.parser` as the second argument.  We are expected to set the second argument because there is potentially more than one parser available on your system, and `bs4` doesn't want to have to guess which one you want to use.

