#FROM nvcr.io/nvidia/pytorch:21.05-py3
FROM pytorch/pytorch

RUN apt-get update
RUN apt-get install -y gcc

RUN groupadd -r algorithm && useradd -m --no-log-init -r -g algorithm algorithm

RUN mkdir -p /opt/algorithm -p /input /output \
    && chown algorithm:algorithm /opt/algorithm /input /output 
USER algorithm

WORKDIR /opt/algorithm

ENV PATH="/home/algorithm/.local/bin:${PATH}"

RUN python -m pip install --user -U pip

# Copy all required files such that they are available within the docker image (code, weights, ...)
COPY --chown=algorithm:algorithm requirements.txt /opt/algorithm/

COPY --chown=algorithm:algorithm model/ /opt/algorithm/model/
COPY --chown=algorithm:algorithm utils/ /opt/algorithm/utils/
COPY --chown=algorithm:algorithm weights/ /opt/algorithm/checkpoints/
COPY --chown=algorithm:algorithm process.py /opt/algorithm/


# Install required python packages via pip - you may adapt the requirements.txt to your needs
RUN python -m pip install --user -r requirements.txt

# Entrypoint to your python code - executes process.py as a script
ENTRYPOINT python -m process $0 $@
