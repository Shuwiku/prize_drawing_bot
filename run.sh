#!/bin/bash
python3 -m venv venv
source ./venv/bin/activate
python3 -m pip install -r ./requirements.txt
clear
python3 ./prize_drawing_bot\
