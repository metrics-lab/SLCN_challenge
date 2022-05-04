# SLCN Challenge 2022 - Docker submission example

Credits: S. Dahan, LZJ. Williams

This repository provides a reference Docker algorithm container for a SLCN 2022 Challenge submission, on the grand-challenge plateform. 

It should serve as an example or/and a template for your own algorithm container implementaion, on Linux/MacOS. 

Here, a [Surface Vision Transformer](https://arxiv.org/abs/2203.16414) (SiT) model is used for the task of birth age prediction as an example. Code is based on this [Github](https://github.com/metrics-lab/surface-vision-transformers).

More information about algorithm container and submission can be found [here](https://grand-challenge.org/blogs/create-an-algorithm/). 

## Content:
1. [Prerequisites](#prerequisites)
2. [Overview of the project structure](#overview)
3. [Requirements for Grand Challenge submission (input/output)](#requirements)
4. [Build, test and export your algorithm container](#container)
4. [Tips and general advice](#advice)
5. [Contacts](#contact)
6. [Acknowledgements](#acknowledgments)


## 1. Prerequisites <a name="prerequisites"></a>

Submissions are based on Docker containers and the evalutils library (provided by Grand-Challenge).

First, you will need to install localy [Docker](https://www.docker.com/get-started).

Then, you will need to install evalutils, that you can pip install: 

```
pip install evalutils
```

Optional: To have GPU support for local testing, you want to install the [NVIDIA container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html).

## 2. Overview of the project structure <a name="overview"></a>


The structure of this repository is based on the Algorithm Container for Classification in evalutils. 

You can either start a project from scratch by following guidelines in [evalutils documentation](https://comic.github.io/evalutils/usage.html#algorithm-container) or by cloning this repository and make the appropriate modifications: 

```
git clone https://github.com/metrics-lab/SLCN_challenge
```

Remark: As evalutils does not implement a class for Regression problem, we only adapted the Classification class to the case of regression problems. 

No matter what methods you used to start your project (evalutils or cloning this repo), you should have at least the following files in your project repository: 

```
.
└── slcn_project
    ├── Dockerfile               # Defines how to build your algorithm container    
    ├── build.sh                 # Builds your algorithm container
    ├── test.sh                  # A script that runs your algorithm container using the example in ./test 
    ├── .gitignore               # Define which files git should ignore (optional)
    ├── process.py               # Contains your algorithm code - this is where you will extend the BaseAlgorithm class
    ├── README.md                # For describing your algorithm to others
    ├── requirements.txt         # The python dependencies of your algorithm container - add any new 
    ├── test                     # A folder that contains an example test image for testing
    │   ├── <uid>.mha            # An example image for the dataset (converted into .mha)
    │   └── expected_output.json # Output file expected to be produced by the algorithm container
```

The Dockerfile 


## 3. Requirements for Grand Challenge submissions (input/output) <a name="requirements"></a>

You Docker container (via process.py) is supposed to read .mha image files. 

Important: Images will be read successively and predictions will be made one by one, ie there will be one birth-age.json file per predicition. 

## 4. Build, test and export your algorithm container <a name="container"></a>

First you should try to build your docker image.

```
bash build.sh
```

This will install all required libraries and copy files and folders into the docker container. 

Then, the testing script will build your container (again), run the process.py script and check if the ./output/birth-age.json is similar to the ./test/expected-output.json

```
bash test.sh
```

Finally, once your algorithm container is working, you can export it as a .tar file for submission with

```
bash export.sh
```

## 4. Tips and general advice <a name="advice"></a>

To remove all unused docker images you can use

```
docker image prune -y 
```

## 4. Contacts <a name="contacts"></a>

Please email slcn.challenge@gmail.com if you have any questions on slcn submissions, or open an issue. 

## 5. Acknowledgements <a name="acknowledgements"></a>

The repository is greatly inspired from [MIDOG_reference_docker](https://github.com/DeepPathology/MIDOG_reference_docker).


The code for Surface Vision Transformer is from [surface-vision-transformers](https://github.com/metrics-lab/surface-vision-transformers).