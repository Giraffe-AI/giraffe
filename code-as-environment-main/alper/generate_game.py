import time
import re
import os
import pathlib
import subprocess
from utils import get_oai_completion, check_code_safety
import argparse
import json

def get_user_response(t):
    #prompt user
    user_input = input("Enter your message: ")

    if user_input.strip() == "":
        user_input = f"Iterate and improve on the code based on your TODOs."

    return user_input

def response_to_code(completion_text):
    code_segments = re.findall(r'```[Pp]ython(.*?)```', completion_text, re.DOTALL)

    if len(code_segments) == 0:
        raise ValueError("No python code segment found.")
    elif len(code_segments) > 1:
        raise ValueError("Multiple python code segments found.")
    else:
        return code_segments[0].strip()
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--game_name", type=str, help="Name of the game to generate code for")

    args = parser.parse_args()

    game_dir = pathlib.Path(f"game_directories/{args.game_name}")
    if not game_dir.exists():
        raise ValueError(f"Game directory {game_dir} does not exist.")

    #open files using pathlib
    game_description = pathlib.Path(f"game_directories/{args.game_name}/game_idea.txt").read_text()
    initial_prompt = pathlib.Path(f"prompts/game_generation/initial_prompt.txt").read_text()
    system_message = pathlib.Path(f"prompts/game_generation/system_message.txt").read_text()
    feedback_prompt = pathlib.Path(f"prompts/game_generation/feedback_prompt.txt").read_text()
    error_prompt = pathlib.Path(f"prompts/game_generation/error_prompt.txt").read_text()


    messages = [
            {"role": "system", "content": system_message},
            #using system messages to prompt makes the model more obedient
            {"role": "system", "content": game_description + initial_prompt},
    ]

    out_dir = f"generations/{args.game_name}-{time.strftime('%Y-%m-%d-%H:%M:%S')}"
    os.makedirs(out_dir)

    for t in range(10):

        gpt_completion = get_oai_completion(messages)
        response_code = response_to_code(gpt_completion)

        assert check_code_safety(response_code), "Code is not safe."

        # Update the new code file and the messages file
        pathlib.Path(f"{out_dir}/code_t{t}.py").write_text(response_code)
        pathlib.Path(f"{out_dir}/messages.json").write_text(json.dumps(messages))

        messages.append({"role": "assistant", "content": response_code})

        error = None
        try:
            subprocess.run(["python", os.path.join(out_dir, f"code_t{t}.py")], check=True, text=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e.stderr}")
            error = e.stderr

        #if there's an error, pass the error back to the model
        if error is not None:
            messages.append({"role": "user", "content": f"Error: [{error}]. {error_prompt}"})
        else:
            user_feedback = get_user_response(t)
            messages.append({"role": "user", "content": f"Feedback:[ {user_feedback} ]. {feedback_prompt}"})

