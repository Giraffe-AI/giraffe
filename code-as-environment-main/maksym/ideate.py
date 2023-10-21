import openai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an extremely creative genius game designer. You come up with extremely cool ideas for simple yet fun 2D games"},
        {"role": "user", "content": "Please give me game idea for a simple 2D atari games that would use arrow keys as controls"},
    ]
)
print(response['choices'][0]['message']['content'])