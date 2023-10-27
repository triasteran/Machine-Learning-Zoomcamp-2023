# MidTermProject: classification of leukemia types using gene expression data  

## Project Description and some terminology 

First, I searched articles where interesting datasets are described. 
I was thinking about some biological data since I'm working as a bioinformatician. 
Currently, my area of exprertise is translatomics, however, I used to have some basic experience with cancer transcriptomics data. 

I decided to go with the dataset containing the aggregation of microarray gene expression data of leukemia patients from CuMiDa (available in a raw reads form here: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE9476 and procesed form here: https://sbcb.inf.ufrgs.br/cumida). 

Let's begin with some basic terminology. 

Gene expression is the process by which the information encoded in a gene (region of DNA) is turned into a function; this happens via <i>transcription</i> when RNA is syntesized based on the DNA matrix and then <i>translation</i> when proteins are generated based on RNA matrix (some RNAs are non-protein-coding and perform other functions). Analysis of gene expression allows us to know how abundant certain RNAs or/and proteins are in a cell. Gene expression of healthy cell is not the same as gene expression of tumour cell: some genes are transcribed and translated more or less efficiently. 

Microarray gene expression data is a relatively old technology for detection of gene expression, now it's widely replaced with RNA-seq (transcriptomics). 
There are still plenty of microarray data which can be reused and give insights into biological mechanisms of health and disease. DNA microarrays are microscope slides that are printed with thousands of tiny spots in defined positions, with each spot containing a known DNA sequence (e.g. of certain gene). The DNA molecules attached to each slide act as probes to detect gene expression: they bind single-stranded DNA molecules (those DNA molecules are derived from cellular RNAs) labeled with a fluorescent probe based on complementarity principle. Then, expression is measured based on the level of fluorescence signal.  Here is the schematic represantation of the process: 
![image](https://github.com/triasteran/Machine-Learning-Zoomcamp-2023/assets/47274795/71a7a120-a612-43fa-b3fd-4e8983887677)

This project is about using thousands gene expression data from hundreds of patients to detect different leukemia types. Leukemia is a broad term for cancers of the blood cells. The type of leukemia depends on the type of blood cell that becomes cancer and whether it grows quickly or slowly. Treatment and prognosis depends on a type, so being able to distinguish between leukimia types using gene expression data is a very important step that can help patients to receive a suitable and timely treatment. 

---------------------------------------------------------------------------------------------------------------------------------------------------------

## Structure of the repository

* <b>README.md</b>. You are reading it now; it contains description of the project, provides links to dataset and instructions how to run the dockerised ML model. 
* <b>notebook_v1.ipynb</b>. It contains code for data processing, visualisation and model development 
* <b>train.py</b>. It contains GridSearchCV for parameters tuning and training the final model and saving it using pickle library (to the file model.C=1.n=130.bin)
* <b>model.C=1.n=130.bin</b> saved ML model  
* <b>predict.py</b>. It loads the model and serve it via a web serice (Flask)
* <b>predict-test.py</b>. It contains code for testing the model
* <b>conda_env.yml</b>. It is conda environment for specifying packages and versions 
* <b>Dockerfile</b>. It contains receipy for docker container
* <b>B-CELL_ALL_ETV6-RUNX1.json, B-CELL_ALL_HYPERDIP.json, B-CELL_ALL_HYPO.json, B-CELL_ALL_MLL.json, B-CELL_ALL_T-ALL.json</b> These are json files containing test dictionaries that are used in predict-test.py; their names corrspond to their True classes 



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
![Screenshot from 2023-10-08 19-07-25](https://github.com/triasteran/Machine-Learning-Zoomcamp-2023/assets/47274795/1e5309d9-c689-4501-929a-70e46c2842bd)


In parallel, you can test the model by typing this command: 
```
python python predict-test.py
```
![Screenshot from 2023-10-08 19-07-48](https://github.com/triasteran/Machine-Learning-Zoomcamp-2023/assets/47274795/fcee1ef0-8113-41d1-a6d1-16b573d0883d)



