# In-class assignment 6
## Debugging Python

In each of the following questions, you'll see a small amount of Python code and the output that is produced when the code is run.  In every case, the output should read `correct!`.  Make corrections directly to the Python code and e-mail me your edited Markdown file.

1. Code:
   ```python
   print('correct!)
   ```
   Output:
   ```shell
     File "<stdin>", line 1
       print('correct!)
                   ^
   SyntaxError: EOL while scanning string literal
   ```

2. Code:
   ```python
   letters = ['c', 'e', 'o', 'c', 'r', 't', 'r']
   for offset in range(2):
       for i in range(offset, len(letters), 2):
           unscrambled = letters[i]
   print(unscrambled)
   ```
