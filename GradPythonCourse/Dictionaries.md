
## Gathering information with dictionaries

A dictionary is an extremely useful Python object.  It is a collection of key-value pairs, where a *key* is an immutable object like a string or integer, and a *value* is another object that is referred to by that key.  For example, in an English-language dictionary, the word *apple* is a key, and its associated value is a definition of apple.  In a phone book, the key would be your friend's name, and the value would be their phone number.  These examples should give you an intution that keys need to be unique.  You can't have two names in a phone book that are *exactly* the same; this would defeat the purpose of having a phone book in the first place.

A value can be any object, including mutable objects like lists.  It can even be a dictionary!  This creates an interesting data structure.  If you think of a dictionary as the root of a tree:
```
root --+-- key1 --> value1
       |
       +-- key2 --> value2
```
then setting `value2` to be another dictionary creates another level of the tree:
```
root --+-- key1 --> value1
       |
       +-- key2 --> root --+-- key3 --> value3
                           |
                           +-- key4 --> value4
```
This makes dictionaries a natural representation of tree-like (hierarchical) data.

Try making a simple dictionary.  To initialize an empty dictionary, use curly braces like this:
```python
>>> d = {}
```
You can then add items to the dictionary using its `update` function:
```python
>>> d.update({'toast': 1, 'jam': 5})
>>> d
{'jam': 5, 'toast': 1}
```
We could also have initialized the dictionary starting with these items:
```python
>>> d = {'jam': 5, 'toast': 1}
>>> d = dict(jam=5, toast=1)  # another way to do it
```

Dictionaries are also useful for rapidly looking up objects.  This is because of how they work - each key is converted by a [hash function]() into an index that is used to directly look up the associated value.  For example, suppose you have compiled a list of genes from one data set, and you need to check whether a particular gene is in the list.  One way to do this is to use the `in` operator to check if our list contains the gene:
```python
>>> from time import time
>>> li = list(range(int(1e6)))  # all integers from 0 to 999999
>>> t0 = time(); 89987 in li; t1 = time()
True
>>> t1-t0
0.003858804702758789  # seconds
```
That might not seem like a long time, but when you are dealing with a very large data set and you need to look things up many times, this can consume a lot of computing time.  This is because the computer is doing a linear search through the list.  It is like entering a bookstore and looking for a specific book by starting at the first shelf, taking each book off the shelf and looking at its cover until you find the one you want.  If the store has a million books, then on average the book you want will be roughly the 500,000th book you pull off the shelf.  (We're assuming that this is a really silly store that arranges its books completely at random.)

To illustrate, here is a bit of Python code to demonstrate that we get about the same time as the `in` operator with a linear search through the list:
```python
from time import time
li = list(range(1000000))

t0 = time()  # start the clock!
for i in li:
  if i==89987:
    break  # exit the loop
t1 = time()
print(t1-t0)  # I get 0.0033576488494873047 seconds
```

Now let's accomplish the same task by converting our list into a dictionary.  We don't have any values to associate with the keys, so we just set them all to `None`.
```python
>>> di = dict([(k, None) for k in li])  # constructing from a list of key-value tuples
>>> t0 = time(); 89987 in di; t1 = time()
True
>>> t1-t0
4.291534423828125e-05  # seconds
```
This is nearly two orders of magnitude less time!

Dictionaries are also very useful when you need to associate multiple values with the same key.  For example, suppose that you have observations for the same patients in different files, and you need to merge those records.  However, these files are not in the same order and don't even contain all the same patients.  One approach to deal with this situation is to read each file into Python and accumulate records under unique keys, where each key corresponds to a patient, and then writing out the information you want into another file.

I do this all the time when working through data from large cohort studies.  Of course it isn't the only way to go about this, and not necessarily the best way.  I think many would argue that you should build a database with a framework like SQLite instead of using a Python script to make yet another tabular data file.  However, I like working directly with the data and being able to inspect the end product as a plain text file.
