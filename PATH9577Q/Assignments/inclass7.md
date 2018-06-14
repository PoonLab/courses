# In-class assignment 7
## Regular expressions and sequence motifs

Regular expressions play an important role in bioinformatics because we are often dealing with long nucleotide or protein sequences that contain motifs, where a motif is a biologically significant pattern.  In this exercise, we're going to use regular expressions to count the number of motifs in some example sequences.  For example, the [Eukaryotic Linear Motif database](http://elm.eu.org/) is a repository of short linear motifs (SLiMs) in protein sequences that play important roles in regulating cellular processes.  

1. Human immunodeficiency virus type 2 (HIV-2) is the less prevalent of the two types of HIV that can cause AIDS.  Like HIV-1, the HIV-2 virus particle has a lipid envelope studded with glycosylated envelope proteins.  N-linked glycans play a significant role in the immune evasion of the virus -- as a product of the cellular post-translation modification pathway, they are recognized as 'self'.  

The motif for an N-linked glycosylation site comprises 4 amino acids:
   1. an asparagine (`N`)
   2. any residue except proline (`P`)
   3. either a serine (`S`) or a threonine (`T`)
   4. any residue except proline (`P`)

In the space provided, compile a regular expression for this motif and find all potential N-linked glycosylation sites in the given protein sequence.  How many glycosylation sites does this sequence contain?:
```python
import re
aaseq = 'MTSEKTQLLIAILLASTCLLYCKQYVTVFYGVPAWRNASIPLFCATKNRDTWGTIQCLPDNDDYQEIALNVTEAFDAWNNTVTEQAIDDVKRLFETSIKPCVKLTPLCVAMNCTNVTSTANTTITISSTNMIVNDSSPCASNDSCPGMGEEEMVQCNFSMTGLQRDKVKQYNETWYSRDVVCDQGENDTRRCYMNHCNTSVITESCDKHYWDDMRFRYCAPPGYALLRCNDTNYSGFMPNCSKVVAATCTRMMETQTSTWFGFNGTRAENRTYIYWHSKSNRTIISLNKSFNLSLHCKRPGNKTVVPITLMSGLVFHSQPINTRPRQAWCWFEGEWKEAMQEVKRAIAKHPRYTGTNDTGKINLTAPGRGSDPEVSYMWTNCRGEFLYCNMTWFLNWVENRTGIQRNYAPCHIRQIINTWHKVGKNVYLPPREGELVCNSTVTSLIADIDWIDKNGTNITFSAEVSELYRLELGDYKLVEITPIGFAPTTEKRYSPNHGRPKRGVFVLGFLGFLATAGSAMGAASLTLSAQSRTLLAGIVQQQQQLLDVVKRQQEMLRLTVWGTKNLQARVTAIEKYLGDQARLNSWGCAFRQVCHTTVPWVNDTLMPDWKNMTWQKWEEQIRYLEANISDSLEQAQIQQEKNTYELQKLNSWDVFTNWLDLTSWIKYIQYGVYIVVGIIALRIVIYVVQMLSRLRKGYRPVFSSPPGYIQQIHIHKGQEQPTREGTEEDVGDNGGDRSWPWPIAYLHFLIRLLIRLLITLYNSCRDLLSRIFQTLQPILRNLRDWLRIKTALLQYGCEWIQEAFQAAARTTGETLAGACRGLWRTLGRIGRGIFAVPRRIRQGAEIALL'

```

2. Using the same sequence, generate a list of the start positions for every motif.
```python

```

3. [Noonan-like syndrome](http://elm.eu.org/diseases/) is a genetic condition characterized by  
