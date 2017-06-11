# Scraping

## What is scraping?

[Scraping](https://en.wikipedia.org/wiki/Data_scraping) is a technique that enables a computer to extract information from a source that is not meant to be readily processed by a computer, such as a scanned image.  You can think of scraping as parsing on steroids.  Up till now, we've talked a lot of about parsing as a fundamental tool in bioinformatics, where we read data from a file that is in a standard format.  We can even use regular expressions to repair broken formats.  However, if there is *no* standard format, then things get more challenging!  [Web scraping](https://en.wikipedia.org/wiki/Web_scraping) is used to describe the scenario where scraping is applied to web content.  This is typically an HTML page that has been transmitted from the server to your web browser, which "knows" how to interpret that HTML to render the page contents on your screen.  

There are now a *lot* of data resources online for biological and biomedical research.  [Genbank] is one of the oldest such resources and has been open access for decades, with a sophisticated interface and the ability to download massive data sets.  However, not all online resources are as accessible, either because they do not have the assets (*e.g., webservers, bandwidth) to handle large data transactions - this takes a lot of money! - or because they have some reason for limiting access to data.  These limits can be imposed by paginating the results from a database query (in other words, displaying a large number of results one page at a time, requiring you to follow links through successive pages).  The user is not able to download the results into a local file.  In other cases, access to the database is limited to users with an account on the server, which may have to be arranged with the database curators.  

It is common for users to painstakingly copy-and-paste information from a webpage into a text editor or word processor.  This can be extremely time-consuming!  In some situations, web scraping offers a way to circumvent the limitations set by the database website and automatically extract the entire contents of a database query with a scripting language like Python.  

## Scraping etiquette

Before we get into some of the techniques of web scraping, we should recognize that this is generally not a nice thing to do to a website, especially if we get it wrong.  Remember, computers are both extremely fast and extremely stupid.  If you tell your computer to go to a webpage, grab all its contents, follow a link to the next page and repeat, then the computer will do exactly that *very, very fast*.  This is essentially the same as launching a [denial of service attack](https://en.wikipedia.org/wiki/Denial-of-service_attack) on the remote server - you're sending multiple (potentially hundreds) of page requests to the server in the span of milliseconds.  

There are some "best practices" recommendations that have emerged in the developer community around the etiquette of web scraping.  For example, some recommend checking the website's `robots.txt` file, more formally known as the [robots exclusion protocol](https://en.wikipedia.org/wiki/Robots_exclusion_standard), which contains a set of instructions for automated web crawlers that index web sites for search engines such as Google.  You can read more about such recommendations in this [StackOverflow thread](https://stackoverflow.com/questions/2022030/web-scraping-etiquette).

In my opinion, one thing that you should *absolutely* make sure is part of your scraping script is to build in some sort of time delay between requests.  This will help prevent your computer from firehoseing requests at the remote server.  You should also be careful when implementing and testing your script to make sure that it is working correctly before letting it loose in the wild.  If you *don't* take such steps, then you risk having your IP address blocked by the web server (or even worse, an entire IP address range that may affect your entire university!).  

To throttle down your Python script, you can make use of the `sleep` function that's available in the `time` module:
```python
>>> import time
>>> time.sleep(10)  # waits for ten seconds
```

You should also check whether the website has a [web API](https://en.wikipedia.org/wiki/Web_API) (application programming interface), which provides a set of tools for automating (scripting) transactions with its database.  For example, NCBI has a web API that you can read more about [here].  It's generally good etiquette to use the website API instead of scraping.


## Web browsing with Python

In order to scrape web content, we first need to get Python to browse the web.  


