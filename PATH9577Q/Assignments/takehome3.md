# Take-home 3
To submit this assignment, e-mail to me your copy of this Markdown document and the Python script.

*Name:*


1. Open a new text file called `tka3.py`.  Copy and paste the following:
   ```python
   import sys
   
   def main():
       print(sys.argv)
   
   if __name__ == '__main__':
       main()
   ```
   This is a standard structure for a Python script that can potentially be imported into another script: the `main` function is only run if we call `tka3.py` directly on the command line.  Modify the `main` function of this script so that it iterates over the contents of `sys.argv` and prints each member to the console, and copy the result below:+
   ```python
   # paste your code here
   ```

2. Now we're going to define a new function called `scramble`.  This function should take a single argument, check that it is a string, and then collect all the odd-indexed and even-indexed characters into two separate substrings, and return the concatenation of these substrings.  For example, `pizza` should return as `izpza`.  Add this code after the first `import sys` line and copy the result below:
   ```python
   import sys
   # paste your code here
   ```
   
3. Add a second function called `obscure`, which:
   * takes two integers `a` and `b`, multiplies them together and stores the remainder when we divide this product by `17` as `z1`
   * multiply `a` by 17 and stores the remainder when we divide by `b` as `z2`
   * return the greater of `z1` and `z2`.  
   For example, `84` and `38` should return `22`.
   ```python
   # paste your code here
   ```

4. Finally, utilize these two functions in the `main` function as follows:
   * iterate through `sys.argv`
   * for any entry that *cannot* be cast as an integer, apply `scramble` and print the result.
   * for any entry that *can* be cast as an integer, apply `obscure` to the previous integer entry and this current one, and print the result.  Since the first integer you encounter will have no previous integer, use `128`.  
   Since every entry in `sys.argv` is always a string, use the function below to check whether the string can be cast as an integer.
   ```python
   def cast_integer(s):
       try:
           result = int(s)
       except ValueError:
           return False
       return True
   
   def main():
       last_integer = 128
       # paste your code here
   ```

5. Run your script with the following command line arguments and paste the result the same field:
   ```shell
   python3 tka3.py blue 987345 red 7197982 green 109832
   # copy the output here
   ```
