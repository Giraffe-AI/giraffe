#!/bin/bash

# Run the Python script
python3 generate_script.py

# Run the Bash executable
./generate_all.sh

# Run the narration script
cd narration
python3 narration.py

# Link it all together 
python3 linker.py