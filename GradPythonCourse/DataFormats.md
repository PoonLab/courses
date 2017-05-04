# Bioinformatic data formats

## Binary and text files
First, let's draw a distinction between plain text and binary files.  All files correspond to a series of 1's and 0's on the hard drive or in memory.  A plain text file has a flag that tells the computer that it should apply a [character encoding](https://en.wikipedia.org/wiki/Character_encoding) that maps binary sequences (bit strings) to symbols, such as characters in an alphabet.  For example, the [ASCII](https://en.wikipedia.org/wiki/ASCII) encoding maps the bit string `1001010` to the letter `J`.  This means that when you open the file, the computer knows that it should display its contents as a collection of meaningful characters.  Obviously this is a big advantage for making a file immediately interpretable.  However, we sacrifice some efficiency to make this possible, so binary files tend to be more compact while storing the same information. 

For a plain text file, a format is a set of rules about how the characters are arranged to encode information.  Data formats are a necessary evil in bioinformatics.  Learning to parse new formats and converting between formats is a ubiquitous task that is often made more difficult by the lack of a strict standardization for popular formats such as [NEXUS](https://en.wikipedia.org/wiki/Nexus_file) or [Newick](https://en.wikipedia.org/wiki/Newick_format).  Fortunately, the pervasiveness of such tasks means that there are also plenty of resources in the public domain that make them easier to accomplish.

## Tabular data

Tabular data formats are probably the most common format for storing conventional data types.  A table is made up of rows and columns like a [spreadsheet](https://en.wikipedia.org/wiki/Spreadsheet).  Table rows (by convention) represent independent observations/records, such as a sample of patients, and columns represent different kinds of measurements (variables) such as height and weight.  For example:

| agegp |    alcgp |   tobgp  |ncases |ncontrols |
|-------|----------|----------|-------|----------|
| 25-34 |    40-79 |   20-29  |    0  |       4 |
| 35-44 |   80-119 |   20-29  |    0  |       2 |
| 45-54 |0-39g/day | 0-9g/day |     1  |      46 |
| 55-64 |     120+ |   20-29  |    2   |      3 |
| 25-34 |     120+ |   20-29  |    0   |      1 |
|   75+ |     120+ |   10-19  |    1   |      1 |
| 25-34 |   80-119 |   10-19  |    0   |      1 |
| 55-64 |    40-79 |     30+  |    3   |      6 |
| 25-34 |0-39g/day |   10-19  |    0   |     10 |
| 55-64 |0-39g/day |     30+  |    4   |      6 | 

These data come from the `esoph` dataset in [R](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/00Index.html).  

Since the table rows appear in different lines, then 


