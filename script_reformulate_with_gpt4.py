import os
import json
import openai

# Set OpenAI API key
openai.api_key = "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"

def reformulate_question(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Please reformulate the question without changing the meaning."},
            {"role": "user", "content": question},
        ]
    )
    return response['choices'][0]['message']['content']

# Load the input JSON file
with open("JSON2_q_and_a_variations_knapsack_transformation.json", 'r') as infile:
    data = json.load(infile)

# Initialize the output data structure
output_data = {"variations": []}

# Loop through each variation
for variation in data["variations"]:
    # Generate 3 reformulated questions
    for i in range(1, 4):
        new_variation = variation.copy()
        new_id = f"{variation['id']}.{i}"
        new_variation["id"] = new_id
        new_question = reformulate_question(variation['question_variation'])
        new_variation["question_reformulation"] = new_question
        output_data["variations"].append(new_variation)

# Save to a new JSON file
with open("JSON3_q_and_a_reformulation_knapsack_transformation.json", 'w') as outfile:
    json.dump(output_data, outfile, indent=4)
