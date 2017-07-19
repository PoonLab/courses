# Python:
# Python Base Objects:
## Base Objects
* Non-iterable 
  * Integers
    * Whole numbers
    * Example: 27
  * Floats
    * Have decimal
    * Example: `3.41`
* Iterable
  * Strings (not mutable)
    * Essentially an assortment of characters (ie. letters, numbers, punctuation)
    * Can be declared using single or double quotation marks
    * Example: `"apple"`
  * List (mutable)
    * Used for storing an assortment of data types (ie. integers, floats, strings, etc.)
    * Can be delcared using square brackets
    * Example: `[27, 3.41, ‘apple’]`
  * Tuple (not mutable)
    * Essentially an "unadjustable" list
    * Can be declared using parentheses 
    * Example: `(27, 3.41, 'apple')`
  * Dictionaries (mutable)
    * Used for pairing keys to objects
    * Can be declared using curly brackets
    * Example: 

      ```
      Sarah= {}
      Sarah["lunch"]= "salad"
      Sarah["dinner"]= "potroast"
      Sarah
      {'lunch':'salad', 'dinner':'potroast'}
      ```
 
 **Question** Sarah skipped her lunch break to run an experiment in lab, how do we change the dictionary?
 
      ```
      del Sarah["lunch"]
      {'dinner':'potroast'}
      ```
## Dynamic Typing
* a=7 (integer)
* Note: you are assigning the integer 7 to 'a'
* When you type 'a' into python, it will be defined as 7
* 'a' can also be a string, float, etc.
## Important Note: Python is a Zero-based Index
* In python we start counting with 0 instead of 1.
* Let's use this example to explain:
  ```
  a= "apple"
  a[0]...'a'
  a[3]...'l'
  a[0:2]...'ap'
  a[1:-1]... 'ppl'
  ```
## Manipulation of Strings
* Combining two strings:
  * Concatenation
    ```
    a= "red" + "dog"
    'reddog'
    for a in "reddog":
        print("z"+a)
    ```
* Combining numbers and strings (aka Cast and Concatenate):
  * Example:
    ```
    a= 3 
    b= "cookies"
    c= a+b
    ```
  **Note**: You will receive an error.
    ```
    c= str(a) + b 
    c
    '3cookies'
    ```
* Using a place holder
    ```
    "%d" %NUM= substitute INTEGER
    "%f" %NUM= substitute FLOAT
    ```
  * Example:
    ```
    a= 1207
    b= "room%d"%a
    b
    'room 1207'
    ```
## Manipulation of Lists
* Adding values to the end of a list
  * Append(VALUE):
    * Example:
      ```
      a= [3, 'apple', 67.2]
      a.append('sheep')
      a
      [3, 'apple', 67.2, 'sheep']
      ```
 * Adding values to the middle of a list
   * insert(Location, VALUE):
     * Example:
       ```
       a= [3, 'apple', 67.2]
       a.insert(1, 'sheep')
       a
       [3, 'sheep', 'apple', 67.2]
       ```
     * **Note:** Remeber that python is a *zero-based index*!
* Remove a value at a specific location
  ```
  pop(location)
  a= [3, 'sheep', 'apple', 67.2]
  a.pop(1)
  a
  [3, 'apple', 67.2]
  ```
* Converting items to a list
  ```
  list(item)
  list("western university")
  ['w', 'e', 's', 't', 'e', 'r', 'n', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
  ```
## Operators
* Functions that acts on objects.
* Examples:
  * add + 
    * Example: 
    ```
    a= 1+2=3
    a= "western"+"university"= "westernuniversity"
    ``` 
  * Subtract -
  * Divide /
  * Multiply *
    * Example: 
    ```
    a=3*4=12
    a= "bird"*3= 'birdbirdbird'
    ```
  * Power/Exponent **
# Python Basic Functions:
## Print function
* Example: 
  ```
  print(Hello all!):
    
  Hello all!
  ```
## Open function
* Example: 
  ```open('<path>', '<mode>')```
  * Where the path indicates where the file is to be found and mode indicates what mode the file should be opened in.
## Read function
* Once you have a file open, you can now read it.
* Example: 
  ```
  f.read()
  'Entire document contents'
  ```
## Readline function
* Once you have a file open, you can now read a single line.
* Example: 
  ```
  f.readline()
  'First line of the file'
  f.readline ()
  'Second line of the file'
  ```
## Write function
* Once you have a file open, you can write the contents of a string into a file.
* Example:
  ```
  f.write('insert this line into the document\n')
  ```
  * **Note** \n indicates "new line"
## Close function
* Once you have finshed with the file, you can close it.
* Example:
  ```
  f.close()
  ```
# Python Conditionals:
## "If"
* Example:
  ```
  meal= 1
  If meal:
    print("order up!")
  
  'order up!'
  ```
## "If" "Else"
* Example:
  ```
  meal= 0
  if meal:
    print("order up!")
  else:
    print ("not ready yet!")
    
  not ready yet! 
  ```
## Comparison operators
* Can compare two values
 * Example:
  
   ```
   if (8>9):
     print('true'):
   else:
     print('false'):
      
   false
   ```
## "and"
* Combines two conditionals if BOTH conditions are met
* Example:
  
  ```
  if (8) and (9):
    Print("true")
  true
    
  if (8) and (9):
    Print("yes")
  if not (8):
    Print("no")
     
  yes
  ```
# Python Loops:
* Loops are a way to repeat an action multiple times with less code
## "For" loops
* This type of loop tells the computer that for every item in a list or range, loop over it!
* Example:
  ```
  x= [1,2,3]
  for i in x:
  Print i
        
  1
  2
  3
  ``` 
## Range 
* creates a sequence of numbers
* Example:
  ```
  For i in range(30):
  Print i
      
  0
  1
  2
  ...
  29
  ```
## Range with paremeters
* Example: 
  ```
  for i in range (10, 30, 2)
    print i
    
  10
  12
  14
  ...
  28
  ```
  * **Note** This means that we want the range from 10-30 in increments of 2

