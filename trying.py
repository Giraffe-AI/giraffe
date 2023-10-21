import openai
import os

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an extremely creative genius game designer. You come up with extremely cool ideas for simple yet fun 2D games"},
        {"role": "user", "content": "Please give me game idea for a simple 2D atari games that would use arrow keys as controls"},
    ]
)
print(response['choices'][0]['message']['content'])