# Understanding-SNPs-in-CFTR

## Using the Code

First, install the requirements with "pip install -r requirements.txt"

Next, create the labeled_data files if they are not already created. This can be done with "python3 data/data_preprocessing.py"

From here, you should be able to simply run through the different Jupyter notebooks.

### Data Exploration

This file just gives a basic visualization of the data.

![2dvisualization](https://github.com/riensou/Understanding-SNPs-in-CFTR/assets/90002238/e1ab56a8-f77c-48c1-b827-ea5716139382)

![3dvisualization](https://github.com/riensou/Understanding-SNPs-in-CFTR/assets/90002238/ed1bc5c5-26ac-4db5-b659-5e48c7393b36)

### Linear Regression

Linear regression achieves a Pearson correlation coefficient of about 0.33. However, notably the $R^2$ score is very negative.

### Neural Network

While neural networks are able to achieve an $R^2$ score close to 1 on the training data, the model clearly overfits as the evaluation data is abysmal. 

## Background Information

The following information comes from this [presentation](https://docs.google.com/presentation/d/1xDa77zjvDh7jVBC_ELAdq0k8Vi6ywfcTHIMnW115LP4/edit?usp=sharing).

ABC Transporters:
- CFTR belongs to the ATP binding cassette (ABC) transporter superfamily
- ABC transporters: proteins that use ATP to move substrates across cell membranes

<img width="622" alt="2023-09-23_13-11-20" src="https://github.com/riensou/Understanding-SNPs-in-CFTR/assets/90002238/968a0a65-ba94-4d13-93cc-7e8fb8e394a3">

Cystic Fibrosis Transmembrane Conductance Regulator (CFTR):
- Located on chromosome 7 (7q31.2)
- 1480 residues
- Function: conduct chloride ions across cell membranes down their electrochemical gradient, regulate sodium and bicarbonate channels

<img width="447" alt="2023-09-23_13-13-06" src="https://github.com/riensou/Understanding-SNPs-in-CFTR/assets/90002238/ad45771a-f78c-440a-9886-cade1260260d">

Architecture of CFTR:
- 2 transmembrane domains (TMD1 & TMD2)
- 2 cytosolic nucleotide binding domains (NBD1 & NBD2)
- Regulatory domain (R-domain)

Cystic Fibrosis:
- Recessive disease caused by loss-of-function mutations in the CFTR protein
- Delta 508: deletion of Phenylalanine 508 → severe folding defect
- Defects in the CFTR protein leads to a buildup of thick mucus in airways - mostly affecting the lungs and pancreas
- Cystic fibrosis increases one’s susceptibility to developing infections
- There is no cure for this genetic condition but treatments are used to mitigate symptoms

