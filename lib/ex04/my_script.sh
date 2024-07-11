#!/bin/bash

PYTHON="/usr/bin/python3"
DIR="django_venv"

$PYTHON -m venv $DIR
source $DIR/bin/activate

echo "************ Installing requirements... ************"

python -m pip install --upgrade pip

python -m pip install -r requirement.txt
