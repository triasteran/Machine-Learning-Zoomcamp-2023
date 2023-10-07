# building container based on conda 
FROM continuumio/miniconda3

# copy conda environment file 
COPY conda_env.yml .

# create conda environment 
RUN conda env create -f conda_env.yml

# activate conda environment 
RUN echo "conda activate MLmodel" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

RUN echo "conda environment is activated, scipy version is"
RUN python -c "import scipy"

# set workdir as app/
WORKDIR /app

# copy model, script for prediction to workdir 
COPY ["predict.py", "model.bin", "./"]

# make this port visible 
EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]