# Offline voice-assistant(Under Development)
# Overview:

The Offline Voice Assistant is a fully self-hosted, AI-powered voice assistant designed to operate without an internet connection. It utilizes Vosk for speech recognition and executes system commands, making interactions smooth and efficient. This assistant is built to perform various system tasks, answer queries, and provide a seamless hands-free experience.

# Features

Completely Offline: No reliance on external APIs or internet connectivity.

Customizable Wake Words: Supports multiple wake words to trigger voice commands.

System Command Execution: Can open applications, manage system settings, and perform various actions.

Text-to-Speech (TTS): Uses macOS' built-in say command for spoken responses.

Continuous Listening Mode (In Progress): Plans to improve response flow without requiring repeated wake-word activation.

# Files and Their Purpose

wakeword.py - Listens for predefined wake words and triggers command processing.

voice_assistant.py - Main logic for processing commands and executing actions.

test_audio.py - Helps in testing microphone input and debugging speech recognition.

test_tts.py - Verifies text-to-speech functionality before full integration.

# Installation

Clone the repository:

     git clone <repo-url>
     cd offline-voice-assistant

Install dependencies:

    pip install vosk sounddevice

Run the assistant:

    python3 wakeword.py

# Current Limitations & Future Improvements

Better Command Recognition: Enhancing accuracy to reduce misinterpretations.

Continuous Conversation Mode: Removing the need for wake-word repetition after each command.

GUI Integration (Planned): A visual interface for better usability.

Expanded System Controls: More commands for deeper OS control.

# This project is still under active development, and contributions are welcome!




