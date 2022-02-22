#!/bin/bash
. "$(pwd)/.venv/bin/activate"
python "$(pwd)/main.py"

dt=$(date '+%d/%m/%Y %H:%M:%S');
echo "$dt"