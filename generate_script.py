import openai
import os
import uuid
import json
from utils import get_oai_completion

openai.api_key = "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"

import json

def string_to_json_files(s):
    # Split the string by the repeated pattern '}{'
    dicts = s.split("}{")
    # Add missing curly brackets to the split strings
    for i in range(len(dicts)):
        if not dicts[i].startswith("{"):
            dicts[i] = "{" + dicts[i]
        if not dicts[i].endswith("}"):
            dicts[i] = dicts[i] + "}"
    # Convert each dictionary string to a JSON file
    for i, d in enumerate(dicts):
        with open(f'dict_{i+1}.json', 'w') as f:
            json_obj = json.loads(d)  # Convert string to a Python dictionary
            json.dump(json_obj, f, indent=4)  # Write the dictionary as a JSON to a file
# Test
s = """{...}"""  # Your provided string here
string_to_json_files(s)

topic = "word embeddings"

if __name__ == "__main__":
    idea_prompt = """
    Generate script for an educational video on word embeddings in the style of 3 blue 1 brown.
    ...
    \{title:"Act1", act-description:[act1 description], num-of-scenes:[num-of scenes], scenes:[title:[scene1title], scene-visual:[scene-visual], scene-narration:[scene-narration]}
    """
    messages = [
            {"role": "system", "content": idea_prompt},
    ]
    # For streaming
    acts = get_oai_completion(messages, model="gpt-4")
    print(acts)
