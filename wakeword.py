import os
import json
import queue
import vosk
import sounddevice as sd
import sys
import numpy as np
import subprocess


def speak(text):
    subprocess.run(["say", text])  # Works on macOS

# Define the wake words
WAKE_WORDS = ["matter", "uth ja", "chiku", "chintu", "bhai"]

# Load the Vosk model
MODEL_PATH = "~/vosk_models/vosk-model-small-en-us-0.15"
if not os.path.exists(os.path.expanduser(MODEL_PATH)):
    print("Vosk model not found. Make sure the path is correct.")
    sys.exit(1)
model = vosk.Model(os.path.expanduser(MODEL_PATH))

# Create a queue to hold the audio data
audio_queue = queue.Queue()

# Callback function to process audio
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(bytes(indata))

# Function to process recognized commands
def process_command(command):
    command = command.lower()
    print(f"You said: {command}")
    
    if "hello" in command:
        speak("Hey! How can I help?")
    elif "your name" in command:
        speak("I am your offline AI assistant.")
    elif "open chrome" in command:
        speak("Opening Google Chrome.")
        os.system("open -a 'Google Chrome'")  # macOS command
    elif "exit" in command:
        speak("Goodbye!")
        sys.exit(0)
    else:
        speak("I didn't understand that.")

# Text-to-speech function (macOS `say` command for now)
def speak(text):
    os.system(f"say {text}")

# Start listening to audio
def listen():
    recognizer = vosk.KaldiRecognizer(model, 16000)
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1, callback=callback):
        print(f"Listening for wake words {', '.join(WAKE_WORDS)}...")
        
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "").lower()
                
                if any(wake in text for wake in WAKE_WORDS):
                    print("✨ MATTER Activated! ✨")
                    speak("Yes?")
                    listen_for_command()

# Listen for a command after activation
def listen_for_command():
    recognizer = vosk.KaldiRecognizer(model, 16000)
    print("Listening for a command...")
    
    while True:
        data = audio_queue.get()
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            command = result.get("text", "").lower()
            
            if command:
                process_command(command)
                break  # Stop listening after processing a command

if __name__ == "__main__":
    listen()

