# In-class assignment 6
## Debugging Python

In each of the following questions, you'll see a small amount of Python code and the output that is produced when the code is run.  In every case, the output should read `correct!`.  Make corrections directly to the Python code and e-mail me your edited Markdown file.  (Hint: all of these code blocks have more than one problem to fix.)

1. Code:
   ```python
   print['correct!]
   ```
   Output:
   ```shell
     File "<stdin>", line 1
       print['correct!]
                   ^
   SyntaxError: EOL while scanning string literal
   ```

2. Code:
   ```python
   letters = ['c', 'e', 'o', 'c', 'r' 't', 'r']
   for offset in range(2):
       for i in range(offset, len(letters, 2)):
           unscrambled = letters[i]
   print(unscrambled)
   ```
   Output:
   ```shell
   t
   ```

3. Code:
   ```python
   def mascii(numlist):
       # map all numbers in the list `numlist` to the ASCII character set
       # and return the resulting string
       result = ''
       for i in input:
           result += chr(i)
       return numlist
   
   input = [99, 111, 114, 114, 101, 99, 116, 33]
   mascii(result)
   ```
   Output:
   ```
   Traceback (most recent call last):
     File "inca6.py", line 10, in <module>
       mascii(result)
   NameError: name 'result' is not defined
   ```
   
4. Code:
   ```python
   d = {'A': 'c', 'B': 'o', 'C': 'r', 'D': 'e', 'E': 't', 'F': '!'}
   input = 'feadccba'
   output = ''

   for i in range(len(input), 0, -1):
	   let = input[i]
       output += input[i]
	   if let.islower():
		    output += let.upper()
   
   print(output)
   ```
   
