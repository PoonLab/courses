# Computational Pathology

# What is computational pathology?
* It can be defined in a few ways
  * Using raw data to aide diagnosis of patients
    * Electronic medical records
    * Laboratory data
    * Radiology/pathology imaging
  * Data can be used to derive biologically and clinically applicable findings
  * Using mathematical models to produce inferences and predictions about diagnosis 
  * Overall, using computational methods to improve health care 

# When can computational pathology be utilized?
*	Advanced determination of disease possibility
* Disease trends in populations
* Cost-benefit analysis of treatment in the health care system
* For creating jobs in data-related research in the health care system
* Using computational methods when determining the optimal selection of patients in clinical trials 

# What kind of impact does computational pathology have on research?
* Creating algorithms used for diagnosing disease
* More appropriate selection of therapy
* Aides in prediction of patient outcomes
* In case of cancer analysis:
  * Databases can be made containing cancer genetics, genomics, proteomics, metabolomics, epigenetics, glcomics and exposomes
  * Tumor and stromal architectures
  * Immune interactions in cancer cases

# Current work in Computational Pathology
* Examples include:
  * Physiological and pathological population dynamics of circulating human red blood cells
   * John M. Higgins and L. Mahadevan
  * Computational models of liver fibrosis progression for hepatitis C virus chronic infection
   * James Lara, F. Xavier Lopez-Labrador, Fernando Gonzalez-Candelas, Marina Berenguer, Yury E. Khadyakov
  * Predicting Functional Effect of Human Missense Mutations Using PolyPhen-2
   * Ivan Adzhubei, Daniel M. Jordan, Shamil R. Sunyaev
  * Automated screening for myelodysplastic syndromes through analysis of complete blood count and cell population data parameters
   *  Phillipp W. Raess, Gert-Jan M. van de Geijn, Tjin L. Njo, Boudewijn Klop, Dmitry Sukhachev, Gerald Wertheim, Tom McAleer, Stepen R. Master and Adam Bagg

# Physiological and pathological population dynamics of circulataing human red blood cells
## Overview
* Made use of the hospital clinical lab and statistical physics to establish a master equation model for red blood cell maturation and clearance
* The model can be used to identify patients with anemia and can be used to discern iron-deficiency anemia from thalassemia-trait anemia (having smaller than normal red blood cells, resulting in anemia)
* The model can also determine patients that may be anemic several weeks before the anemia can be detectable
* This study is a prime example of how we can use clinical laboratory data to perform a direct test on human pathophysiology
* Daily, ~2.5x10^11 new RBCs are released from the bone marrow into the peripheral circulation, and continue to undergo an accelerated decline in volume and hemoglobin within a few days
* Subsequently, a longer period of slower decline occurs, and the volume and hemoglobin are coregulated

## Results
* This study compares the probability distributions of reticulocytes (immature RBCs) and the mature RBCs circulating in the blood and found that the correlation between volume and hemoglobin content increases as the cells mature
 * Correlation coefficient of ~0.40 for the reticulocyte population and ~0.85 for the full population
* This indicates that most RBCs mature in a way that its hemoglobin concentration leans toward the Mean Corpuscular Hemoglobin Concentration (MCHC)
 * Note: MCHC is a measure of the concentration of haemoglobin in a given volume of packed RBCs
* This comparison shows a lower variation than that of volume/hemoglobin content. 
* Insert Figures!

# Computational models of liver fibrosis progression for hepatitis C virus chronic infection
## Overview
* Chronic hepatitis C virus infections puts patients more at risk for liver diseases (ie. fibrosis, cirrhosis and hepatocellular carcinoma)
* It was hypothesized that genetic heterogeneity (genetic heterogeneity refers to the presence of a variety of genetic defects which cause the same disease, often due to mutations at different loci on the same gene, a finding common to many human diseases) of HCV was associated with liver disease
* This study reports the benefits of sequences from 3 HCV 1b genomic regions
 * Core, NS3 and NS5b
* These sequences were uesd to recognize viral geneic markers that are associated with the fast and slow rate of fibrosis progression (RFP)

## Results 
* Using machine-learning techniques, linear projections (LP) and Bayesian Networks (BN), the associations between the HCV sequences and RFP could be assessed
* A number of RFP-relevant HCV sites were identified
* Computational models were used and parameterized using the identified sites that associatd HCV strains with RFP in 70/30 split cross-validation (90-95% accuracy) and in validation tests (85-90% accuracy)
* It was determined that the RFP-relevant genetic markers identified in the Hepatitis C Core, NS3 and NS5b genomic regions, and may be useful to forsee RFP (disregarding the transplant status of the patients)
* From computational methods, it was determined that there is a strong genetic association to RFP and suggests that HCV genetic heterogeneity has a measurable effect on the severity of liver disease
* Furthermore, genetic assays can be developed for measuring virulence of HCV strains in clinical/public health settings







