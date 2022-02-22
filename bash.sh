#!/bin/bash
. "$1.venv/bin/activate"
python "$1main.py"

dt=$(date '+%d/%m/%Y %H:%M:%S');
echo "$dt"