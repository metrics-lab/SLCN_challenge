# SLCN Challenge 2022 - Docker submission example

Credits: S. Dahan, LZJ. Williams

This repository provides a reference algorithm Docker container for SLCN 2022 Challenge submission, on the grand-challenge plateform. 

It should serve as an example or/and a template for your own algorithm container implementaion. 

Here, a [Surface Vision Trasnformer](https://arxiv.org/abs/2203.16414) (SiT) model is used for the task of birth age prediction as an example. Code is based on this [Github](https://github.com/metrics-lab/surface-vision-transformers).

More information about algorithm container and submission can be found [here](https://grand-challenge.org/blogs/create-an-algorithm/). 

## Content:
1. [Prerequisites](#prerequisites)
2. [Requirements for Grand Challenge submission](#requirements)


## 1. Prerequisites <a name="prerequisites"></a>

Submissions are based on Docker containers and the evalutils library (provided by Grand-Challenge).

First, you will need to install localy [Docker](https://www.docker.com/get-started).

Then, you will need to install evalutils, that you can pip install: 

```
pip install evalutils
```


## 2. Requirements for Grand Challenge submissions

You Docker container (via process.py) is supposed to read .mha image files. 

Important: Images will be read successively and predictions will be made one by one, ie there will be one birth-age.json file per predicition. 