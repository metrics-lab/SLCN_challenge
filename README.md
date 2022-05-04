# SLCN Challenge - MICCAI 2022

Example of docker container for the SLCN challenge organised as part of the MLCN 2022 workshop, satellite event of the MICCAI 2022. 

# Create DockerFile

coming soon

# Build docker image

coming soon

# Run docker command

coming soon



Introduction
The test set won't be released to the challenge participants. For this reason, participants must containerise their methods with Docker and submit their docker container for evaluation on the test set. Your code won't be shared and will be only used internally by the SLCN organisers.

Docker allows for running an algorithm in an isolated environment called a container.  In particular, this container will locally replicate your pipeline requirements and execute your inference script.

Design your inference script
The inference will be automatically performed using Docker. More specifically, a  command will be executed when your Docker container is run (example: `python3 run_inference.py`), for each of the tasks. 

The command must run the inference on the test set. The test set will be mounted into /input and the results must be saved in /output.  The folder /input will contain all the test metric files in the format [id]_[sess]_{left,right}.shape.gii.  For both tasks, the participant script must save the prediction results in the /output with a CSV file with two columns, one for the predictions, and one for the target values: for example /output/results_birth_age.csv

We provide a script example here.

Create your Docker Container
Docker is commonly used to encapsulate algorithms and their dependencies. In this section, we list four steps you will have to follow in order to create your docker image so that it is ready for submission.

Firstly, you will need to install Docker. The NVIDIA Container Toolkit is also required to use CUDA within docker containers. Secondly, you will need to create your own image. Docker can build images by reading the instructions from a Dockerfile. Detailed explanations are provided here. Many images are available online and can be used as a base image. We recommend pulling from the NVIDIA images for models requiring a GPU (e.g., Tensorflow, PyTorch).

Please look at the SLCN Docker container example on Github.

In a nutshell, Dockerfile allows for:

Pulling a pre-existing image with an operating system and, if needed, CUDA (FROM instruction).
Installing additional dependencies (RUN instructions).
Transfer local files into your Docker image (COPY instructions).
Executing your algorithm (CMD  and ENTRYPOINT instructions).
Dockerfile example:

## Pull from existing image
FROM nvcr.io/nvidia/pytorch:21.05-py3
## Copy requirements
COPY ./requirements.txt .

## Install Python packages in Docker image
RUN pip3 install -r requirements.txt

## Copy all files (here "./src/run_inference.py")
COPY ./ ./
## Execute the inference command 
CMD ["./src/run_inference.py"]
ENTRYPOINT ["python3"]
Thirdly, you can build your docker image:

docker build -f Dockerfile -t [your image name] .
Fourthly, you will upload your image to Docker Hub. Instructions can be found here:

docker push [your image name]
Docker commands
Your container will be run with the following command:

docker run --rm -v [input directory]:/input/:ro -v [output directory]:/output -it [your image name]
[input directory] will be the absolute path of our directory containing the test set, [output directory] will be the absolute path of the prediction directory and [your image name] is the name of your Docker image.

Test your Docker container
To test your docker container, you will have to run your Docker container and perform inference using the validation set. We recommend you test your Docker container prior to submission. 

Firstly, create a folder containing the validation set.

Run:

docker run --rm -v [validation set folder]:/input/:ro -v [output directory]:/output -it [your image name]