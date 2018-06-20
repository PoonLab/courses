# Take-home assignment 7
## Nuclear localisation signals

1. First, we're going to create a function that searches an amino acid sequence for possible nuclear localisation signals (NLSs) -- a sequence that flags a protein for transport into the nucleus.  There are several different motifs that generally comprise basic residues (lysine and arginine).  [The "classical" bipartite NLS](http://elm.eu.org/elms/TRG_NLS_Bipartite_1) is described by the following regular expression:
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
      - Remove the line break character
      - If the line starts with `>`:
         - If `sequence` is a non-empty string
            - append the current label-sequence pair as a tuple on the list
            - reset `sequence` to an empty string
         - Either way, strip `>` and `\n` from the current line and assign the result to `label`
      - Otherwise, strip `\n` from the current line and append the result to `sequence`
   - Append the final label-sequence pair as a tuple on the list
   - Return the list
   ```python
   
   ```
   
3. Finally, incorporate your functions from Q1 and Q2 into a script that takes two file paths from the command line (via `sys.argv`):
   * a path containing a FASTA file of amino acid sequences
   * a path to write tab separated output
   
   Use either old- or new-style string formatting to write the following items (delimited by tabs) on each line of the output file, for each sequence in the input FASTA:
   * The sequence label
   * The length of the sequence in amino acids
   * The number of predicted localisation signals
   
   ```python
   # paste your script here
   
   ```


4. Run the result on this file:
   https://github.com/PoonLab/courses/blob/master/PATH9577Q/Assignments/motifs.fasta
   
   Your answer should look like this:
   ```
   L07347.1 Influenza A virus (strain A/memphis/4/73) nucleoprotein (NP) gene, complete cds	586	1
   AAA42967.1 nucleoprotein [Dhori thogotovirus]	522	1
   AAA43798.1 nucleoprotein [Influenza C virus]	609	0
   AAA16109.1 cyclin-dependent kinase inhibitor [Homo sapiens]	223	1
   AAI17252.1 Tumor protein p73 [Homo sapiens]	679	1
   sp|P08153.1|SWI5_YEAST RecName: Full=Transcriptional factor SWI5	773	1
   AGE89224.1 nucleoprotein [Salmon isavirus]	658	0   
   ```
