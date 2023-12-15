import json
import os

def preprocess_code(code):
    # Preprocesses the code by extracting content from within triple backticks
    if '```python' in code:
        try:
            return code.split('```python')[1].split('```')[0].strip()
        except IndexError:
            return code
    elif '```' in code:
        return code.split('```')[1].strip()
    else:
        return code

def get_model_task_numbers(settings_path):
    # Extracts model, task, and LLM numbers from the settings file
    with open(settings_path, 'r') as f:
        settings_data = json.load(f)
    
    llms_number = settings_data["llms"].split("LLM")[1].split(":")[0].strip()
    model_number = settings_data["optimization_models"].split("Model")[1].split(":")[0].strip()
    task_number = settings_data["tasks"].split("Task")[1].split(":")[0].strip()

    return llms_number, model_number, task_number

def run_code_and_get_output(code):
    # Executes the given code and captures the output, and objective value
    try:
        exec_globals = {}
        exec(code, exec_globals)
        selected_items = exec_globals.get('selected_items', 'No result')
        objective_value = str(exec_globals.get('objective_value', 'No result'))
        return str(selected_items), objective_value
    except Exception as e:
        return f'Error: {e}', 'Error'

# Directory and file paths setup
script_directory = os.path.dirname(os.path.abspath(__file__))
settings_path = os.path.join(script_directory, 'experiment_settings.json')
llms_number, model_number, task_number = get_model_task_numbers(settings_path)
input_filename = os.path.join(script_directory, f"JSON4_llm_response_{model_number}_{task_number}.json")
output_filename = os.path.join(script_directory, f"JSON5_solved_models_from_llm_{model_number}_{task_number}.json")

# Load and process the data
with open(input_filename, 'r') as f:
    data = json.load(f)

for variation in data['variations']:
    llm_code = variation['llm_model']
    preprocessed_code = preprocess_code(llm_code)
    variation['llm_model_preprocessed'] = preprocessed_code
    solver_output, llm_objective_value = run_code_and_get_output(preprocessed_code)
    variation['llm_optimum'] = solver_output
    variation['llm_objective_value'] = llm_objective_value

# Save the processed data
with open(output_filename, 'w') as f:
    json.dump(data, f, indent=4)
