import openai
import os
import uuid
import json
from utils import get_oai_completion
openai.api_key = "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"


scene_description = """
Scene 3: A Simple Example of Word Embeddings

Visual:

A 3D space appears, like a 3D graph.
Four labeled dots emerge:
"king" and "queen" are closely placed vertically.
"man" and "woman" are closely placed vertically.
The horizontal positioning illustrates the relationship between "king-man" and "queen-woman".
Arrows:
An arrow from "man" to "king" appears, labeled "royalty".
A similar arrow, in length and direction, from "woman" to "queen".
As narration progresses, the similarities in arrow direction and length are emphasized with a glowing effect.
Narration:

"Let's delve into an example to understand this better."
"In our 3D space, words are represented as points."
"Notice how the relationship 'man' to 'king' is analogous to 'woman' to 'queen'."
"The relationships, or the semantic meanings, are captured as vectors or arrows in this space."
"""

if __name__ == "__main__":
    idea_prompt = f"""
    Generate manim code for this scene from 3b1b video {scene_description}
    """
    messages = [
            {"role": "system", "content": system_message},
            #using system messages to prompt makes the model more obedient
            {"role": "system", "content": game_description + initial_prompt},
    ]
    # For streaming
    code = get_oai_completion(messages, model="gpt-4")
