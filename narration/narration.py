from elevenlabs import generate, play, save
from elevenlabs import set_api_key
import moviepy.editor as mp
set_api_key("fa2665e81b00d1a5ab4f6b30d6097ee6")

audio = generate(
  text="Welcome to another episode of 3blue1brown. Today, we're going to explore the Pythagorean theorem, a fundamental principle in geometry that you've probably heard of. It's about right-angled triangles, like the one you see here.",
  voice="Charlie",
  model="eleven_multilingual_v1"
)

file = save(audio,'test.mp3')
videoclip = mp.VideoFileClip("PythagoreanTheorem.mp4")
audioclip = mp.AudioFileClip("test.mp3")

new_audioclip = mp.CompositeAudioClip([audioclip])
videoclip.audio = new_audioclip
videoclip.write_videofile("narration.mp4")
play(audio)