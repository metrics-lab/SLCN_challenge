# SLCN Challenge 2022 - Docker submission example

Credits: S. Dahan, LZJ. Williams

This repository provides a reference Docker algorithm container for SLCN 2022 Challenge submissions.

It should serve as an example or/and a template for your own algorithm container implementation, on Linux/MacOS, for submission on the grand-challenge plateform. 

Here, a [Surface Vision Transformer](https://arxiv.org/abs/2203.16414) (SiT) model is used for the task of birth age prediction as an example. Code is based on this [Github](https://github.com/metrics-lab/surface-vision-transformers).

More information about algorithm container and submission can be found [here](https://grand-challenge.org/blogs/create-an-algorithm/). 

## Content:
1. [Prerequisites](#prerequisites)
2. [Overview of the project structure](#overview)
3. [Requirements for Grand Challenge submission (input/output)](#requirements)
4. [Build, test and export your algorithm container](#container)
5. [Tips and general advice](#advice)
6. [Grand Challenge Submissions](#submission)

    6.1. [Create your Algorithm page on Grand Challenge](#algo)

    6.2. [Upload your Algorithm container on Grand Challenge](#container)

    6.3. [Try-out your algorithm container](#try)

    6.4 [Submitting your solution of the challenge website](#submit)

7. [Contacts](#contact)
8. [Acknowledgements](#acknowledgments)


## 1. Prerequisites <a name="prerequisites"></a>

Submissions on grand-challenge require the use of Docker containers and the evalutils library (provided by Grand-Challenge).

First, you will need to install localy [Docker](https://www.docker.com/get-started).

Then, you will need to install evalutils, that you can pip install: 

```
pip install evalutils
```

Optional: To have GPU support for local testing, you want to install the [NVIDIA container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html).

## 2. Overview of the project structure <a name="overview"></a>


The structure of this repository follows the structure of the **Algorithm Container** for Classification in [evalutils](https://comic.github.io/evalutils/d). 

You can either start a project from scratch by following guidelines in [evalutils documentation](https://comic.github.io/evalutils/usage.html#algorithm-container) or by cloning this repository and make the appropriate modifications: 

```
git clone https://github.com/metrics-lab/SLCN_challenge
```

Remark: As evalutils does not implement a class for Regression problems, we only adapted the Classification class to the case of regression problems. 

No matter what methods you used to start your project (evalutils or cloning this repo), you should have at least the following files in your project repository: 

```
.
└── your_project
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
### Dockerfile

The Dockerfile first pull an image from the docker hub. If you need a different base image to build your container (e.g., Tensorflow instead of Pytorch, or a different version), you can adapt the Dockerfile to your particular case. If you need additional libraries, you can add them in the *requirements.txt* file accordingly. Make sure that all source files, such as model and weights, are copied to the docker container (see illustration bellow from [MIDOG Challenge](https://github.com/DeepPathology/MIDOG_reference_docker/)). We provide an example of Dockerfile that you can adapt to your case. 

![dockerfile_img](https://user-images.githubusercontent.com/43467166/128198999-37dd613d-aeef-41a6-9875-9fdf29db4717.png)

### Process.py

The *process.py* file is the main file that needs to be adapted. This file will load your model and your trained weights, read one by one the input images, pre-process the data (if needed), make the prediction for the birth age prediction task, post-process the prediction (if needed), and return the final regression score as a **float** value. More details about input and output in [Section 3](#requirements).

## 3. Requirements for Grand Challenge submissions (input/output) <a name="requirements"></a>

You Docker container (via process.py) reads **.mha** image files as inputs. The metrics file **.shape.gii** provided in the challenge will have to be converted into **.mha** files. A python script is provided as an example.

The output birth-age.json files should simply contain each a single float output, such as:

```
38.99058151245117
```
(see *./test/expected_output.json* for an example)

**Important:** On the server, images will be processed successively and predictions will be made one by one, i.e. there will be one birth-age.json output file per predicition. 

## 4. Build, test and export your Algorithm Container <a name="container"></a>

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

## 5. Tips and general advice <a name="advice"></a>

To remove all unused docker images you can use
```
docker image prune -y 
```

## 6. Grand Challenge Submissions <a name="container"></a>

Submission for the challenge have to uploaded on [SLCN Challenge Website](https://slcn.grand-challenge.org/).

The submissions on grand-challenge work throught the use of Docker containers. As a participant, you will have to create and upload an *Algorithm Container*, created previously, in order to submit a solution. 

### 6.1 Create your Algorithm page on Grand Challenge <a name="algo"></a>

Fill the required information. You can keep your algorithm private. 

![create_algo](https://raw.githubusercontent.com/metrics-lab/SLCN_challenge/main/.github/images/challenge1.png)


Please set the viewer option to Viewer CIRRUS Core (Public); the inputs to *Cortical surface mesh (Image)* and the outputs to *Birth Age (Float)*


![info_algo](https://raw.githubusercontent.com/metrics-lab/SLCN_challenge/main/.github/images/challenge2.png)

### 6.2 Upload your Algorithm container on Grand Challenge <a name="container"></a>

Once your algorithm page is created, you will be able to either upload your algorithm container (the .tar output file of the *bash export.sh* command) or link it to a github repository containing your project. 

![info_algo](https://raw.githubusercontent.com/metrics-lab/SLCN_challenge/main/.github/images/challenge3.png)


### 6.3 Try-out your algorithm container <a name="try"></a>

Even if your container is working perfectly localy, it might failed when uploaded onto the grand-challenge servers. Therefore, we highly advice you to **try-out** your algorithm container, by uploading one image example (a .mha file such as the one provided in ./test/).

![info_algo](https://raw.githubusercontent.com/metrics-lab/SLCN_challenge/main/.github/images/challenge4.png)


### 6.4 Submitting your solution of the challenge website <a name="submit"></a>

Once your algorithm container is working, you can submit it for any phases on the SLCN challenge website. 

![info_algo](https://raw.githubusercontent.com/metrics-lab/SLCN_challenge/main/.github/images/challenge5.png)


## 7. Contacts <a name="contacts"></a>

Please email slcn.challenge@gmail.com if you have any questions on slcn submissions, or open an issue directly here. 

## 8. Acknowledgements <a name="acknowledgements"></a>

The repository is greatly inspired from [MIDOG_reference_docker](https://github.com/DeepPathology/MIDOG_reference_docker).


The code for Surface Vision Transformer is from [surface-vision-transformers](https://github.com/metrics-lab/surface-vision-transformers).