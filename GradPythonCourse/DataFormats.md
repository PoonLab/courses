# Bioinformatic data formats

## Binary and text files
First, let's draw a distinction between plain text and binary files.  All files correspond to a series of 1's and 0's on the hard drive or in memory.  A plain text file has a flag that tells the computer that it should apply a [character encoding](https://en.wikipedia.org/wiki/Character_encoding) that maps binary sequences (bit strings) to symbols, such as characters in an alphabet.  For example, the [ASCII](https://en.wikipedia.org/wiki/ASCII) encoding maps the bit string `1001010` to the letter `J`.  This means that when you open the file, the computer knows that it should display its contents as a collection of meaningful characters.  Obviously this is a big advantage for making a file immediately interpretable.  However, we sacrifice some efficiency to make this possible, so binary files tend to be more compact while storing the same information. 

For a plain text file, a format is a set of rules about how the characters are arranged to encode information.  Data formats are a necessary evil in bioinformatics.  Learning to parse new formats and converting between formats is a ubiquitous task that is often made more difficult by the lack of a strict standardization for popular formats such as [NEXUS](https://en.wikipedia.org/wiki/Nexus_file) or [Newick](https://en.wikipedia.org/wiki/Newick_format).  Fortunately, the pervasiveness of such tasks means that there are also plenty of resources in the public domain that make them easier to accomplish.

## Tabular data

Tabular data formats are probably the most common format for storing conventional data types.  A table is made up of rows and columns like a [spreadsheet](https://en.wikipedia.org/wiki/Spreadsheet).  Table rows (by convention) represent independent observations/records, such as a sample of patients, and columns represent different kinds of measurements (variables) such as height and weight.  For example:

|agegp |alcgp  |tobgp    | ncases| ncontrols|
|:-----|:------|:--------|------:|---------:|
|75+   |40-79  |0-9g/day |      2|         5|
|75+   |40-79  |10-19    |      1|         3|
|35-44 |80-119 |10-19    |      0|         6|
|65-74 |80-119 |10-19    |      4|        12|
|55-64 |40-79  |30+      |      3|         6|
|45-54 |120+   |10-19    |      3|         4|
|55-64 |120+   |20-29    |      2|         3|
|25-34 |80-119 |30+      |      0|         2|
|55-64 |40-79  |20-29    |      4|        17|
|55-64 |80-119 |10-19    |      8|        15|

These data come from the `esoph` dataset in [R](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/00Index.html). For what it's worth, to extract this subsample I used the following command in R:
```R
kable(esoph[sample(1:nrow(esoph), 10),], format='markdown', row.names=F)
```
These are aggregate data from a case-control study of esophageal cancer in France.  If you're interested about the study, you can read more about it in the source reference: [Brewlow and Day 1980](https://www.iarc.fr/en/publications/pdfs-online/stat/sp32/).  

How do we record this information in a plain text file?  Typically, we preserve the row structure of the table by placing line breaks between each row.  A [line break](https://en.wikipedia.org/wiki/Newline) is a special character encoding that tells the computer to move to a new line when displaying the content of a text file.  Different operating systems use [different control characters](https://en.wikipedia.org/wiki/Newline#Representations) in the ASCII encoding set to represent a line break: UNIX and its descendants use `LF` (line feed); Apple computers used `CR` (carriage return) until the OS became a UNIX-like system; and Microsoft Windows uses a combination of `LF` and `CR`.  This frequently causes problems when passing data files originating from different computers between programs that were developed on different platforms!  If you are trying to process a data file with a program and it isn't working, this is a possible cause.

We still have to deal with preserving the column structure of a tabular data set.  This is usually accomplished with a [delimiter](https://en.wikipedia.org/wiki/Delimiter): a character or sequence of characters that is used to separate content that belongs to different items.  The comma `,` is probably the most common delimiter, closely followed (if not surpassed) by the [tab character](https://en.wikipedia.org/wiki/Tab_key#Tab_characters), which is represented by the escape character `\t`.  To illustrate, here is how our `esoph` data would appear in a comma-separated values (CSV) file:
```
agegp,alcgp,tobgp,ncases,ncontrols
75+,40-79,0-9g/day,2,5
75+,40-79,10-19,1,3
35-44,80-119,10-19,0,6
65-74,80-119,10-19,4,12
55-64,40-79,30+,3,6
45-54,120+,10-19,3,4
55-64,120+,20-29,2,3
25-34,80-119,30+,0,2
55-64,40-79,20-29,4,17
55-64,80-119,10-19,8,15
```

and here is the same data set as a tab-separated values (TSV) file:
```
agegp	alcgp	tobgp	ncases	ncontrols
75+	40-79	0-9g/day	2	5
75+	40-79	10-19	1	3
35-44	80-119	10-19	0	6
65-74	80-119	10-19	4	12
55-64	40-79	30+	3	6
45-54	120+	10-19	3	4
55-64	120+	20-29	2	3
25-34	80-119	30+	0	2
55-64	40-79	20-29	4	17
55-64	80-119	10-19	8	15
```

An important feature of these formats is that the first line is being used to store the column labels.  This is often referred to as the *header row*.  Including the header row is optional in a CSV or TSV file, but it is important to be aware of whether it is present or absent when you are processing the file.  

A tabular data file should have the same number of items on each line.  If a line has more items than another, then the assignment of items to the various columns becomes ambiguous (especially if the data are similar types, such as a large set of numbers).  In other words, did we append an extra number to the left, or the right, or some where in the middle?  

What happens if our data includes entries that contain the delimiter?  For example, suppose that our data set includes text fields that contain a description of symptoms, such as: `muscular pain, acute`.  This creates the exact problem that we just described!  Fortunately, this format is so widely used, and this problem so common, that there is a standardized solution: we enclose the affected item in double quotes.  In other words, this row:
```
67,muscular pain, acute,Toronto
```
becomes this:
```
67,"muscular pain, acute",Toronto
```

## Working with tabular data in Python
