# Failure to Launch: Challenges in bringing next-generation sequencing into the clinical HIV laboratory

## Art Poon [@GitHub](github.com/ArtPoon)
#### Departments of Pathology and Laboratory Medicine; Microbiology and Immunology; Applied Mathematics at Western University, Ontario, Canada



# HIV genotyping is standard of care

* Generate the genetic sequence of a patient's HIV infection
* Examine sequence for mutations that confer drug resistance
* Optimize patient's drug regimen in response to virus evolution
* Significantly improves clinical outcomes!



# BC Centre for Excellence in HIV/AIDS

<center>
![CFE logo](/img/cfelogo.png)
</center>

* A CAP accredited clinical laboratory for HIV genotyping.
* BC Drug Treatment Program - fully subsidized clinical testing and treatment for all residents of BC living with HIV
* A population database with clinical, demographic and genetic data for nearly 9,000 patients. 
* Over 30,000 HIV resistance genotypes



# 
<center>
![](/img/cfe-samples.svg)
</center>



# Sanger sequencing

<center>
![DNA sequence chromatogram](/img/DNAsequence.svg)
</center>

* Dye-terminator sequencing with capillary electrophoresis.
* A decades-old workhorse of the modern lab.
* Ambiguous base calls can reproducibly detect minority HIV species (>25%)



# Next-generation sequencing

* Run millions of sequencing reactions at the same time!
* Development of new sequencing chemistry, highly specialized instruments.



# The promise of NGS for HIV

* Detection of minority HIV variants
* More cost-effective whole-genome sequencing?
* Reconstructing the evolution of HIV within patients



# 
![Starship Enterprise](/img/enterprise.jpg)



# 
![Debris from Virgin Spaceship Two](/img/spaceship2.jpg)



# The 454 
![The 454 GS-FLX](/img/gs-flx.jpg)
![Basic steps of Roche/454 pyrosequencing](/img/454.svg)




# Thousands of reads per sample...

* Could still use the usual software to process the data.
* Roche/454 became dominant in field of HIV because of longer read lengths. 
* More linkage information for polymorphisms
* Much work centred on clinical validation of 454 for screening HIV coreceptor 
  tropism



# HIV coreceptor tropism
![HIV uses one of two coreceptors to enter a cell](/img/coreceptors.svg)



# HIV coreceptor antagonists

* Some people have a large deletion in CCR5 that confers natural resistance to 
  HIV infection
* Coreceptor antagonists mimic this phenotype by blocking CCR5
* If HIV V3 evolves tropism to CXCR4, then antagonist is ineffective
* *Trofile* was standard phenotypic assay used to screen patients



# 
<center>
![Deep sequencing analysis of maraviroc trials](/img/maraviroc.jpg)
</center>
from Swenson *et al.* (2011) J Infect Dis 203(2): 237-245.



# 
<center>

![Mapping tropism mutations to HIV trees](/img/MCTmaps.svg)
</center>



# Curse of the homopolymer

* The 454 and similar systems suffered from high insertion/deletion error rates 
* Worst within single nucleotide repeats (homopolymers)
* The HIV genome is about 40% A!
* HIV drug resistance mutations K65R and K103N in islands of A-repeats



# K103N = AAAAA!
![AAAAA!](/img/AAAAA.png)



# The Fallen

* [rc454](https://www.broadinstitute.org/viral-genomics/rc454)
* [Segminator](http://www.bioinf.manchester.ac.uk/segminator/)
* [hy454](http://www.datamonkey.org/dataupload_uds.php)
* Roche/454



# The Illumina MiSeq

![MiSeq](/img/miseq.png) ![MiSeq process](/img/miseq.svg)



# 100,000's of reads per sample!

* Orders of magnitude more data to process
* Slightly higher error rate
* No homopolymer error issue




# MiCall



# Tile-cycle error rates



# Longitudinal contamination



# Cross-contamination



# FDA requirements



# Kive



# Kive demo



# 
