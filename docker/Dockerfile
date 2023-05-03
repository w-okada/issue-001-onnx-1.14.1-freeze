
FROM debian:stable-slim
# FROM nvidia/cuda:12.0.1-cudnn8-runtime-ubuntu22.04

RUN apt-get update \
        && apt-get install -y python3-pip python-is-python3 emacs git build-essential wget gdb

RUN wget https://github.com/Kitware/CMake/releases/download/v3.26.3/cmake-3.26.3-linux-x86_64.sh
RUN chmod +x cmake-3.26.3-linux-x86_64.sh
RUN ./cmake-3.26.3-linux-x86_64.sh --skip-license --prefix=/usr/local

# RUN git clone -b v1.14.1 --depth 1 https://github.com/microsoft/onnxruntime.git
RUN git clone --depth 1 https://github.com/microsoft/onnxruntime.git
WORKDIR /onnxruntime/tools/ci_build
RUN pip install -r requirements.txt
RUN python build.py --build_wheel --build_dir=build --config=Debug --parallel=$(nproc) --skip_tests --allow_running_as_root
RUN pip install build/Debug/dist/onnxruntime-*-cp39-cp39-linux_x86_64.whl

WORKDIR /
ADD metadata.onnx /
ADD test_metadata.py /
