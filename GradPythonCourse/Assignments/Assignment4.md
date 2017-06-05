1. Modify the following Python script to be called from the command line for any input file:
   ```python
   def main(path):
       handle = open(path, 'rU')
       headers = []
       counter = 0
       outfile = None
       for line in handle:
           if line.startswith('@'):
               headers.append(line)
               continue
           if counter % 10 == 0:
               if outfile:
                   outfile.close()
               # open new file
               outfile = open('slice{}.sam'.format(counter), 'w')
               for header in headers:
                   outfile.write(header)
           outfile.write(line)
           counter += 1
       outfile.close()
           
   main('input.sam')
   ```
   Save your script to a file in the `examples` folder and run it on the `SRR5261740.trunc.sam` file.
   
2. 
