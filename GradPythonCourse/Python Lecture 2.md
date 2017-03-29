# Conditionals and Loops

* **Before we start conditionals, we must go over a few basic functions**
  * Print function
    * Example:
      ```
      print(Hello all!):
    
      Hello all!
      ```
      
  * Open function
    * Example:
      `open('<path>', '<mode>')` 
      * Where the path indicates where the file is to be found and mode indicates what mode the file should be opened in
    * Table 1.  The corresponding meaning of characters indicating different modes.
    **** INSERT PHOTO!** 
  * Read function
    * Once you have a file open, you can now read it.
    * Example:
    ```
      f.read()
      'Entire document contents'
      ```
  * Readline function
    * Once you have a file open, you can now read a single line.
    * Example:
    ```
      f.readline()
      'First line of the file'
      f.readline ()
      'Second line of the file'
      ```
  * Write function
    * Once you have a file open, you can write the contents of a string into a file
    * Example:
    ```
      f.write('insert this line into the document\n')
      ```
      * **Note** \n indicates "new line"
   * Close function
    * Once you have finshed with the file, you can close it.
    * Example:
      `f.close()`
      

# Conditionals  

* "If" 
  * Example:
  ```
  meal= 1
  If meal:
    print("order up!")
  
  'order up!'
  ```

* "If" "Else" 
  * Example:
  ```
  meal= 0
  if meal:
    print("order up!")
  else:
    print ("not ready yet!")
    
  not ready yet! 
  ```

* Comparison operators
  * Can compare two values
  * Example:
  
    ```
    if (8>9):
      print('true'):
    else:
      print('false'):
      
    false
    ```
    
* "and"
  * combines two conditionals if BOTH conditions are met
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

# Loops

* Loops are a way to repeat an action multiple times with less code
  * "For" loops
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
    
* Range 
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
* Range with paremeters

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
