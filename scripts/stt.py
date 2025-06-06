"""
Script Name: stt.py
Purpose: Implements continuous speech-to-text conversion using Google's speech recognition service.
Author: Deepak Terse
Date: 2024-05-23

Usage:
    python scripts/stt.py

Description:
    This script provides real-time speech-to-text conversion capabilities, continuously listening
    for user voice input and transcribing it to text. It utilizes Google's speech recognition
    service for accurate transcription and includes ambient noise adjustment for better accuracy.
    
    The script runs in a continuous loop until the user says "bye", making it suitable for
    interactive voice applications or as a component in larger voice-controlled systems.
    
    Features:
    - Real-time voice input processing
    - Automatic ambient noise adjustment
    - Continuous listening mode
    - Clear visual feedback with emoji indicators
    - Graceful error handling for various scenarios

Dependencies:
    - SpeechRecognition
    - PyAudio (for microphone access)
    - Google Speech Recognition API (internet connection required)

References:
    - [SpeechRecognition Documentation](https://github.com/Uberi/speech_recognition)
    - [Google Speech Recognition API](https://cloud.google.com/speech-to-text)
"""

import speech_recognition as sr
import time

def listen_and_transcribe():
    """
    Continuously listens for user voice input and transcribes it to text.
    Stops when the user says 'bye'.
    """
    recognizer = sr.Recognizer()
    
    print("🎤 Starting voice recognition...")
    print("Speak now! Say 'bye' to exit.")
    
    while True:
        try:
            with sr.Microphone() as source:
                print("\n🎤 Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                audio = recognizer.listen(source)
                
                text = recognizer.recognize_google(audio)
                print(f"🗣️  You said: {text}")
                
                if text.lower() == "bye":
                    print("👋 Goodbye!")
                    break
                    
        except sr.UnknownValueError:
            print("❓ Could not understand audio")
        except sr.RequestError as e:
            print(f"❌ Could not request results; {e}")
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            time.sleep(1)  # Brief pause before retrying

if __name__ == "__main__":
    listen_and_transcribe() 