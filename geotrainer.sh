#!/bin/bash


if [[ $1 == "-ir" ]]
then
    pip install -r requirements.txt
    python3 main.py
    exit 0
fi

if [[ $1 == "-ur" ]]
then
    pip uninstall -r requirements.txt
    exit 1
fi


python3 main.py
