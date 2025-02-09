import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set voice speed
engine.setProperty("rate", 155)  

def speak(text):
    """Make JARVIS speak."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice input."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Couldn't understand you.")
            return None
        except sr.RequestError:
            print("Speech service unavailable.")
            return None

# Main loop
while True:
    command = listen()
    if command:
        if "hello" in command:
            speak("Hey! How can I help?")
        elif "your name" in command:
            speak("I am Jarvis,  your offline AI assistant.")
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I didn't understand that.")

