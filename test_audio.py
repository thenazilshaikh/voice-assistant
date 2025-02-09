import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Sorry, I couldn't understand that.")
except sr.RequestError:
    print("Error with the speech recognition service.")


