# MidTermProject: classification of leukemia types using gene expression data  

## Project Description and some terminology 

First, I searched articles where interesting datasets are described. 
I was thinking about some biological data since I'm working as a bioinformatician. 
Currently, my area of exprertise is translatomics, however, I used to have some basic experience with cancer transcriptomics data. 

I decided to go with the dataset containing the aggregation of microarray gene expression data of leukemia patients from CuMiDa (available in a raw form here: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE9476 and procesed form here: https://sbcb.inf.ufrgs.br/cumida). 

Let's begin with some basic terminology. 

Gene expression is the process by which the information encoded in a gene (region of DNA) is turned into a function; this happens via <i>transcription</i> when RNA is syntesized based on the DNA matrix and then <i>translation</i> when proteins are generated based on RNA matrix (some RNAs are non-protein-coding and perform other functions). Analysis of gene expression allows us to know how abundant certain RNAs or/and proteins are in a cell. Gene expression of healthy cell is not the same as gene expression of tumour cell: some genes are transcribed and translated more or less efficiently. 

Microarray gene expression data is a relatively old technology for detection of gene expression, now it's widely replaced with RNA-seq (transcriptomics). 
There are still plenty of microarray data which can be reused and give insights into biological mechanisms of health and disease. DNA microarrays are microscope slides that are printed with thousands of tiny spots in defined positions, with each spot containing a known DNA sequence (e.g. of certain gene). The DNA molecules attached to each slide act as probes to detect gene expression: they bind single-stranded DNA molecules (those DNA molecules are derived from cellular RNAs) labeled with a fluorescent probe based on complementarity principle. Then, expression is measured based on the level of fluorescence signal.  Here is the schematic represantation of the process: 
![image](https://github.com/triasteran/Machine-Learning-Zoomcamp-2023/assets/47274795/71a7a120-a612-43fa-b3fd-4e8983887677)

This project is about using thousands gene expression data from hundreds of patients to detect different leukemia types. Leukemia is a broad term for cancers of the blood cells. The type of leukemia depends on the type of blood cell that becomes cancer and whether it grows quickly or slowly. Treatment and prognosis depends on a type, so being able to distinguish between leukimia types using gene expression data is a very important step that can help patients to receive a suitable and timely treatment. 

---------------------------------------------------------------------------------------------------------------------------------------------------------

## Structure of the repository

* README.md
* notebook.ipynb
* train.py
* predict.py
* Dockerfile

ML model is organised in a following framework (except, maybe, wrapping up in a cloud): 

![Untitled presentation (1)](https://github.com/triasteran/Machine-Learning-Zoomcamp-2023/assets/47274795/d8754caa-fe6f-4b4b-8a64-24ce7f0cfee1)


## Instructions on how to run the project

First, you need to build docker image using this command (in the same directory where Dockerfile is). This would take ~5minutes. 
```
docker build -t ml .
```

Then, you can run the docker container with gunicorn server using this command: 
```
docker run -it --rm -p 9696:9696 ml
```

In parallel, you can test the model by typing this command: 
```
python python predict-test.py
```

Expected output: 
```
{'class_number': 4.0, 'probability_of_class': 0.999847939746374, 'subtype': 'B-CELL_ALL_MLL'}
{'class_number': 2.0, 'probability_of_class': 0.9999315880097102, 'subtype': 'B-CELL_ALL_HYPERDIP'}
{'class_number': 3.0, 'probability_of_class': 0.998557557184204, 'subtype': 'B-CELL_ALL_HYPO'}
{'class_number': 5.0, 'probability_of_class': 0.9998561615581214, 'subtype': 'B-CELL_ALL_T-ALL'}
{'class_number': 1.0, 'probability_of_class': 0.9999967231199175, 'subtype': 'B-CELL_ALL_ETV6-RUNX1'}
```

