import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import pygame
import numpy as np
import tempfile
import os
from threading import Thread, Event

samplerate = 44100  # Hertz

def transcribe_speech(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)

    try:
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    os.remove(filename)

def record_audio(filename, stop_event):
    print("Please speak:")
    myrecording = sd.rec(int(samplerate * 10), samplerate=samplerate, channels=1)
    while not stop_event.is_set():
        sd.sleep(1000)
    sd.stop()
    sf.write(filename, myrecording, samplerate)

def main():
    pygame.init()

    # make a temporary file for the audio
    temp_dir = tempfile.gettempdir()
    temp_filename = os.path.join(temp_dir, 'temp.wav')

    # make a stop event
    stop_event = Event()

    # start recording audio in a separate thread
    audio_thread = Thread(target=record_audio, args=(temp_filename, stop_event))
    audio_thread.start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                stop_event.set()
                audio_thread.join()
                transcribe_speech(temp_filename)
                return

if __name__ == "__main__":
    main()
