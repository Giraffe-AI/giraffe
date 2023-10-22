import openai
import ast

openai.api_key = "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"

def get_oai_completion(messages, temperature=0.2, model="gpt-4"):

    #streaming by default
    response = openai.ChatCompletion.create(
        model = model,
        messages=messages,
        stream=True,
        temperature=0
    )

    collected_events = []
    completion_text = ''
    old_length = 0
    # iterate through the stream of events
    for event in response:

        collected_events.append(event)
        delta = event['choices'][0]['delta']

        if 'content' in delta:
            completion_text += delta["content"]
            # only print the new content
            print(completion_text[old_length:], end='', flush=True) 
            old_length = len(completion_text)

    return completion_text

def check_code_safety(code : str):
    #ensure that no libraries are imported other than pygame, random, and math

    # List of allowed modules
    allowed_modules = ["manim,", "numpy", "math", "random"]

    # Parse the code into an Abstract Syntax Tree
    tree = ast.parse(code)

    # Walk the AST
    for node in ast.walk(tree):
        # Check for import statements
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name not in allowed_modules:
                    return False  # Disallowed import detected
        # Check for import from statements
        if isinstance(node, ast.ImportFrom):
            if node.module not in allowed_modules:
                return False  # Disallowed import detected

    return True  # All imports are allowed