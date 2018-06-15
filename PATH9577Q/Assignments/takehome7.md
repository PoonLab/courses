# Take-home assignment 7
## Regular expressions and formatted strings

1. First, we're going to create a function that searches an amino acid sequence for possible nuclear localisation signals (NLSs) -- a sequence that flags a protein for transport into the nucleus.  There are several different motifs that generally comprise basic residues (lysine and arginine).  [The "classical" bipartite NGS](http://elm.eu.org/elms/TRG_NLS_Bipartite_1) is described by the following regular expression:
   ```
   [KR][KR].{7,15}[^DE]((K[RK])|(RK))(([^DE][KR])|([KR][^DE]))[^DE]
   ```
   where bipartite means "two parts".
   
   Write a function that takes a protein sequence as its single argument and returns the number of potential classical bipartite NGSs.
   ```python
   
   
   ```
   
2. Next, we need to write a function that reads in a FASTA formatted file and returns a list of label-sequence tuples.  I'll provide pseudocode (a set of instructions that resemble a computer program but use human language) here:
   - Declare a new variable storing an empty list.
   - Set `sequence` to an empty string.  Set `label` to an empty string.
   - Iterating over each line in the file stream:
      - If the line starts with `>`:
         - If `sequence` is a non-empty string
            - append the current label-sequence pair as a tuple on the list
            - reset `sequence` to an empty string
         - Either way, strip `>` from the current line and assign the result to `label`
      - Otherwise, strip `>` from the current line and append the result to `sequence`
   - Append the final label-sequence pair as a tuple on the list
   - Return the list
   ```python
   
   ```
   
3. Finally, incorporate your functions from Q1 and Q2 into a script that takes two file paths from the command line (via `sys.argv`):
   * a path containing a FASTA file of amino acid sequences
   * a path to write tab separated output
   
   Use either old- or new-style string formatting to write the following items on each line of the output file, for each sequence in the input FASTA:
   * The sequence label
   * The length of the sequence in amino acids
   * The number of predicted localisation signals


4. Run the result on this file:
   https://github.com/PoonLab/courses/blob/master/PATH9577Q/Assignments/motifs.fasta
   and paste the result here:
   ```
   
   
   ```
