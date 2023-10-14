import os
import openai
import json
from dotenv import load_dotenv
import random

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def get_example(entry):
    """Construct an example from an entry."""
    question = entry["question_variation"]
    answer = entry["answer_section"] if "answer_section" in entry else entry["answer_variation"]
    return f"{question}\n{answer}"

# Get the directory of the currently executing script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Find the root directory by going up the directory tree until you reach the 'Experiment' folder
root_directory = script_directory
while os.path.basename(root_directory) != 'Experiment' and root_directory != os.path.dirname(root_directory):
    root_directory = os.path.dirname(root_directory)

# Construct the path to the 'Optimization Models' folder
optimization_models_path = os.path.join(root_directory, "Optimization Models")

# Construct the full path to experiment_settings.json
settings_path = os.path.join(script_directory, "experiment_settings.json")

# Load settings from experiment_settings.json
with open(settings_path, "r") as settings_file:
    settings = json.load(settings_file)

# Extract number from ICL description
icl_number = int(settings["ICL"].split(":")[0][-1])

# Continue with the existing logic to get the task, model, and experiment descriptions
task_desc = settings["tasks"]
task_number = task_desc.split(":")[0][-1]  # Extracting the task number

model_desc = settings["optimization_models"]
model_number = model_desc.split(":")[0][-1]  # Extracting the model number

experiment_desc = settings["experiments"]

# Get the llms value from the settings and convert to lowercase
llms_model = settings["llms"].split(":")[1].strip().lower()


# Constructing the path to the input file using the modified code
model_folder_name = model_desc.strip().split(":")[0] + ": " + model_desc.strip().split(":")[1].strip()
task_folder_name = task_desc.strip().split(":")[0] + ": " + task_desc.strip().split(":")[1].strip()

base_path = os.path.join(root_directory, "Question Generation", model_folder_name, task_folder_name, experiment_desc.strip())
input_json_filename = os.path.join(base_path, f"JSON3_reformulation_{model_number}_{task_number}.json")

# System message and log setup based on task_number
if task_number == "1":
    system_message = "Build a Python optimization model according to the users description and return only the executable code and nothing else"
    log_message = "Model {} built"
    output_filename = os.path.join(script_directory, f"JSON4_llm_response_{model_number}_{task_number}.json")
elif task_number == "2":
    # Import the model based on model_number
    with open(os.path.join(optimization_models_path, f"model{model_number}_knapsack.py"), "r") as model_file:
        model_content = model_file.read()
    system_message = "Modify the following Python optimization model according to the users question and return only the modified executable code and nothing else"
    log_message = "Model {} transformed"
    output_filename = os.path.join(script_directory, f"JSON4_llm_response_{model_number}_{task_number}.json")

# Load the original JSON file
with open(input_json_filename, "r") as f:
    data = json.load(f)

# Iterate over each question and send it to OpenAI API
for i, variation in enumerate(data['variations']):
    question = variation['question_reformulation']
    entry_id = variation['id']  # Extracting the id from the entry
    question_set_number = int(entry_id.split(".")[2])
    
    user_messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": question}
    ]

    if task_number == "2":
        user_messages.append({"role": "user", "content": model_content})


    example_ids = {}  # This will store the IDs of the examples sent with the question

    # Add examples to the message if needed
    if icl_number > 0:
        # Determine the pool of examples to draw from based on distribution_desc
        if settings["distribution"] == "Dist0: Out-of-distribution_ICL":
            example_pool = [e for e in data['variations'] if int(e['id'].split(".")[2]) != question_set_number]
        else:  # "Dist1: In-distribution_ICL"
            example_pool = [e for e in data['variations'] if int(e['id'].split(".")[2]) == question_set_number]
        
        # Randomly draw the examples
        selected_examples = random.sample(example_pool, min(icl_number, len(example_pool)))
        examples_message = "Examples:\n\n"
        examples_message += "\n\n".join([get_example(e) for e in selected_examples])

        # Save the IDs of the selected examples
        for idx, example in enumerate(selected_examples, 1):
            example_ids[str(idx)] = example['id']
        
        user_messages.append({"role": "user", "content": examples_message})

    # Create the conversation using the dynamic model determined from settings
    response = openai.ChatCompletion.create(
        model=llms_model,
        messages=user_messages
    )

    # Extract the model response from OpenAI
    llm_model_response = response['choices'][0]['message']['content']

    # Add the llm_model_response and example IDs to the question entry in the in-memory JSON object
    data['variations'][i]['llm_model'] = llm_model_response
    if example_ids:
        data['variations'][i]['icl_example_ids'] = example_ids

    # Log the request with the id
    print(log_message.format(entry_id))

# Save the modified object to the specified output file
with open(output_filename, "w") as f:
    json.dump(data, f, indent=4)
