import os
import json
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def reformulate_question(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Please reformulate the description without changing the meaning. Don't reformulate the word index"},
            {"role": "user", "content": question},
        ],
        temperature= 0.7
    )
    return response['choices'][0]['message']['content']

# Load the input JSON file
with open("JSON2_solved_variations_knapsack_transform.json", 'r') as infile:
    data = json.load(infile)

# Initialize the output data structure
output_data = {"variations": []}

# Loop through each variation
for variation in data["variations"]:
    # Generate 3 reformulated questions
    for i in range(1, 4):
        # Print the console log message
        print(f"Reformulating question {variation['id']}.{i}")
        new_variation = variation.copy()
        new_id = f"{variation['id']}.{i}"
        new_variation["id"] = new_id
        new_question = reformulate_question(variation['question_variation'])
        new_variation["question_reformulation"] = new_question
        output_data["variations"].append(new_variation)

# Save to a new JSON file
with open("JSON3_reformulation_knapsack_transform.json", 'w') as outfile:
    json.dump(output_data, outfile, indent=4)
