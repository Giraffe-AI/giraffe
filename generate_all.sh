#!/bin/bash

# Directory containing the JSON files
directory="pythagorean_theorem"

# Extract the name of the last directory to use as the topic
topic=$(basename "$directory")

# Iterate over each JSON file in the directory
for file in "$directory"/*.json; do
    # Extract the filename (without the directory path)
    filename=$(basename "$file")
    # Invoke generate_scene.py with the appropriate arguments
    python3 generate_scene.py --topic "$topic" --file "$filename"
done
