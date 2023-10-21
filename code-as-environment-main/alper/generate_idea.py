import openai
import pathlib
import json
import urllib.request
from utils import get_oai_completion
import os
#from bing_image_downloader import downloader
import shutil


openai.api_key = "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"
if __name__ == "__main__":

    idea_prompt = pathlib.Path("prompts/game_idea/game_idea_prompt.txt").read_text()
    jsonify_prompt = pathlib.Path("prompts/game_idea/game_idea_jsonify_prompt.txt").read_text()

    messages = [
            {"role": "system", "content": idea_prompt},
    ]

    game_idea = get_oai_completion(messages, model="gpt-4")
    # game_idea = pathlib.Path('/Users/alpercanberk/Projects/code-as-environment/alper/game_directories/dishwasher_dash/game_idea.txt').read_text()

    messages.append({"role": "assistant", "content": game_idea})
    messages.append({"role": "system", "content": jsonify_prompt})

    #get a jsonified version of the game idea
    jsonify = get_oai_completion(messages, model="gpt-4")
    # jsonify = pathlib.Path('/Users/alpercanberk/Projects/code-as-environment/alper/game_directories/dish_washer_dash/game.json').read_text()

    json_dict = json.loads(jsonify)
    name = json_dict["name"]
    # no need for image assets rn
    #image_assets = json_dict["image_assets"]

    #create a directory in game_directories 
    game_dir = pathlib.Path(f"game_directories/{name}")
    game_dir.mkdir(exist_ok=True)

    pathlib.Path(f"game_directories/{name}/game_idea.txt").write_text(game_idea)
    pathlib.Path(f"game_directories/{name}/game.json").write_text(jsonify)

    #create a directory for image assets
    image_dir = game_dir / "image_assets"
    image_dir.mkdir(exist_ok=True)

    #save image as [name].png into image_dir
    # for key, search_query in image_assets.items():
    #     downloader.download(search_query,
    #                         limit=1,
    #                         output_dir=image_dir,
    #                         adult_filter_off=True,
    #                         force_replace=False,
    #                         timeout=60,

        # # Bing downloads the images to their own directories, this code moves them to the image_dir
        # temp_dir = os.path.join(image_dir, search_query)
        # for filename in os.listdir(temp_dir):
        #     if filename.endswith(".png"):  
        #         old_file_path = os.path.join(temp_dir, filename)
        #         new_file_path = os.path.join(image_dir, key + '.png') 
        #         shutil.move(old_file_path, new_file_path) 

        # # Remove the temporary directory
        # shutil.rmtree(temp_dir)
