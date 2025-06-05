"""
Script Name: tts.py
Purpose: Synthesizes text to speech and plays it back.
Author: Deepak Terse
Date: 2024-05-23

Usage:
    python scripts/tts.py

Description:
    This script is a proof of concept for an AI voice assistant project, designed to produce human-like voice synthesis.
    It utilizes the TTS library with a pre-trained VCTK model to convert a fixed text string into speech.
    The synthesized speech is saved to a temporary WAV file, played back using sounddevice and scipy.io.wavfile,
    and the temporary file is subsequently removed.

Dependencies:
    - TTS
    - sounddevice
    - scipy
    - portaudio (external dependency, install using brew)

References:
    - [VCTK dataset](https://datashare.ed.ac.uk/handle/10283/3443)
"""
from TTS.api import TTS
import sounddevice as sd
import scipy.io.wavfile
import tempfile
import os

# Using a pre-trained model (offline, realistic voice)
tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False, gpu=False)

text = "Hello, I am your virtual assistant. How can I help you today?"

with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as fp:
    tts.tts_to_file(text=text, file_path=fp.name, speaker="p230")

    sr, data = scipy.io.wavfile.read(fp.name)
    sd.play(data, samplerate=sr)
    sd.wait()

    os.remove(fp.name)
