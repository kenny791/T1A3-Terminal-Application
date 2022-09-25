#!/bin/bash

# installs dependencies
if [[ $1 == "-ir" ]]
then
    pip install -r requirements.txt
    exit 0
fi

# unistalls dependencies
if [[ $1 == "-ur" ]]
then
    pip uninstall -r requirements.txt
    exit 1
fi

# opens webbrowser and directs user to README file
if [[ $1 == "-h" ]]
then
    python3 -m webbrowser https://github.com/kenny791/T1A3-Terminal-Application#readme
    exit 2
fi

# launched the application when no arguments are provided
python3 main.py
