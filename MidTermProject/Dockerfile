# building container based on conda 
FROM continuumio/miniconda3

# copy conda environment file 
COPY conda_env.yml .

# create conda environment 
RUN conda config --add channels anaconda 
RUN conda env create -f conda_env.yml

SHELL ["conda", "run", "--no-capture-output", "-n", "myenv", "/bin/bash", "-c"]

# set workdir as app/
WORKDIR /app

# copy model, script for prediction to workdir 
COPY ["predict.py", "model.C=1.n=130.bin", "./"]

# make this port visible 
EXPOSE 9696

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "myenv", "gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
