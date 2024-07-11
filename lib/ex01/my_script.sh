#!/bin/bash

PYTHON="/usr/bin/python3"
DIR="local_lib"
PATH_URL="https://github.com/jaraco/path.git"
LOGS="install.log"
SMALL_PROGRAM="my_program.py"

echo "************ Installing $PATH_URL ************"

$PYTHON -m venv $DIR
source $DIR/bin/activate

python -m pip --version

python -m pip install --upgrade pip

python -m pip install --log $LOGS --force-reinstall git+$PATH_URL

echo ""
echo "************ Program output ************"
python $SMALL_PROGRAM
