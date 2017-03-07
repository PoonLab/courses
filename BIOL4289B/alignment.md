# The diversity of viruses
## Art Poon
### BIOL 4289B - Biosystematics and Phylogenetics

---

# Viruses matter

* Not classified as "alive" (no metabolism, no translation)
* Viruses evolve
* Have significant impact on the fitness of organisms
* Have signifcant impact on the environments of living things

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
* Substitution matrices
* BLAST
* Gap penalties
* Affine penalties - gap open and extension
* Global versus local alignment (terminal gap penalties)
* Multiple sequence alignment - why this is difficult
* Guide trees
* Iterative alignment
* Short read mappers

---

# Pairwise alignment

* An alignment is a hypothesis about how components of two sequences are descended from a common ancestor.
* Generally two reasons this is can be difficult:
  1. Locating the overlap
  2. Insertion/deletion (indel) differences

---

# Defining a cost function



---


* Inexact matches - we should weight them differently.
* *e.g.*, transitions occur more often than transversions.

---





