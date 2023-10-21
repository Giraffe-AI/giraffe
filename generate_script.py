import openai
import os
import uuid
import json
from utils import get_oai_completion

openai.api_key = "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"

topic = "pythagorean theorem"

if __name__ == "__main__":
    idea_prompt = """
    Generate script for an educational video on %s in the style of 3 blue 1 brown.
    Give any equations in latex.
    ...
    \{title:"Act1", act-description:[act1 description], num-of-scenes:[num-of scenes], scenes:[title:[scene1title], scene-visual:[scene-visual], scene-narration:[scene-narration]}
    """ % topic
    messages = [
            {"role": "system", "content": idea_prompt},
    ]
    # For streaming
    acts = get_oai_completion(messages, model="gpt-4")
    print(acts)
