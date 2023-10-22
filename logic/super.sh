#!/bin/bash

# post temporary code to the website
curl -X POST -H "Content-Type: application/json" -d '{"code":"200", "video":"temp"}' http://localhost:3001/script-started

cd .. 
cd logic 

# Run the Python script
python3 generate_script.py || { echo 'command failed' ; exit 1; }

# Run the Bash executable
./generate_all.sh

# Run the narration script
cd narration
python3 narration.py
cd ..
# Link it all together
python3 linker.py
rm -f narration/*.mp3
rm -rf media/*

# post the video
curl -X POST -H "Content-Type: application/json" -d '{"code":"200", "video":"final.mp4"}' http://localhost:3001/script-complete