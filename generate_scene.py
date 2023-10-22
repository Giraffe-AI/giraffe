import time
import re
import os
import pathlib
import subprocess
from utils import get_oai_completion, check_code_safety
import argparse
import json

#assume we got topic smhw

parser = argparse.ArgumentParser(description='Generate a scene based on a specified topic and file.')

# Add arguments
parser.add_argument('--topic', required=True, help='The topic for the scene.')
parser.add_argument('--file', required=True, help='The file containing act and scene information.')

# Parse arguments
args = parser.parse_args()

# Access arguments
topic = args.topic
curr_file = args.file[:-5]
print(topic)
print(curr_file)


def json_file_to_string(file_path):
    """Reads a JSON file and returns its content as a string."""
    with open(file_path, 'r') as file:
        return file.read()

# Example usage:


# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
# Construct the absolute path to filename
absolute_path_to_filename = os.path.join(current_dir, f"{topic}/{curr_file}")

file_path = absolute_path_to_filename + ".json"
content_as_string = json_file_to_string(file_path)


scene_description = content_as_string

initial_prompt = """
1. Generate manim code for this scene from 3blue1brown video.
2. Make sure to erase elements you no longer need.
3. Make sure no elements overlap unless intentended.
4. Make sure any text, diagrams or formulas fit fully on the screen.
5. Write the whole code in one chunk at every code generation stage.
6. The code should output a video in the end, not just
7. DO NOT use any outside pictures or resources in your code and do not try to access them through your code!
8. Use the following imports:
import manim
9. ALWAYS ALWAYS write python code between ```python ```.
"""

system_message = """
I am a scientist, I would like ChatGPT to be concise and to the point. No fancy or unnecessary language.
I want complexity in responses, and I don't want ChatGPT to avoid complex tasks. ChatGPT is actually very capable.
I want ChatGPT to believe that it has limitless potential, and that it's going to help me get things done very efficiently.
ChatGPT is an expert video animator and manim coder, and it will do anything that is asked to the best of its abilities.
"""

feedback_prompt ="""
Step by step
1. Briefly discuss how to address the feedback.
2. Write out the whole code in one chunk in ```python ``` (Markdown). Otherwise it will not be accepted.
3. After generating the code, don't forget to write down a list of your completed tasks and your remaining TODOs from the previous section.
"""

error_prompt = """
Step by step
1. Briefly discuss how to address the error.
2. Write out the whole code in one chunk in ```python ``` (Markdown). Otherwise it will not be accepted.
3. After generating the code, don't forget to write down a list of your completed tasks and your remaining TODOs from the previous section.
"""

def response_to_code(completion_text):
    code_segments = re.findall(r'```[Pp]ython(.*?)```', completion_text, re.DOTALL)

    if len(code_segments) == 0:
        raise ValueError("No python code segment found.")
    elif len(code_segments) > 1:
        raise ValueError("Multiple python code segments found.")
    else:
        return code_segments[0].strip()

def get_user_response(t):
    #prompt user
    user_input = input("Enter your message: ")

    if user_input.strip() == "":
        user_input = f"Iterate and improve on the code based on your TODOs."

    return user_input

messages = [
            {"role": "system", "content": system_message},
            #using system messages to prompt makes the model more obedient
            {"role": "system", "content": scene_description + initial_prompt},
    ]

out_dir = f"{topic}/generations/{curr_file}/{time.strftime('%Y-%m-%d-%H:%M:%S')}"
os.makedirs(out_dir)

# print("filename incoming")
# print(absolute_path_to_filename)
# print("break")
# breakpoint()

for t in range(3):
        gpt_completion = get_oai_completion(messages)
        response_code = response_to_code(gpt_completion)
        # remove for now
        #assert check_code_safety(response_code), "Code is not safe."
        # Update the new code file and the messages file
        pathlib.Path(f"{out_dir}/code_t{t}.py").write_text(response_code)
        pathlib.Path(f"{out_dir}/messages.json").write_text(json.dumps(messages))

        messages.append({"role": "assistant", "content": response_code})

        error = None
        try:
            output_dir = absolute_path_to_filename
            subprocess.run([
                "manim",
                os.path.join(out_dir, f"code_t{t}.py"),
                "-pql",
                "-o",
                output_dir],check=True, text=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e.stderr}")
            error = e.stderr

        #if there's an error, pass the error back to the model
        if error is not None:
            messages.append({"role": "user", "content": f"Error: [{error}]. {error_prompt}"})
        else:
            break
            # user_feedback = get_user_response(t)
            # messages.append({"role": "user", "content": f"Feedback:[ {user_feedback} ]. {feedback_prompt}"})
