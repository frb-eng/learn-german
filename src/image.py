#!/usr/bin/env python

from base64 import decode, decodebytes
from os import environ, makedirs
from sys import argv
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=environ.get("OPEN_API_TOKEN"),
)
response = client.images.generate(
  model="dall-e-3",
  prompt="Ich geh mal schnell zur Bäckerei",
  size="1024x1024",
  quality="standard",
  style="natural",
  n=1,
  response_format="b64_json"
)

makedirs("images", exist_ok=True)

with open("images/image.png", "wb") as file:
    if response.data[0].b64_json:
        file.write(decodebytes(bytes(response.data[0].b64_json, 'utf-8')))

