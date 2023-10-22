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
    ...
    {
    "title": "Act 1",
    "act-description": "act1 description",
    "num-of-scenes": "num-of scenes",
    "scenes": [
        {
            "title": "scene1title",
            "scene-visual": "scene-visual",
            "scene-narration": "scene-narration"
        },
        {
            "title": "scene2title",
            "scene-visual": "scene2-visual",
            "scene-narration": "scene2-narration"
        }
    ]
}
    """ % topic

    messages = [
            {"role": "system", "content": idea_prompt},
    ]

    acts = get_oai_completion(messages)

    # Create a folder with UUID
    folder_name = str(uuid.uuid4())
    os.mkdir(folder_name)

    dicts = acts.split("}\n{")
    for i in range(len(dicts)):
        if not dicts[i].startswith("{"):
            dicts[i] = "{" + dicts[i]
        if not dicts[i].endswith("}"):
            dicts[i] = dicts[i] + "}"
    print(len(dicts))
    #for i, d in enumerate(dicts):
    #    with open(os.path.join(folder_path, f'dict_{i+1}.json'), 'w') as f:
    #        json_obj = json.loads(d)
    #        json.dump(json_obj, f, indent=4)

    # Check if the string 'acts' is a valid JSON string
    #if is_valid_json(acts):
    #    string_to_json_files(acts, folder_name)
    #else:
    #    print("Invalid JSON response.")
