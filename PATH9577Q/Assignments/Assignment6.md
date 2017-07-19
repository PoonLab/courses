# Assignment 6 - Good code

Please submit this Markdown document with your answers to me by e-mail.  
Due date: July 4, 2017.

1. Identify three things (each with a specific example) about the following script that are **not** consistent with good Python coding style as defined in our class.  Use the space provided in the nested list below for your answers:
   ```python
   def z(q    ):
    m=''
    for y  in q:
     y = y.upper()
     if y=='A':
      m+='T'
     elif y=='C': m+='G'
     elif y=='G':
      m+='C'
     elif y=='T': m+='A'
     else:
         m +=   '?'
    return m
   import sys
   print(z(sys.argv[1]))
   ```
   1. 
   2. 
   3. 

2. Write documentation within the following script using inline or block comments, or docstrings:
   ```python
   def dna_complement(seq):
       complement = {'A': 'T', 
                     'C': 'G', 
                     'G': 'C', 
                     'T': 'A'}
       result = map(lambda x: complement.get(x, '?'), seq.upper())
       return ''.join(result)
   ```

3. Complete a script that includes the above function (with your documentation), using the `argparse` module to take a string argument from the command line.  Provide help text.  Print the result to the console.  Use the template below:
   ```python
   import argparse
   
   def main():
       # your code here
   
   if __name__ == '__main__':
       main()
   ```
