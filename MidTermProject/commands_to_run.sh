# create an image from Dockerfile
docker build -t MLimage:v1 .

# Run server in docker container using MLimage:v1 image 
docker run -it --rm -p 9696:9696 MLimage:v1