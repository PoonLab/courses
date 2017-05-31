# Regular expressions

A regular expression is a representation of a subset of all possible strings, called a *pattern*.  The concept of regular expressions originates from linguistics, particularly the field of computational linguistics (natural language processing), the study of breaking a language down into a strict (formal) set of rules that can be encoded for a machine.

Regular expressions (or *regex*es, for short) are extremely useful when you are dealing with text-based data sets.  We can screen a set of strings for those that match the regex, capture parts of those strings, and then use those parts to rewrite the string.  It doesn't sound like much, but it is a big deal.  Unforunately, there are different kinds of regular expressions.  Python uses Perl-style regular expressions.

![](https://imgs.xkcd.com/comics/regular_expressions.png)

A regular expression is defined by inserting special characters into the string.  Many of these are characters that we would normally want to use for their original meaning, such as the round brackets `(` and `)`.  To tell Python that we want to use brackets in the "normal" way, we need to use the escape symbol `\` like we do for line breaks (`\n`):
```python
"\(like this\)"
```
Also note that *any* character can be used in a regular expression, such as spaces and punctuation marks.

To load the regular expressions module, type:
```python
>>> import re
```


## Defining character sets

A set of characters is defined by square brackets.  For example, `"c[aou]t"` matches `"cat"`, `"cot"` and `"cut"`, but not `"cet"`.  It also does not match `"bat"`, because the pattern expects the set to have a `'c'` on the  left and a `'t'` on the right.

Some times you want to specify a large range of characters in a set.  To save you the trouble of typing all of those characters in, regular expressions have a range syntax: `"[x-y]"` where `x` and `y` are the inclusive limits of the range.  For example, `"[a-z]"` is the subset of all lower case characters in the alphabet.  `"[0-9]"` is all the digits.

You can specify a partial range.  `"[A-C]"` matches `'A'`, `'B'`, and `'C'`, but not `'D'`.  You can also concatenate ranges.  For example, `"[A-CE-Z]"` is the upper case alphabet excluding D.  Finally, you can complement the set with the `^` symbol.  The pattern `[^D]` matches any character except `'D'`.  Python's regular expressions also assumes a specific order of characters.   The digits `0-9` precede `A-Z`, which in turn precede `a-z`.  This means that you can define a range that spans these intuitive sets.  For example: `"foo[5-HT-j]"` matches `"foo9"` and `"food"`, but not `"fooJ"` or `"foot"`.

There are also special characters that represent predefined character sets, so you don't have to write out all possible characters with the square bracket notation:

* `.` matches *any* character
* `\w` matches any character that is a letter or digit (alphanumeric characteres) or an underscore (`_`)
* `\d` matches any digit
* `\s` matches any whitespace character such as a tab (`\t`), space (` `) or linebreak (`\n`).

Note that when we are writing regular expression patterns, we are simply declaring a string.  This string defines a pattern under the rules of regular expressions.  We don't have to use double-quotes `"` for these strings; single-quotes `'` will serve just as well.  I'm not going to be consistent!


## Using patterns

Before we go on with defining patterns, we need to learn a bit about how to use them so that we can work through some examples.  There are generally two ways to use the `re` module.  First, you can directly call functions from the module:
```python
>>> dir(re)
['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_alphanum_bytes', '_alphanum_str', '_cache', '_cache_repl', '_compile', '_compile_repl', '_expand', '_locale', '_pattern_type', '_pickle', '_subx', 'compile', 'copyreg', 'error', 'escape', 'findall', 'finditer', 'fullmatch', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'sys', 'template']
```
For example, we can look for all substrings that match the pattern `"[A-Z]"`:
```python
>>> re.findall("[A-Z]", 'YaRo0w!')
['Y', 'R']
```
The `findall` function returned a list of all substrings (in this case, single characters) that matched the pattern.  This list can be assigned to a variable to be used later on.  If there are no matches, then it returns an empty list:
```python
>>> re.findall("[A-Z]", 'python?')
[]
```

Second, you can compile a pattern, which creates an `SRE_Pattern` object:
```python
>>> p = re.compile("[A-Z]")
```
This object has the many of the same functions as the `re` module itself:
```python
>>> set(dir(p)).intersection(dir(re))
{'sub', 'search', 'fullmatch', 'match', 'findall', '__doc__', 'finditer', 'subn', 'split'}
```
Indeed, it returns exactly the same results as our previous examples calling from `re`:
```python
>>> p.findall('YaRo0w!')
['Y', 'R']
>>> p.findall('python?')
[]
```
One difference is that we don't have to keep entering the pattern-defining string when calling this function.  A more important difference, however, is that Python doesn't have to keep compiling our regular expression pattern, which is a waste of computing time if we are running the same function many times.  For example, this script (don't bother copying this out):
```python
from time import time
import re

t0 = time()
for i in range(10000):
    matches = re.findall("[A-Z]", 'YaRo0w!')
t1 = time()

t2 = time()
p = re.compile("[A-Z]")
for i in range(10000):
    matches = p.findall('YaRo0w!')
t3 = time()

print('module {} seconds'.format(t1-t0))
print('compiled {} seconds'.format(t3-t2))
print('compiling is {} times faster'.format((t1-t0)/(t3-t2)))
```
This script produces the following result:
```shell
module 0.0111448764801 seconds
compiled 0.00501084327698 seconds
compiling is 2.22415187705 times faster
```
I would expect even greater speed gains with more complex regular expressions.

For now, `findall` is good enough to illustrate how various patterns work.  Later on, we'll cover some of the other functions, such as `match` and `sub`.


## Repeating characters and sets

Let's continue on with the `+` symbol.  This symbol is used to describe a regular expression where the preceding character can be repeated one or many times.  For example, `a+` can represent `a`, `aa`, or `aaaaaaa`.  This symbol will only affect the character immediately in front of it.  `ba+` matches `baa` but not `bbaa`.

This symbol is especially powerful when combined with character sets.  For example, `"[A-Z]+"` matches any substring combining upper case letters, of any length:
```python
>>> p = re.compile('[A-Z]+')
>>> p.findall('JACKET')
['JACKET']
>>> p.findall('pants')
[]
>>> p.findall('Tie')
['T']
```

If you want to include the possibility that there is *no* match, then you can use the `*` symbol.  For example:
```python
>>> p = re.compile('i[aon]*n')
>>> p.findall('in')
['in']
>>> p.findall('piaaaaaano')
['iaaaaaan']
```

You can also declare a pattern that expects a specific number or range of matches.  For example:
```python
>>> p = re.compile('[abc]{3}')
>>> p.findall(' abcbacbabca ')
['abc', 'bac', 'bab']
```
only returns matches that span 3 characters in the set `[abc]`.  This is different behaviour than:
```python
>>> p = re.compile('[abc]+')
>>> p.findall(' abcbacbabca ')
['abcbacbabca']
```
If you want to match a range of lengths, then you can use the `{m,n}` syntax:
```python
>>> p = re.compile('a{3,5}')
>>> p.findall('aa')
[]
>>> p.findall('aaa')
['aaa']
>>> p.findall('aaaaaaaa')
['aaaaa', 'aaa']
```
The range can contain zero:
```python
>>> p = re.compile('da{0,5}d')
>>> p.findall('daaad')
['daaad']
>>> p.findall('dd')
['dd']
```

Finally, the special case of `{0,1}` has its own symbol `?`, which means that the preceding character or set may or may not appear once in the pattern:
```python
>>> p = re.compile('to?ny')
>>> p.findall('tny')
['tny']
```
Note that this means we have to escape `?` if we mean the question mark, and not the 0/1 match:
```python
>>> p = re.compile('tony?')  # may or may not contain 'y'
>>> p.findall('anton?')
>>> p = re.compile('tony\?')  # literal question mark
>>> p.findall('anton?')
[]
>>> p.findall('antony?')
['tony?']
```
The same thing goes for every other special character we've covered.

Lastly, sometimes a pattern can't be defined by a single regular expression.  We can attempt to match more than one regular expression by concatenating expressions with the `|` operator:
```python
>>> p = re.compile("c[aeiou]t|d[iou]g")
>>> p.findall('cat')
['cat']
>>> p.findall('dog')
['dog']
>>> p.findall('cag')
[]
```

> **Exercise:** Try writing a regular expression pattern that matches Genbank accession numbers.  These are supposed to start with one or two upper case letters, and end with five or six digits.  For example, `JN398015` and `U15660` are permitted accession numbers, but `8AB801` and `CYY5018599` are not.


## Position

So far we've assumed that a substring matching our pattern can appear anywhere in the master string.  If we want to find substrings in a particular location in the string, then we need to be able to refer to the start and end of that string.  Thus, we have the special characters `^` and `$`, respectively.  Note that this is the second special usage of the character `^` - remember that this symbol is also used to invert the contents of a set.  For example, `"^[^a]` matches any string that does not start with an `'a'`.

Regular expressions become very powerful when you can make ambiguous or exact matches relative to the start or end of a string.  For example, suppose that we want to capture the last date in ISO format `YYYY-MM-DD` in a long line of text:
```python
>>> import re
>>> s = "AC109823_Uganda_C_2011-08-20_2012-09-02"
>>> pat = re.compile("[0-9-]+$")  # this will match the date at the end of the string
>>> pat.findall(s)
['2012-09-02']  
```

The `^` and `$` symbols are also useful when we want to make sure that there are no leading or trailing characters around our pattern:
```
>>> pat = re.compile("^[abc]+$")
>>> pat.findall('cababc')
['cababc']
>>> pat.findall('tcababc')
[]
>>> pat.findall('cababcz')
[]
```


## Capturing groups

A group in a regular expression is defined by enclosing characters in round parentheses:
```python
>>> pat = re.compile('f(o+)bar')
>>> pat.findall('foobar')
['oo']
>>> pat.findall('fooba')
[]
```
Something interesting is happening here.  The string has to match our entire pattern in order to be considered a match; this is why `fooba` is not a match.  However, the `findall` function is not returning the entire match when we process the string `foobar` - it's only returning the part of the match enclosed in parentheses.  This is a really useful feature of regular expressions when want to extract specific parts of a string.

We can define multiple groups in a pattern:
```python
>>> pat = re.compile('f(o+)b(a+)r')
>>> pat.findall('foobar')
[('oo', 'a')]
```

Extracting groups is useful when we want to apply a test to a specific group.  For example, we could use a regular expression to validate calendar dates:
```python
>>> pat = re.compile("([0-9]{4})-([A-Z][a-z]{2})-([0-9]+)")  # e.g., 1999-Jan-01
>>> pat.findall('1970-Jan-01')
[('1970', 'Jan', '01')]
>>> year, month, day = pat.findall('2009-Oct-21')[0]  # note we had to index into the list returned by findall
>>> int(day) <= 31  # validate day
True
>>> month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
True
```
In practice, we would want to include a conditional to check whether `findall` matched *any* substring.  If it didn't, then that would imply that the string did *not* contain a valid calendar date (at least, according to how we are defining valid date strings).



### Example: Defining sequence motifs

A common application of regular expressions in bioinformatics is matching sequence motifs.  For example, some proteins are modified by the addition of glycans (large sugar molecules) to specific amino acids.  The glycosylation of amino acids is determined by motifs in the primary protein sequence.  N-linked glycoslyation involves the addition of a glycan to an asparagine that is part of a four-residue motif that includes either a serine or threonine at the third position, and no prolines at either the second or fourth positions.  

We *could* scan for potential motifs using a series of `if..else` statements and looping through the sequence:
```python
def lousy_way(s):
    """ Scan an amino acid sequence for N-linked glycosylation motifs """
    results = []
    for i in range(len(s)-3):
        peptide = s[i:(i+4)]
        if peptide.startswith('N') and 'P' not in peptide and peptide[2] in 'ST':
            results.append(peptide)
    return(results)
```
but using a regular expression is far more elegant and faster:
```
def good_way(s):
    return re.findall('N[^P][ST][^P]', s)
```

Here is our function in action when applied to a [human herpesvirus 2 envelope glycoprotein B](https://www.ncbi.nlm.nih.gov/nuccore/KP143740.1) sequence:
```
>>> p = "MRGGGLICALVVGALVAAVASAAPAAPRASGGVAATVAANGGPASRPPPVPSPATTRARKRKTKKPPERPEATPPPDANATVAAGHATLRAHLREIKVENADAQFYVCPPPTGATVVQFEQPRRCPTRPEGQNYTEGIAVVFKENIAPYKFKATMYYKDVTVSQVWFGHRYSQFMGIFEDRAPVPFEEVIDKINAKGVCRSTAKYVRNNMETTAFHRDDHETDMELKPAKVATRTSRGWHTTDLKYNPSRVEAFHRYGTTVNCIVEEVDARSVYPYDEFVLATGDFVYMSPFYGYREGSHTEHTSYAADRFKQVDGFYARDLTTKARATSPTTRNLLTTPKFTVAWDWVPKRPAVCTMTKWQEVDEMLRAEYGGSFRFSSDAISTTFTTNLTQYSLSRVDLGDCIGRDAREAIDRMFARKYNATHIKVGQPQYYLATGGFLIAYQPLLSNTLAELYVREYMREQDRKPRNATPAPLREAPSANASVERIKTTSSIEFARLQFTYNHIQRHVNDMLGRIAVAWCELQNHELTLWNEARKLNPNAIASATVGRRVSARMLGDVMAVSTCVPVAPDNVIVQNSMRVSSRPGTCYSRPLVSFRYEDQGPLIEGQLGENNELRLTRDALEPCTVGHRRYFIFGGGYVYFEEYAYSHQLSRADVTTVSTFIDLNITMLEDHEFVPLEVYTRHEIKDSGLLDYTEVQRRNQLHDLRFADIDTVIRADANAAMFAGLCAFFEGMGDLGRAVGKVVMGVVGGVVSAVSGVSSFMSNPFGALAVGLLVLAGLVAAFFAFRYVLQLQRNPMKALYPLTTKELKTSDPGGVGGEGEEGAEGGGFDEAKLAEAREMIRYMALVSAMERTEHKARKKGTSALLSSKVTNMVLRKRNKARYSPLHNEDEAGDEDEL"
>>> from time import time
>>> t0 = time(); good_way(p); time() - t0
['NATV', 'NYTE', 'NLTQ', 'NATH', 'NASV', 'NITM']
5.91278076171875e-05
>>> t1 = time(); lousy_way(p); time()-t1
['NATV', 'NYTE', 'NLTQ', 'NATH', 'NASV', 'NITM']
0.0006232261657714844
>>> 0.0006232261657714844 / 5.91278076171875e-05
10.540322580645162
```
So using regular expressions not only gives us tidier code, but it's also much faster!

![](https://imgs.xkcd.com/comics/cadbury_eggs.png)


## Find and replace

Replacing groups is another powerful application of regular expressions.  We've already discussed how the `str.replace` function can be used to replace all instances of a specific substring with another specific substring:
```python
>>> "lobster".replace('ster', 'by')
'lobby'
```
We are often dealing with ambiguous or complex cases where we need to replace a variety of (often similar) strings with a particular substitute string, or with string that is derived from the match.  Replacements are accomplished using the `re` module function `sub`.  In the first case, we can simply provide the replacement substring that will be substituted into every match.  For example:
```python
>>> s
'The Dillinger Escape Plan'
>>> re.sub('[A-Z]', 'Z', s)
'Zhe Zillinger Zscape Zlan'
```
Or a more biologically useful example:
```python
def censor_stop_codons(seq):
    """
    Convert any stop codons in a nucleotide sequence into ambiguous codons.  Assumes standard
    genetic code.
    """
    return re.sub("TA[AG]|TGA"
```

What if we want to move matches around, or replace everything around the matches?  Well, we need to have some way to refer to specific groups.  Regular expressions provides a scheme for doing this: we can refer to the first group as `\1`, the second as `\2` and so on.  For example, we can swap the first two capital letters in our example by referencing the different groups in another order:
```python
>>> re.sub('^([A-Z])([^A-Z]+)([A-Z])(.+)', '\\3\\2\\1\\4', s)
'Dhe Tillinger Escape Plan'
```
Note that we had to escape the escape character `\`!  

![](https://imgs.xkcd.com/comics/substitutions.png)


## Getting more information about groups

So far, we have just used two of the functions in the `re` module: `findall` and `sub`.  To understand some of the other functions, we have to learn about the `Match` object that is defined by the `re` module.  Think of a `Match` as a special object like strings in lists in Python; it has its own attributes and functions, including:
* `group`: the matching substring
* `span`: the start and end indices of the substring relative to the parent string
* `string`: the parent string
* `groups`: a tuple containing groups captured by the regular expression

The functions that return a *Match* object or a generator of *Match* objects are:
* `search`: returns a *Match* object for the first instance of the regular expression
* `match`: applies the regular expression to the start of the string only
* `finditer`: returns a generator for all non-overlapping *Match* objects

In practice, I can usually accomplish what I need to do without getting involved with *Match* objects.  If I'm not doing a simple find-and-replace and I need the location of the matching substrings for some other reason, then I might use `finditer`.  

