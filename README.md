# face-detection

Face Detection Project

## Environment setup

MacOS Apple Silicon Setup steps for detection deeplearning

- Download Mambaforge-${version}-MacOSX-arm64.sh from https://github.com/conda-forge/miniforge/releases
- Install using /bin/bash Mambaforge-23.3.1-0-MacOSX-arm64.sh
- conda create --name detection-deeplearning python=3.8
- conda activate mlp
- conda install -c apple tensorflow-deps
- pip install tensorflow-macos
- pip install tensorflow-metal
- Now install other dependencies using `pip install requirements.txt`

## Contains

- A face detection code using opencv and using cascade classifier pre trained model
- A face detection code using
