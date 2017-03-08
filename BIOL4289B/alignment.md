# The diversity of viruses
## Art Poon
### BIOL 4289B - Biosystematics and Phylogenetics

---

# Viruses matter

* Are viruses alive? (no metabolism, no translation)
* Viruses evolve.
* Have significant impacts on the fitness of organisms.
* Important components of ecosystems.

<center>![https://what-if.xkcd.com/80/](virus_mountain.png)</center>

---

# Origin of viruses

* Progressive hypothesis:  viruses evolved from mobile genetic elements

* Regressive hypothesis:  viruses descended from intracellular parasites

* Virus-first hypothesis:  viruses are a basal lineage from an RNA world ancestor

<small>Source: http://www.nature.com/scitable/topicpage/the-origins-of-viruses-14398218</small>

---

# What is a virus species?

* There is no genetic homology across all viruses like 16S rRNA
* Virus diversity organised by nucleic acid (Baltimore classification)
* International Committee on Taxonomy of Viruses requires virus species to be distinguished by multiple criteria
* A recent consensus statement published in [*Nature Reviews Microbiology*](http://www.nature.com/nrmicro/journal/vaop/ncurrent/full/nrmicro.2016.177.html) argues that a distinct genetic type should be sufficient to name a new species

---

# dsDNA viruses

<table>
<tr>
    <td width="60%">
        <h2>T4 bacteriophage, <i>Myoviridae</i></h2>
        <ul>
            <li>Head-tail structure</li>
            <li>T4, 169 kb genome, about 300 ORFs</li>
            <li>Contractile sheath injects virus genome into cell through non-contractile tube</li>
            <li><b>Cyanophages</b>, infect cyanobacteria, encode photosynthesis proteins</li>
        </ul>
    </td>
    <td>
        <img src="/img/t4-bacteriophage.jpg">
    </td>
</tr>
</table>

---

# dsDNA viruses
## Mimivirus, *Mimiviridae*

<table>
<tr>
    <td width="60%">
        <ul>
            <li>First observed in 1992</li>
            <li>One of largest known viruses, up to 750nm in diameter</li>
            <li>Amoebae are natural hosts</li>
            <li>1.2Mb genome, about 900 predicted genes</li>
            <li>Genes with homology to organismal "housekeeping" genes</li>
        </ul>
    </td>
    <td>
        <img src="/img/mimivirus.png">
    </td>
</tr>
</table>

---

# dsDNA viruses
## Zamilon virophage, *Lavidaviridae*

<table>
<tr>
    <td width="60%">
        <ul>
            <li>"Parasite" of Mimivirus, replicates within "virus factory" formed by its host virus</li>
            <li>Discovered in 2013</li>
            <li>Genome encodes 20 ORFs, 3 homologous to Mimivirus</li>
            <li>Other virophages have deleterious effect on host virus</li>
        </ul>
    </td>
    <td>
        <img src="/img/zamilon-virophage.jpg">
    </td>
</tr>
</table>

---

<table>
<tr>
    <td width="55%">
        <h1>dsDNA viruses</h1>
        <h2>Crenarchael viruses, multiple</h2>
        <ul>
            <li>Hyperthermophiles, isolated from acidic hot (even near-boiling) springs</li>
            <li>Highly diverse morphologies, some unique to archaeal viruses</li>
            <li>Rods, filaments, spindles, "bottles", "bullets"</li>
        </ul>
        <small>Source: Prangishvili 2013, Ann Rev Microbiol 67: 565-585
    </td>
    <td>
        <img src="/img/mi670565.f2.jpeg">
    </td>
</tr>
</table>


---

# ssDNA viruses
## &phi;X174, *Microviridae*

<table>
<tr>
    <td width="60%">
        <ul>
            <li>Infects E.~coli</li>
            <li>The first genome sequence</li>
            <li>Circular genome, 5386 bases encoding 11 genes</li>
            <li>Injects its DNA into host cell through spike protein</li>
        </ul>
    </td>
    <td>
        <img src="/img/phiX174.png">
    </td>
</tr>
</table>

---

# ssDNA viruses
## Torque teno virus, *Anelloviridae*

<table>
<tr>
    <td width="55%">
        <ul>
            <li>First isolated in 1997</li>
            <li>Circular genome, about 3.8 kb</li>
            <li>Roughly half of human population infected</li>
            <li>Many possible modes of transmission, reason for ubiquity unknown</li>
            <li>Unusually high mutation rate</li>
        </ul>
    </td>
    <td>
        <img src="/img/TTV-prevalence.png">
    </td>
</tr>
</table>

---

# (+)ssRNA viruses
## Zika virus, *Flaviviridae*

<table>
<tr>
    <td width="55%">
        <ul>
            <li>Arthropod-borne virus (arbovirus)</li>
            <li>Infection during pregnancy a cause of microcephaly</li>
            <li>[100 new genome sequences](http://biorxiv.org/content/early/2017/02/18/109348) suggests multiple introductions from Brazil to Caribbean islands, US</li>
        </ul>
    </td>
    <td>
        <img src="/img/Zika-chain-colored.png">
    </td>
</tr>
</table>

---

# (-)ssRNA viruses

<table>
<tr>
    <td width="55%">
        <h2>Ebolavirus, <i>Filoviridae</i></h2>
        <ul>
            <li>West African outbreak, over 11,000 deaths</li>
            <li>Five known species, varying pathogenicity</li>
            <li>Filaments uniform diameter, length varies with genome number</li>
            <li>Hemorrhagic fever, average fatality rate 78%</li>
        </ul>
    </td>
    <td>
        <img src="/img/ebola-TEM.jpg">
    </td>
</tr>
</table>

---

# RNA reverse-transcribing viruses
## Human immunodeficiency virus, *Retroviridae*

<table>
<tr>
    <td width="55%">
        <ul>
            <li>At least three introductions from non-human primates into human population.</li>
            <li>One of the fastest rates of adaptation ever measured.</li>
            <li>Virus carries two copies of RNA genome.</li>
        </ul>
        <small>Source: https://depts.washington.edu/jaisril/microscopy/</small>
    </td>
    <td>
        <img src="/img/hiv-em1.jpg">
    </td>
</tr>
</table>

---

# Sequence alignment
## Learning objectives
<table>
<tr>
<td>
<ul>
<li>Substitution matrices</li>
<li>Gap penalties</li>
<li>Affine penalties - gap open and extension</li>
<li>Global versus local alignment (terminal gap penalties)</li>
</ul>
</td>
<td>
<ul>
 <li>Multiple sequence alignment - why this is difficult
 <li>Guide trees</li>
 <li>Iterative alignment</li>
 <li>Short read mappers</li>
</ul>
</td>
</tr>
</table>


---

# Pairwise alignment

* An alignment is a hypothesis about how residues of two sequences are descended from a common ancestor.
* Generally two problems to solve:
  1. Locating the overlap
  ```
    ACGTAGGAA  >>  ACGTAGGAA
    CGTACG     >>  -CGTACG--
  ```

  2. Insertion/deletion (indel) differences
  ```
    ACGTAGGAA   >>  ACGTAGG--AA
    ACGACGTTAA  >>  ACG-ACGTTAA
  ```

---

# Exact solution is too difficult

* Thorne-Kishino-Felsenstein (1991; TKF91)
* Explicit model reconstructing ancestral insertion and deletion events
  ```
  ACGTAG  >>  AC-TAG  >>  ACTA[GC]G
  ACTGTAG  >>  ACTGTAG[CG]  >>  ACT--AGCG
  ```
* Not feasible for data sets of even modest size
* Instead we almost always use a "heuristic" algorithm

---

# Substitution matrices

* First developed by Dr. Margaret Dayhoff (PAM matrices)
* *e.g.*, BLOSUM62, an empirical model of how often specific substitutions are expected to occur:
  ```
      Ala  Cys  Trp  Val
  Ala   4    0   -3    0
  Cys   0    9   -2   -1
  Trp  -3   -2   11   -3
  Val   0   -1   -3    4
  ```
`$$ S_{ij} = \log\frac{p_{ij}}{q_i q_j}$$` where $p_{ij}$ is observed pairs and $q_i$ is overall frequency of residue $i$

---

# Gap penalties

* There has to be some cost to indels or else:
  ```
  ACACACAC    ACACACAC    ACACACAC
  ACAC----    AC----AC    A--CA--C
  ```
  will be scored the same.
* Generally every gap incurs some cost to an alignment.

---

# Affine gap penalties

* Linear gap penalty: Each gap has the same cost
* Affine gap penalty:  "Opening" a gap incurs some cost $u$, and extending the gap incurs a linear cost at some rate $v$.
$$W(l) = u + v\times l$$
* So if $u=10$ and $v=1$:
  ```
  ACACACAC    ACACACAC    ACACACAC
  ACAC----    AC----AC    A--CA--C
    -14         -14         -24
  ```

---

# Global vs. local

* Do you expect your sequences to align end-to-end, or is there incomplete coverage?
* Local alignment ignores "terminal" gaps at the start or end of an aligned sequence:
  ```
  ACACACAC    ACACACAC    ACACACAC
  ACAC----    AC----AC    A--CA--C
     0          -14         -24
  ```

---

# Solving it

* The cost function defines one or more alignments that minimize cost
* Finding these alignments is made efficient with a "dynamic programming" algorithm.
* *e.g.*, Needleman-Wunsch, Smith-Waterman, Gotoh
* Breaks down problem into small pieces, computes each piece once, and then looks up stored solutions for later computation

---

# Multiple sequence alignment

* Difficult to scale up pairwise alignment to many sequences
* Aligning sequence B to A and C to A does not align B and C:
  ```
  A: ACG-T   A: ACGT   B: ACGGT
  B: ACGGT   C: AC-T   C: AC-T
  ```
* We need some scheme for applying pairwise alignment to a set of sequences

---

# Guide trees

* Progressively build up an MSA
* Start with the most similar pair of sequences based on some alignment-free measure
* Alignments are propagated back up the tree
* Iterative alignment -- reconstruct a new guide tree from the previous iteration's MSA

---

# Software

* [CLUSTALW](http://www.clustal.org)
* [T-COFFEE](http://www.tcoffee.org/Projects/tcoffee/)
* [MUSCLE](http://www.drive5.com/muscle)
* [MAFFT](http://mafft.cbrc.jp/alignment/software/)
* [PRANK](http://www.ebi.ac.uk/goldman-srv/prank/prank/)

---

# Alignment of next-generation sequence data

* The output of NGS platforms is enormous
* Standard MSA methods are too slow!
* There are dozens of programs available

<small>Source: https://academic.oup.com/bioinformatics/article/28/24/3169/245777/Tools-for-mapping-high-throughput-sequencing-data</source>

---

# Short read mapping

* Build an index (hash table) of one or more reference genomes
* A hash function efficiently reduces a complex object to a relatively simple value
* *e.g.*, count the number of G's in a stretch of 20 bases
* Map short read to reference by index look-up


