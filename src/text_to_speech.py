#!/usr/bin/env python

from base64 import decode, decodebytes
from os import environ, makedirs
from pathlib import Path
from sys import argv
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=environ.get("OPEN_API_TOKEN"),
)

makedirs("speech", exist_ok=True)

speech_file_path = "speech/speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Ich geh mal schnell zur Bäckerei",
  speed=0.9
)

response.stream_to_file(speech_file_path)

