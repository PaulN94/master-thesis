import json
import re  # for regular expression extraction

def get_model_task_numbers(settings_path):
    with open(settings_path, 'r') as f:
        settings_data = json.load(f)
    
    # Extract model number from the "optimization_models" field using split
    model_number = settings_data["optimization_models"].split("Model")[1].split(":")[0].strip()

    # Extract task number from the "tasks" field using split
    task_number = settings_data["tasks"].split("Task")[1].split(":")[0].strip()

    return model_number, task_number

def run_code_and_get_output(code):
    try:
        # Define the execution environment, if necessary
        exec_globals = {}

        # Execute the code
        exec(code, exec_globals)

        # Extract solver output from the global environment
        solver_output = exec_globals.get('selected_items', 'No result')

        return str(solver_output)

    except Exception as e:
        return f'Error: {e}'

# Import settings file
model_number, task_number = get_model_task_numbers('experiment_settings.json')
if not model_number or not task_number:
    raise ValueError("Could not extract model or task number from settings file.")

input_filename = f"JSON4_llm_response_{model_number}_{task_number}.json"
output_filename = f"JSON5_solved_models_from_llm_{model_number}_{task_number}.json"

# Read input JSON file
with open(input_filename, 'r') as f:
    data = json.load(f)

# Run Python code for each variation
for variation in data['variations']:
    llm_code = variation['llm_model_response']
    solver_output = run_code_and_get_output(llm_code)
    variation['llm_optimum'] = solver_output

# Write new JSON file with solver outputs
with open(output_filename, 'w') as f:
    json.dump(data, f, indent=4)
