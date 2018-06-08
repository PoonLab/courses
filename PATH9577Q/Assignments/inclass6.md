# In-class assignment 6
## Debugging Python

In each of the following questions, you'll see a small amount of Python code that is full of bugs.  In every case, the output should read `correct!`.  Make corrections directly to the Python code and e-mail me your edited Markdown file.  (Hint: paste the code into a text file, run the script and examine the error message that results.)

1. Code:
   ```python
   print['correct!]
   ```
   
2. Code:
   ```python
   letters = ['c', 'e', 'o', 'c', 'r' 't', 'r']
   unscrambled = ''
   for offset in range(2):
       for i in range(offset, len(letters, 2)):
           unscrambled = letters[i]
   print(unscrambled)
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
   
