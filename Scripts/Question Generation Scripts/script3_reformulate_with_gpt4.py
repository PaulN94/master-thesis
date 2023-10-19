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
            {"role": "system", "content": "Please reformulate the question without changing the meaning. Don't reformulate the word index"},
            {"role": "user", "content": question},
        ],
        temperature= 0.7
    )
    return response['choices'][0]['message']['content']

# Get the directory of the currently executing script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to experiment_settings.json
settings_path = os.path.join(script_directory, "experiment_settings.json")

# Load the settings from the experiment_settings.json file
with open(settings_path, "r") as settings_file:
    settings = json.load(settings_file)

# Construct the model and task numbers
model_number = settings["optimization_models"].split("Model")[1].split(":")[0].strip()
task_number = settings["tasks"].split("Task")[1].split(":")[0].strip()
reformulations_per_variation = int(settings["reformulations_per_variation"])

# Construct the full path to input and output JSON files
input_file_path = os.path.join(script_directory, f'JSON2_solved_variations_{model_number}_{task_number}.json')
output_file_path = os.path.join(script_directory, f'JSON3_reformulation_{model_number}_{task_number}.json')

# Load the input JSON file
with open(input_file_path, 'r') as infile:
    data = json.load(infile)

# Initialize the output data structure
output_data = {"variations": []}

# Loop through each variation
for variation in data["variations"]:
    # Generate reformulated questions as per the number specified in the settings
    for i in range(1, reformulations_per_variation + 1):
        # Print the console log message
        print(f"Reformulating question {variation['id']}.{i}")
        new_variation = variation.copy()
        new_id = f"{variation['id']}.{i}"
        new_variation["id"] = new_id
        new_question = reformulate_question(variation['question_variation'])
        new_variation["question_reformulation"] = new_question
        output_data["variations"].append(new_variation)

# Save to a new JSON file
with open(output_file_path, 'w') as outfile:
    json.dump(output_data, outfile, indent=4)
