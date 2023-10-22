import openai
import os
import uuid
import json
from utils import get_oai_completion


topic = "pythagorean theorem"

def is_valid_json(s):
    try:
        json.loads(s)
        return True
    except json.JSONDecodeError:
        return False

if __name__ == "__main__":
    idea_prompt = """
    Generate script for an educational video on %s in the style of 3blue 1brown. Format your output as a JSON file as per the example below.
    The script should consist of 5 acts:
    Act 1: Introduction (3 scenes)
    Act 2: Transition (3 scenes)
    Act 3: Main proof/result (3 scenes)
    Act 4: Explanation (3 scenes)
    Act 5: Conclusion (3 scenes)
    and return output in following format:
    [
        {
        "scene-filename":act number and scene number
        "scene-title":
        "scene-visual":
        "scene-narration":
        }
    ]
    """ % topic

    messages = [
            {"role": "system", "content": idea_prompt},
    ]

    acts = get_oai_completion(messages)
    # Convert the string into a list of dictionaries
    data_list = json.loads(acts)

    # Directory to save the files in
    directory = topic.replace(" ", "_")

    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

# Save each dictionary into a separate .json file
for entry in data_list:
    filename = os.path.join(directory, entry["scene-filename"] + ".json")
    with open(filename, "w") as file:
        json.dump(entry, file, indent=4)

