import moviepy.editor as mp
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

with open('topic.txt', 'r') as file:
    folder_path = './' + file.read().strip() + '/'

# List to hold all the VideoFileClip objects
clips = []

# Get a sorted list of all .mp4 filenames in the directory
mp4_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".mp4")])

for filename in mp4_files:
    mp4_filepath = os.path.join(folder_path, filename)

    # Load the video clip and append it to the clips list
    clips.append(VideoFileClip(mp4_filepath))

# Concatenate all the video clips
if clips:
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("final.mp4")
else:
    print("No .mp4 files found in the specified folder.")
