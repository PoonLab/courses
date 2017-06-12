# Date and time objects in Python

## Dates are difficult

Dates are difficult.  A year is a fairly well-defined period of time (the duration of the Earth's rotation around the sun) and a day is also well-defined (rotation of the Earth around its axis), but there are different schemes for partitioning the year into months and days, such as the [Gregorian](https://en.wikipedia.org/wiki/Gregorian_calendar) and various [lunar](https://en.wikipedia.org/wiki/Lunar_calendar) calendars.  Calendars are imperfect because days must be integer valued, but there is a non-integer number of days in an Earth year (about 365.2422).  This means that even the [leap-year](https://en.wikipedia.org/wiki/Leap_year) adjustment is imperfect.  It also means that what seems like a relatively simple question for a computer -- what day of the week was it one million days ago? --- is not trivial to answer.  

Dates are also difficult because there are many ways of writing them down.  For example, January 1, 1970 is a date known as the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time), which is as good an arbitrary point of reference as [any other](https://en.wikipedia.org/wiki/Anno_Domini).  Here are various string representations of the UNIX epoch:
* 1970-01-01
* 01/01/1970
* Jan 1, 1970
* 70/01/01

There are several issues that arise here.  First, month and day numbering are easily confused.  Does `70/01/02` mean the first day of February or the second day of January?  Even worse, if only the last two digits of the year are given then all three values (days, months, and years) can be confounded!  Second, different representations can be used inconsistently.  For example, NCBI Genbank records have a field for annotating sequences with the sample collection date, but I've seen several different date formats used among records.  I try to use the ISO format whenever possible (YYYY-MM-DD).

![](https://imgs.xkcd.com/comics/iso_8601.png)

Dates matter in bioinformatics.  They are a good example of a complex and structured data type.  When we're dealing with longitudinal clinical data, we need to be able to extract dates from records that may be recorded in different formats.  Parsing sample collection dates from sequence data enable us to use evolutionary models to reconstruct the historical dynamics of a disease outbreak.  

Fortunately, Python has multiple modules to deal with several of these issues.  The first one we'll talk about is `datetime`.  
## The `datetime` module

The `datetime` module defines several classes (a class is a type of object; a list is a basic class of object in Python).  We'll start with the `date` class:
```python
>>> from datetime import date
>>> date.today()
datetime.date(2017, 5, 31)
>>> birth_date = date(2000, 3, 10)  # create an arbitrary date object
>>> diff = date.today() - birth_date
>>> diff
datetime.timedelta(6291)
>>> diff.days  # a simpler integer answer
6291
```
The `datetime.date` object is a generic representation for calendar dates.  Our objective is to convert string representations of dates into these objects.  This object has a number of functions and attributes, some of which are common to all instances of `datetime.date`:
```python
>>> birth_date.min  # this a read-only attribute
datetime.date(1, 1, 1)
>>> birth_date.max  # in a few millenia, we'd better have a new version of Python :)
datetime.date(9999, 12, 31)
>>> birth_date.ctime()  # C-style representation of date
'Fri Mar 10 00:00:00 2000'
>>> birth_date.toordinal()  # number of days since UNIX epoch
730189
>>> birth_date.isoformat()  # yay!
'2000-03-10'
```

