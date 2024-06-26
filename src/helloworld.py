import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPEN_API_TOKEN"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "what are all the available models for OPENAI? gpt-3.5-turbo is one of them.",
        }
    ],
    model="gpt-4o",
)

print(chat_completion.choices[0].message.content)
