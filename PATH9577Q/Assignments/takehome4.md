# Take-home assignment 4
Write a script to retrieve the entry at a specific row and column index of a CSV file.

1. First, we need to write a function that takes an open file as its single argument.  The file should be assumed to contain a tabular data set in a CSV format.  The function should return a list of lists.  Each internal list should correspond to a row in the tabular data set.  Remember, to insert a list into the end of a list, use the `append` function; for example, `a = [[6,7]]; a.append([1,2,3])` results in `[[6,7], [1,2,3]]` assigned to `a`.
   ```python
   def csv_to_lists(handle):
       rows = []
       # your code goes here!
       return rows
   ```

2. Next, use the template below to write a `main` function that handles arguments from the command line.  It should check that there are three arguments (other than the name of the script).  
   * The first argument should be a path to the CSV file
   * The second argument should be an integer to index into the row
   * The third argument should be an integer to index into the column

   ```python
   import sys
   
   # your csv_to_lists function should go here
   
   def main():
       # check that sys.argv is expected length - return a helpful message if it isn't
       
       # unpack the contents of sys.argv
       # cast the appropriate values as `int`
       
       # call csv_to_lists and assign the result to a variable `lists`
       
       # check that `lists` has enough rows
       
       # index into the requested row
       
       # check that this row is long enough
       
       # index into the requested row entry (column)
       
       # print the result
       
   if __name__ == '__main__':
       main()  # we got called from the command line!
   ```

3. Run your script on the file `esoph.csv` to print the value in row 4, column 4.  (Remember, Python is zero indexed!)  Paste the result below:
   ```shell
   
   ```


