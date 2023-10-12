import json

# Load settings from the experiment_settings.json file
with open('experiment_settings.json', 'r') as settings_file:
    settings = json.load(settings_file)

# Extract model and task numbers from the settings
model_string = settings['optimization_models']
task_string = settings['tasks']

model_number = model_string.split('Model')[1].split(':')[0].strip()
task_number = task_string.split('Task')[1].split(':')[0].strip()

# Define input and output filenames based on the extracted numbers
input_file = f'JSON5_solved_models_from_llm_{model_number}_{task_number}.json'
output_file = f'JSON6_evaluated_{model_number}_{task_number}.json'

# Read the input JSON5 file
with open(input_file, 'r') as f:
    data = json.load(f)

# Loop through each entry and compare 'solver_output' and 'llm_optimum'
for entry in data['variations']:
    solver_output = entry['solver_output']
    llm_optimum = entry['llm_optimum']

    # Add the 'correct' field based on the comparison
    entry['correct'] = (solver_output == llm_optimum)

# Save the updated data to the output JSON6 file
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)
