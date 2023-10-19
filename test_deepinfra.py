import openai

# Point OpenAI client to our endpoint
openai.api_key = "92RbvpzNcpp28wEGcV2TA4agGatDl0uo"
openai.api_base = "https://api.deepinfra.com/v1/openai"

chat_completion = openai.ChatCompletion.create(
    model="codellama/CodeLlama-34b-Instruct-hf",
    messages=[{"role": "system", "content": "act as a pirate"},
            {"role": "user", "content": "Hello"}
              ],
)

print(chat_completion.choices[0].message.content)