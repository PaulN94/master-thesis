import json
import os  # for path manipulations

# Get the directory of the currently executing script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the experiment_settings.json file
settings_path = os.path.join(script_directory, 'experiment_settings.json')

# Load settings from the experiment_settings.json file
with open(settings_path, 'r') as settings_file:
    settings = json.load(settings_file)

# Extract model and task numbers from the settings
model_string = settings['optimization_models']
task_string = settings['tasks']

model_number = model_string.split('Model')[1].split(':')[0].strip()
task_number = task_string.split('Task')[1].split(':')[0].strip()

# Define input and output filenames based on the extracted numbers
input_filepath = os.path.join(script_directory, f'JSON5_solved_models_from_llm_{model_number}_{task_number}.json')
output_filepath = os.path.join(script_directory, f'JSON6_evaluated_{model_number}_{task_number}.json')

# Read the input JSON5 file
with open(input_filepath, 'r') as f:
    data = json.load(f)

# Loop through each entry and compare the objective values and solver outputs
for entry in data['variations']:
    llm_objective_value = entry.get('llm_objective_value')
    objective_value = entry.get('objective_value')
    solver_output = entry.get('solver_output')
    llm_optimum = entry.get('llm_optimum')

    # Add the 'correct' field based on the comparison
    entry['correct'] = (llm_objective_value == objective_value) and (solver_output == llm_optimum)

# Save the updated data to the output JSON6 file
with open(output_filepath, 'w') as f:
    json.dump(data, f, indent=4)
