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



# Three grand challenges

1. Error rates and diversity
2. Contamination
3. Reproducibility



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
<small>Swenson *et al.* (2011) J Infect Dis 203(2): 237-245.</small>



# 
<center>
![Mapping tropism mutations to HIV trees](/img/MCTmaps.svg)
</center>
<small>Poon *et al.* </small>



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
* No homopolymer error issue - bases added one at a time

* Can this new platform be used for clinical HIV genotyping?



# Read mapping

* Volume of data demands faster sequence alignment methods
* Settled on *bowtie2* to map reads to an indexed reference genome
* Rapid look-up of sequence fragments for genome positions 
* Efficient local alignment handles sequence divergence



# HIV variability is a problem
```
10000 reads; of these:
  10000 (100.00%) were paired; of these:
    10000 (100.00%) aligned concordantly 0 times
    0 (0.00%) aligned concordantly exactly 1 time
    0 (0.00%) aligned concordantly >1 times
    ----
    10000 pairs aligned concordantly 0 times; of these:
      0 (0.00%) aligned discordantly 1 time
    ----
    10000 pairs aligned 0 times concordantly or discordantly; of these:
      20000 mates make up the pairs; of these:
        19979 (99.89%) aligned 0 times
        21 (0.10%) aligned exactly 1 time
        0 (0.00%) aligned >1 times
0.10% overall alignment rate
```



# Adaptive reference mapping

* Use the mapped reads to update the reference
* Remap reads from original data to the new index
```
10000 reads; of these:
  10000 (100.00%) were paired; of these:
    403 (4.03%) aligned concordantly 0 times
    9597 (95.97%) aligned concordantly exactly 1 time
    0 (0.00%) aligned concordantly >1 times
    ----
    403 pairs aligned 0 times concordantly or discordantly; of these:
      806 mates make up the pairs; of these:
        749 (92.93%) aligned 0 times
        57 (7.07%) aligned exactly 1 time
        0 (0.00%) aligned >1 times
96.25% overall alignment rate
```



# MiCall
* Developed the lab pipeline as an open source project on GitHub - https://github.com/cfe-lab/MiCall
* Basic pipeline steps:
  1. Preliminary map of reads to standard reference genomes
  2. Adaptive re-mapping of reads
  3. Merge paired-end reads, convert to custom alignment format
  4. Count nucleotide, amino acid frequencies



# HIV genotyping with the MiSeq

* Every HIV RT sample in this run had ~3% E138A
* Quality scores for these bases were normal.
<center>
![Barplot of RT mutation frequencies](/img/mutation-barplot-v2.svg)
</center>



# Digging into the guts

