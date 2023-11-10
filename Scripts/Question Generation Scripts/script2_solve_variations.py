import os
import json

def run_code_and_get_output(code):
    try:
        # Initialize the global environment
        exec_globals = {}

        # Execute the code
        exec(code, exec_globals)

        # Extract solver output from the global environment
        solver_output = exec_globals.get('selected_items', 'No result')
        objective_value = exec_globals.get('objective_value', 'No objective value') # Capture objective value
        fingerprint = exec_globals.get('fingerprint', 'No fingerprint') # Capture fingerprint if available

        return str(solver_output), str(objective_value), str(fingerprint)

    except Exception as e:
        return f'Error: {e}', 'Error', 'Error'

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

# Construct the full path to input and output JSON files
input_file_name = os.path.join(script_directory, f'JSON1_variations_{model_number}_{task_number}.json')
output_file_name = os.path.join(script_directory, f'JSON2_solved_variations_{model_number}_{task_number}.json')

# Read JSON file
with open(input_file_name, 'r') as f:
    data = json.load(f)

# Run Python code for each variation
for variation in data['variations']:
    answer_code = variation['answer_variation']
    solver_output, objective_value, fingerprint = run_code_and_get_output(answer_code)
    variation['solver_output'] = solver_output
    variation['objective_value'] = objective_value # Add objective value to the variation
    variation['true_model_fingerprint'] = fingerprint # Add fingerprint to the variation

# Write new JSON file with solver outputs
with open(output_file_name, 'w') as f:
    json.dump(data, f, indent=4)
