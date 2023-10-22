from elevenlabs import generate, play, save
from elevenlabs import set_api_key
import moviepy.editor as mp
import os
import json
set_api_key("YOUR_API_KEY")

# Assuming you are in a different folder and you want to loop through the .json files in the 'generations' folder
with open('../topic.txt', 'r') as file:
    folder_path = '../' + file.read().strip()

for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        with open(os.path.join(folder_path, filename), 'r') as f:
            data = json.load(f)
            name = os.path.splitext(filename)[0]
            mp3_filename = name + '.mp3'
            narration_text = data.get("scene-narration", "")

            # Always generate and save audio from narration text.
            if os.path.exists(mp3_filename):
              print(f"Audio file {mp3_filename} exists, skipping.")
            else:
              audio = generate(
                  text=narration_text,
                  voice="Charlie",
                  model="eleven_multilingual_v1"
              )
              save(audio, mp3_filename)

            mp4_filepath = folder_path + '/' + name + '.mp4'

            # Only attempt to combine audio and video if the MP4 exists.
            if os.path.exists(mp4_filepath):
                videoclip = mp.VideoFileClip(mp4_filepath)
                audioclip = mp.AudioFileClip(mp3_filename)

                new_audioclip = mp.CompositeAudioClip([audioclip])
                videoclip.audio = new_audioclip
                videoclip.write_videofile(mp4_filepath)
            else:
                print(f"Video file {mp4_filepath} does not exist, skipping.")