* Every MiSeq run produces InterOp binary files that store diagnostic metrics
* `ErrorMetricsOut.bin` contains &phi;X174 error rates for each tile and cycle
* It looks like this:
```
7??=??&M7??=??`M7??=???M?>7??M???>a??MW??=&??M?>ݸ=M???>???M?	
?=D??M?j">??M???=ȷMw??=??M{?=h?N?a?>???N?Z>???N?+?=?N??=?8N?
U?=??gN??H>[??N?n>?:@>ŴYN	9iB>l??N?u>#??N
```



# Some Python gets you this:

```
tile,cycle,errorrate
1101,1,1.2627854347229004
1101,2,0.16267767548561096
1101,3,0.11590784043073654
1101,4,0.13420908153057098
1101,5,0.06303759664297104
1101,6,0.13217560946941376
1101,7,0.11184090375900269
1101,8,0.08337230980396271
1101,9,0.13217560946941376
```



# Some R gets you this:

![Bad cycles](/img/bad-cycles1.png)



# Censoring bad cycles removed E138A

* This problem is specific to amplicon sequencing applications.
* Because every read has the same position, a given cycle corresponds to the 
  same base in every read.
* When a selling point of NGS is sensitivity (~1%), this is a significant issue!



# Carry-over contamination

* Reads as many as 7 previous runs can appear in the current run
* Used modified PCR primer with extra T (TAATG, start 130926), 
  alternated primers between runs.
<center>![Measures of longitudinal run contamination](/img/carryover1.png)</center>
<small>LC Swenson et al., Tropism Testing by MiSeq Is Comparable to 454-Based 
Methods but Exhibits Contamination Issues; Abstract #611, Conference on Retroviruses and Opportunistic Infections, Boston, MA, March 3-6, 2014</small>



# Bleach fixes everything

* Eventually a revised wash protocol with bleach was [posted](https://drive.google.com/file/d/0B383TG7oJh2CTWp6MzZkMHBDd28/edit) by Illumina

<center>
![Reduction of longitudinal run contamination with bleach wash](/img/carryover2.png)
</center>



# Cross-contamination

<div id="left">
<ul>
  <li>
  Often the lab multiplexed samples on the same run with different targets
  </li>
  <li>
  Noticed hepatitis C virus (HCV) and human leukocyte antigen (HLA) samples 
   on the same run were seeping into each other
  </li>
</ul>
<small>
CJ Brumme et al. Abstract #592, Conference on Retroviruses 
 and Opportunistic Infections, Seattle, WA, February 23-26, 2015
</small>
</div>

<div id="right">
![](/img/cross-contamination1.png)
</div>




# Are shared indices the problem?

![](/img/cross-contamination.png)




# Summary: Is your machine lying to you?

* Unreported bad cycles
* Carryover contamination among runs
* Cross-contamination among samples
* Adapter, [&phi;X174 control](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4511556/) contamination



# Reproducibility

* A paper eventually submitted by a previous undergraduate intern was 
  returned for revision, over two years after the experiment.
* One of the reviewers asked for clarification on data processing.
* The 454 pipeline was developed under version control (svn)
* This was <u>completely worthless</u>.



# Which pipeline version ran the data?

* Yes, version control is valuable, but...
* Nothing in result files to indicate versioning.
* By date?  May have run with an older version.
* May have run with uncommitted changes.



# New accreditation requirements

* College of American Pathologists:
 
  <small>
  *"the specific version(s) of the bioinformatics pipeline used to 
  generate NGS data files [must be] traceable for each patient report"*
  </small>

* American College of Medical Genetics and Genomics:

  <small>
  *"The laboratory must also document the bioinformatics pipeline that 
  it uses in the analysis of NGS data and capture the specific version 
  of each component of the pipeline utilized in the analysis of each 
  patient test. <br><br>
  A system must be developed that allows the laboratory 
  to track software versions, the specific changes each version 
  incorporates, and the date the new version was implemented on clinical 
  samples."*
  </small>



# 
![](/img/desolate.jpg)



# Workflow management systems

* Automate pipeline execution
* Galaxy and Apache Taverna are popular WMSs
* Tracking origin of data is fragile
* Not convenient for handling multiple versions



# <center>![](/img/kive-logo.svg)</center>

* An open source [Django](https://www.djangoproject.com/) app (http://github.com/cfe-lab/Kive)
* A WMS for the development and maintenance of clinical pipelines
* Tracks every pipeline version and the origin of every data set



# How does it work?

* Take md5 checksum of every script and data set
* Normally used to verify integrity of file transfers
* Checksums are stored in the Kive database



# Kive demo



# Kive now tracks all MiSeq runs at CFE

* Roughly six MiSeq runs every week (two machines)
* Every new run is automatically processed with MiCall within Kive
* Any results file is permanently traceable to its source.
* Applied to Genome Canada for funding to support development.



# But the community doesn't want it

* <small>"*Bioinformatics is becoming increasingly a service industry and computing is 
  going towards the cloud. This proposal assumes local expertise and compute 
  infrastructure. It's old fashioned.*"</small>
  
* <small>"*Genomic clinical analysis doesn't need a graphical interface to 
  MD5-checksum'd pipelines.*"</small>



# Failures to launch

* Error and diversity are confounded for HIV -- difficult to overcome with bioinformatics
* Extreme sensitivity competes with error and sample contamination 
* Clinical labs are unprepared to address new CAP requirements for NGS-based assays

* <u>Technologies continue to evolve</u>



# Acknowledgements

* The laboratory results I have cited were obtained by my former colleagues at 
 the *BC Centre for Excellence in HIV/AIDS* 
 (Chanson J. Brumme, Luke C. Swenson, Hope Lapointe, P. Richard Harrigan)

<center>
![](/img/GenomeCanadaLogo.png) ![](/img/shim.png) ![](/img/cihr.png)
</center>