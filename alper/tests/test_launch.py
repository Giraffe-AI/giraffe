import subprocess

try:
    result = subprocess.run(["python", 
                             "/Users/alpercanberk/Projects/code-as-environment/alper/generations/2023-07-25-21:18:25/code_t2.py"], 
                            check=True, text=True, capture_output=True)
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e.stderr}")
