
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04
# FROM nvidia/cuda:12.0.1-cudnn8-runtime-ubuntu22.04

RUN apt-get update \
        && apt-get install -y python3-pip emacs git \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

ADD metadata.onnx /
ADD test_metadata.py /


