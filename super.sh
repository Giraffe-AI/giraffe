#!/bin/bash

# post temporary code to the website
curl -X POST -H "Content-Type: application/json" -d '{"code":"200", "video":"temp"}' http://localhost:3001

# Run the Python script
python3 generate_script.py

# Run the Bash executable
./generate_all.sh

# Run the narration script
cd narration
python3 narration.py

# Link it all together 
python3 linker.py

# post the video
curl -X POST -H "Content-Type: application/json" -d '{"code":"200", "video":"final.mp4"}' http://localhost:3001
