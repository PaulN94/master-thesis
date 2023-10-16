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

# Define a function to construct an example from an entry
def get_example(entry):
    """Construct an example from an entry."""
    question = "Question:\n" + entry["question_variation"]
    answer = "Code:\n" + (entry["answer_section"] if "answer_section" in entry else entry["answer_variation"])
    return f"{question}\n\n{answer}\n"

# Get the current script's directory path
script_directory = os.path.dirname(os.path.abspath(__file__))

# Find the root directory which has the name 'Experiment'
root_directory = script_directory
while os.path.basename(root_directory) != 'Experiment' and root_directory != os.path.dirname(root_directory):
    root_directory = os.path.dirname(root_directory)

# Construct paths for optimization models and experiment settings
optimization_models_path = os.path.join(root_directory, "Optimization Models")
settings_path = os.path.join(script_directory, "experiment_settings.json")

# Load experiment settings from the JSON file
with open(settings_path, "r") as settings_file:
    settings = json.load(settings_file)

# Extract relevant details from the settings
icl_number = int(''.join(filter(str.isdigit, settings["ICL"].split(":")[0])))
task_desc = settings["tasks"]
task_number = task_desc.split(":")[0][-1]
model_desc = settings["optimization_models"]
model_number = model_desc.split(":")[0][-1]
experiment_desc = settings["experiments"]
llms_model = settings["llms"].split(":")[1].strip().lower()

# Construct folder names and input JSON filename based on the extracted details
model_folder_name = model_desc.strip().split(":")[0] + ": " + model_desc.strip().split(":")[1].strip()
task_folder_name = task_desc.strip().split(":")[0] + ": " + task_desc.strip().split(":")[1].strip()
base_path = os.path.join(root_directory, "Question Generation", model_folder_name, task_folder_name, experiment_desc.strip())
input_json_filename = os.path.join(base_path, f"JSON3_reformulation_{model_number}_{task_number}.json")

# Construct system message and output filename based on task number
if task_number == "1":
    system_message = "Please build a Python optimization model according to the users description and return only the modified executable model in code and nothing else. The code utilizes the Gurobi solver, to solve the optimization model."
    if icl_number > 0:
        system_message += "\n\nHere are some example questions and their correct codes:\n— EXAMPLES —\n\n{selected_examples}\n\n—"
    log_message = "Model {} built"
    output_filename = os.path.join(script_directory, f"JSON4_llm_response_{model_number}_{task_number}.json")
elif task_number == "2":
    with open(os.path.join(optimization_models_path, f"model{model_number}_knapsack.py"), "r") as model_file:
        model_content = model_file.read()
    system_message = "Please transform the Python optimization model according to the users question and return only the modified unabridged executable model and nothing else.\n\n— OPTIMIZATION MODEL TO TRANSFORM —\n\n{model_content}\n\n—"
    if icl_number > 0:
        system_message += "\n\nHere are some example questions and the sections in the model that are modified to answer the example question. Altough the examples are only sections, remember to output the full modified model to answer the user question:\n— EXAMPLES —\n\n{selected_examples}\n\n—"
    log_message = "Model {} transformed"
    output_filename = os.path.join(script_directory, f"JSON4_llm_response_{model_number}_{task_number}.json")

# Load the input data from the JSON file
with open(input_json_filename, "r") as f:
    data = json.load(f)

# Process each variation in the data, construct user messages and make API calls
for i, variation in enumerate(data['variations']):
    question = variation['question_reformulation']
    entry_id = variation['id']
    question_set_number = int(entry_id.split(".")[2])
    selected_examples_content = ""  # Initialize this to empty

    example_ids = {}
    if icl_number > 0:
        if settings["distribution"] == "Dist0: Out-of-distribution_ICL":
            example_pool = [e for e in data['variations'] if int(e['id'].split(".")[2]) != question_set_number]
        else:
            current_variation_number = int(entry_id.split(".")[3])
            example_pool = [e for e in data['variations'] if int(e['id'].split(".")[2]) == question_set_number and int(e['id'].split(".")[3]) != current_variation_number]
        
        selected_examples = random.sample(example_pool, min(icl_number, len(example_pool)))
        selected_examples_content = "\n\n".join([get_example(e) for e in selected_examples])
        for idx, example in enumerate(selected_examples, 1):
            example_ids[str(idx)] = example['id']

    user_messages = [
        {"role": "system", "content": system_message.format(model_content=model_content, selected_examples=selected_examples_content)},
        {"role": "user", "content": question}
    ]

    # Print details before sending to the API
    print("\n--- Sending to API ---")
    print("Model:", llms_model)
    for msg in user_messages:
        print(f"  Role: {msg['role']}")
        print(f"  Content:\n    {msg['content']}\n")
    print("------------------------\n")

    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model=llms_model,
        messages=user_messages
    )

    # Process the API response and update the data
    llm_model_response = response['choices'][0]['message']['content']
    data['variations'][i]['llm_model'] = llm_model_response
    if example_ids:
        data['variations'][i]['icl_example_ids'] = example_ids

    # Print log message
    print(log_message.format(entry_id))


# Save the updated data to the output JSON file
with open(output_filename, "w") as f:
    json.dump(data, f, indent=4)
