# CapStoneProject1: Image classification of leukemia and normal cells 

## Project description 
I decided to continue on the topic of leukemia (like I did in the MidTermProject), but this time it is binary image classification of normal and leukemic cells. Acute lymphoblastic leukemia (ALL) is the most common type of childhood cancer and accounts for approximately 25% of the pediatric cancers. 
It is important to be able to diagnose it at early stages. The task is to distinguish between normal cells and immature leukemic blasts using images obtained with microscope. It is quite challenging task for researcher because cells share morphological similarity. 

The data are available at https://www.kaggle.com/datasets/andrewmvd/leukemia-classification. 

Let's have a look at the examples of classes. 

<table>
<tr>
<th> ![image](https://raw.githubusercontent.com/triasteran/Machine-Learning-Zoomcamp-2023/main/CapstoneProject1/tests/UID_78_9_7_all.bmp) </th>
<th> ![image](https://raw.githubusercontent.com/triasteran/Machine-Learning-Zoomcamp-2023/main/CapstoneProject1/tests/UID_H48_16_13_hem.bmp) </th>
</tr>
<tr>
<td>



In this project I'll be training CNN-based models and other standard ML models. 

---------------------------------------------------------------------------------------------------------------------------------------------------------

## Structure of the repository

* <b>README.md</b>. You are reading it now; it contains description of the project, provides links to dataset and instructions how to run the dockerised ML model. 
* <b>notebook.ipynb</b>. It contains code for data processing and model development 
* <b>train.py</b>. It contains training the final model and saving it 
* <b>predict.py</b>. It loads the model and serve it via a web serice (Flask)
* <b>predict_test.py</b>. It contains code for testing the model
* <b>conda_env.yml</b>. It is conda environment for specifying packages and versions 
* <b>Dockerfile</b>. It contains receipy for docker container

The final model turned out to weigh more than 25Mb which (allowed for github upload), therefore I do not have it here.  
Therefore if you want to repeat the pipeline, you will need to run the train.py first which will save the model (e.g. with name X) and 
then you can add the model name to the Docker file before building an image and also add it to predict.py script. 

---------------------------------------------------------------------------------------------------------------------------------------------------------

## Instructions on how to run the project

First, you can download the content of the github dir by using this command: 
```
git clone ... 
```

Next, after you changed to the downloaded directory with Dockerfile, you need to build docker image using this command. This would take ~5minutes. 
```
docker build -t ml .
```

Then, you can run the docker container with gunicorn server using this command: 
```
docker run -it --rm -p 9696:9696 ml
```

In parallel, you can test the model by typing this command: 
```
python python predict_test.py
```

This it the expected output: 
```
expected class: ALL {'all': '0.9530534744262695', 'hem': '0.046946526'}
expected class: HEM {'all': '0.20552486181259155', 'hem': '0.79447514'}
```


