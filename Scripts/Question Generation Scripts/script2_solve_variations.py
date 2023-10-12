import json

def run_code_and_get_output(code):
    try:
        # Initialize the global environment
        exec_globals = {}

        # Execute the code
        exec(code, exec_globals)

        # Extract solver output from the global environment
        solver_output = exec_globals.get('selected_items', 'No result')

        return str(solver_output)

    except Exception as e:
        return f'Error: {e}'

# Load the settings from the experiment_settings.json file
with open("experiment_settings.json", "r") as settings_file:
    settings = json.load(settings_file)

# Construct the model and task numbers
model_number = settings["optimization_models"].split("Model")[1].split(":")[0].strip()
task_number = settings["tasks"].split("Task")[1].split(":")[0].strip()

input_file_name = f'JSON1_variations_{model_number}_{task_number}.json'
output_file_name = f'JSON2_solved_variations_{model_number}_{task_number}.json'

# Read JSON file
with open(input_file_name, 'r') as f:
    data = json.load(f)

# Run Python code for each variation
for variation in data['variations']:
    answer_code = variation['answer_variation']
    solver_output = run_code_and_get_output(answer_code)
    variation['solver_output'] = solver_output

# Write new JSON file with solver outputs
with open(output_file_name, 'w') as f:
    json.dump(data, f, indent=4)
