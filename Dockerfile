## Pull from existing image
# FROM nvcr.io/nvidia/pytorch:21.05-py3
FROM continuumio/miniconda

## Copy requirements
COPY ./src/requirements.txt .

## Install Python packages in Docker image
RUN pip3 install -r requirements.txt

## Copy all files
COPY ./ ./

## Execute the inference command 
CMD ["./src/run_inference.py"]
ENTRYPOINT ["python3"]
