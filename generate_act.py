import openai
import pathlib
import json
import urllib.request
from utils import get_oai_completion
import os
import shutil

openai.api_key = "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"


if __name__ == "__main__":

    #idea_prompt = pathlib.Path("prompts/game_idea/game_idea_prompt.txt").read_text()
    idea_prompt = """

    """
    messages = [
            {"role": "system", "content": idea_prompt},
    ]
    #for streaming
    game_idea = get_oai_completion(messages, model="gpt-4")
    scenes = game_idea.split("[End of scene]")
    print(len(scenes))