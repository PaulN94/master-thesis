import os
import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Count to ten"},
    ]
)

response['choices'][0]['message']['content']

print(response)
