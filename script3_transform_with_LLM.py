import os
import openai
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# System message
system_message = "Modify the following Python optimization model according to the users question and return only the modified executable code and nothing else"

# Load the original JSON file
input_json_filename = "JSON3_reformulation_knapsack_transform.json"
with open(input_json_filename, "r") as f:
    data = json.load(f)

# Read the content of knapsack_model.py
with open("knapsack_model.py", "r") as f:
    knapsack_model_content = f.read()

# Iterate over each question and send it to OpenAI API
for i, variation in enumerate(data['variations']):
    question = variation['question_reformulation']
    entry_id = variation['id']  # Extracting the id from the entry

    # Create the conversation
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": question},
            {"role": "user", "content": knapsack_model_content}
        ]
    )

    # Extract the transformed model
    transformed_model = response['choices'][0]['message']['content']

    # Add the transformed model to the question entry in the in-memory JSON object
    data['variations'][i]['knapsack_model_transformed'] = transformed_model

    # Log the request with the id
    print(f"Model {entry_id} reformulated")  # this will print "Model 1.2.1.1.1 reformulated", "Model 1.2.1.1.2 reformulated", etc.

# Save the modified object to a new JSON file
output_json_filename = "JSON4_llm_response_knapsack_transform.json"
with open(output_json_filename, "w") as f:
    json.dump(data, f, indent=4)
