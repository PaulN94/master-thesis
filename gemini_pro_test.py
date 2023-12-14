import google.generativeai as genai

genai.configure(api_key="AIzaSyCdJuWgFnisZvoZWbegXfFa9T8LWKiw9Fw")
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content(
    'Tell me a story about a magic backpack.',
    generation_config=genai.types.GenerationConfig(
        temperature=0)
)

print(response.text)