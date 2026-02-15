#!/usr/bin/env bash

add-apt-repository ppa:deadsnakes/ppa
apt update

apt-get install -y python3.13 python3.13-dev python3.13-venv

python3.13 -m ensurepip --upgrade --default-pip
python3.13 -m pip install setuptools
python3.13 -m pip install -r /autograder/source/requirements.txt
