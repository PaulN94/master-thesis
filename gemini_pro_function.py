from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables from .env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

def gemini_pro(prompt):
    # Create a model
    model = genai.GenerativeModel('gemini-pro')

    # Generate content
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=0)
    )

    return response.text

# Example usage with a custom prompt
user_messages = "Tell me a story about a space adventure."
answer = gemini_pro(user_messages)
print(answer)
