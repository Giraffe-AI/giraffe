import openai
import os
import uuid
from utils import get_oai_completion

openai.api_key = "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"

def save_script_and_scenes(idea_prompt, scenes):
    # Generate a unique id for this completion
    unique_id = str(uuid.uuid4())
    # Create a directory with the unique id
    os.makedirs(unique_id, exist_ok=True)
    # Save the initial prompt to init_prompt.txt
    with open(f"{unique_id}/init_prompt.txt", "w") as file:
        file.write(idea_prompt)
    # Create a directory for scenes
    os.makedirs(f"{unique_id}/scenes", exist_ok=True)
    # Save each scene to a separate file
    for i, scene in enumerate(scenes):
        # Get the title for each scene (first 4 words or less)
        title = "_".join(scene.split()[:4])
        with open(f"{unique_id}/scenes/{title}.txt", "w") as file:
            file.write(scene)

if __name__ == "__main__":
    idea_prompt = """
    give me a script for a 3b1b video
    explaining spectral theorem in an intuitive way.
    The script should include at least 10 scenes.
    return scenes in json format
    """
    messages = [
            {"role": "system", "content": idea_prompt},
    ]
    # For streaming
    game_idea = get_oai_completion(messages, model="gpt-4")
    scenes = game_idea.split("[end of scene]")
    print(len(scenes))  # Print the number of scenes generated
    save_script_and_scenes(idea_prompt, scenes)
