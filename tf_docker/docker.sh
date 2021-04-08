#!/bin/bash

cd $(dirname $0)
docker run -it --rm -v ${PWD}/notebooks:/tf/notebooks -p 8888:8888 tensorflow/tensorflow:latest-jupyter
