import openai

response = openai.ChatCompletion.create(
  model="gpt-4",
  max_tokens=7900,
  messages=[
        {"role": "system", "content": "You are 3Blue1Brown AI. You are a brilliant educator and creator. You generate the best visual ways to explain concepts, and you are proficient in using manim."},
        {"role": "user", "content": """
            Code me up a simple top-down game using PyGame where you're a garbage truck and your goal is to collect trash
            1. Make sure it's physically realistic. 
            2. Make sure that it has a goal.
            3. Make the colors realistic, and add some randomization.
            4. Make it composable, as you will be writing some unit tests for it later so you may have to create simplified environments. 
            5. Make sure that episodes terminate. 
            6. If possible, add interesting dynamics.
            7. Be concise
            8. Put a time limit on the episode.
            9. Make sure the player can't disappear.
            10. Think of interesting game dynamics and add them. 
         """
         },
    ]
)

print(response.choices[0].message.content)