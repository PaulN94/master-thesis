import sys
import os
import random
import json
import importlib
import hashlib

# Function to compute SHA256 hash of a given string
def compute_sha256(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()

# Get the directory of the currently executing script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Traverse up to Workspace Root
experiment_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(script_directory))))

# Add the experiment directory to sys.path for importing
sys.path.append(experiment_directory)

# Construct the full path to experiment_settings.json
settings_path = os.path.join(script_directory, "experiment_settings.json")

# Load the settings from the experiment_settings.json file
with open(settings_path, "r") as settings_file:
    settings = json.load(settings_file)

# Extract the model number from the settings
model_number = int(settings["optimization_models"].split("Model")[1].split(":")[0].strip())

# Compute the full path to the relevant model file in the "Optimization Models" folder
model_file_name = f"model{model_number}_knapsack.py"
model_file_path = os.path.join(experiment_directory, "Experiment", "Optimization Models", model_file_name)

# Import the module dynamically
spec = importlib.util.spec_from_file_location(f"model{model_number}", model_file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Compute the SHA256 hash of the module's content
with open(model_file_path, 'r') as f:
    module_content = f.read()
hash_base_model = compute_sha256(module_content)

# Construct the import string for the Templates folder in workspace root
task_number = settings["tasks"].split("Task")[1].split(":")[0].strip()
module_name = f"Templates.dict_{model_number}_{task_number}_templates"

# Using importlib to dynamically import the module and dictionary
module = importlib.import_module(module_name)
dict_template = getattr(module, f"dict_{model_number}_{task_number}")

# Create an empty dictionary to store the generated questions and answers
generated_questions = dict(variations=[])

# Create a set to store the SHA256 hashes of all generated answer variations
answer_hashes = set()

# Loop through each template
for template in dict_template['templates']:
    template_id = template['id']
    question_template = template['question_template']
    answer_template = template['answer_template']
    answer_template_section = template.get('answer_template_section', "")
    variables = template['variables']

    # Variable values storage for use in arrayLength and uniqueID
    variable_values = {}
    unique_id_values = {}

    # Generate variations for each template based on the settings file
    for i in range(1, int(settings["variations_per_template"]) + 1):
        new_id = f"{template_id}.{i}"
        new_question = question_template
        new_answer = answer_template
        new_answer_section = answer_template_section

        # Calculate hash for the answer_variation and compare with hash_base_model
        answer_hash = compute_sha256(new_answer)

        # Regenerate the answer_variation if the hash is the same as 1. the hash of the optimization model to be transformed; or 2. the hash of a previous answer_variation
        while answer_hash == hash_base_model or answer_hash in answer_hashes:
            # Reset variables for regeneration
            variable_values = {}
            unique_id_values = {}

            # Fill in the placeholders in the question and answer
            for variable in variables:
                var_name = variable['name']
                var_type = variable['type']
                unique_id = variable.get('uniqueID')

                if var_type == "int":
                    var_range = variable['range']
                    if isinstance(var_range[1], dict):
                        var_range[1] = variable_values[var_range[1]['var']] - var_range[1].get('subtract', 0)
                    var_value = random.randint(var_range[0], var_range[1])

                    # Ensure uniqueness within the same uniqueID
                    if unique_id:
                        while unique_id in unique_id_values and var_value in unique_id_values[unique_id]:
                            var_value = random.randint(var_range[0], var_range[1])
                        if unique_id not in unique_id_values:
                            unique_id_values[unique_id] = []
                        unique_id_values[unique_id].append(var_value)

                elif var_type == "float":
                    var_range = variable['range']
                    var_value = random.uniform(var_range[0], var_range[1])
                    var_value = round(var_value, 2)

                elif var_type == "array":
                    array_length = variable['arrayLength']
                    if 'var' in array_length:
                        array_length = variable_values[array_length['var']]
                    var_range = variable['range']
                    var_value = [random.randint(var_range['min'], var_range['max']) for _ in range(array_length)]

                # Store the value for future reference
                variable_values[var_name] = var_value

                new_question = new_question.replace(f"{{{var_name}}}", str(var_value))
                new_answer = new_answer.replace(f"{{{var_name}}}", str(var_value))
                new_answer_section = new_answer_section.replace(f"{{{var_name}}}", str(var_value))

            # Calculate hash again for the regenerated answer_variation
            answer_hash = compute_sha256(new_answer)

        # Add the hash to answer_hashes set to track it
        answer_hashes.add(answer_hash)

        # Reset unique_id_values for next iteration
        unique_id_values = {}

        # Add the new question and answer to the generated_questions dictionary
        new_variation = {
            "id": new_id,
            "question_variation": new_question,
            "answer_variation": new_answer,
        }
        if new_answer_section:
            new_variation["answer_section"] = new_answer_section
        generated_questions['variations'].append(new_variation)

# Save the generated_questions dictionary to a file in JSON format
output_file_name = os.path.join(script_directory, f'JSON1_variations_{model_number}_{task_number}.json')
with open(output_file_name, 'w') as f:
    json.dump(generated_questions, f, indent=4)
