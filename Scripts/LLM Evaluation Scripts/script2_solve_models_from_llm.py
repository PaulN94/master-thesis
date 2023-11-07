import json
import os

# Preprocessing of the code.
def preprocess_code(code):
    # If "python" is present and the code is enclosed in triple backticks, extract the code
    if '```python' in code:
        try:
            return code.split('```python')[1].split('```')[0].strip()
        except IndexError:
            return code
    # If there's no "python" tag, but the code is still enclosed in triple backticks, extract it
    elif '```' in code:
        return code.split('```')[1].strip()
    # If none of the conditions apply, return the original code
    else:
        return code

# Function to extract the numbers associated with the model, task, and LLM from a settings file.
def get_model_task_numbers(settings_path):
    # Open and read the settings file
    with open(settings_path, 'r') as f:
        settings_data = json.load(f)
    
    # Extract numbers from the respective settings
    llms_number = settings_data["llms"].split("LLM")[1].split(":")[0].strip()
    model_number = settings_data["optimization_models"].split("Model")[1].split(":")[0].strip()
    task_number = settings_data["tasks"].split("Task")[1].split(":")[0].strip()

    # Return the extracted numbers
    return llms_number, model_number, task_number

# Function to execute the given code and get its output or error.
def run_code_and_get_output(code):
    try:
        # Set up a clean global namespace for execution
        exec_globals = {}
        # Execute the provided code
        exec(code, exec_globals)
        # Try to get the 'selected_items' from the executed code's namespace
        solver_output = exec_globals.get('selected_items', 'No result')
        return str(solver_output)
    except Exception as e:
        # If there's an error during execution, return the error message
        return f'Error: {e}'

# Path to the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))
# Construct path to the settings file
settings_path = os.path.join(script_directory, 'experiment_settings.json')

# Get the LLM, model, and task numbers from the settings file
llms_number, model_number, task_number = get_model_task_numbers(settings_path)
# Validate the model and task numbers
if not model_number or not task_number:
    raise ValueError("Could not extract model or task number from settings file.")

# Construct filenames based on the model and task numbers
input_filename = os.path.join(script_directory, f"JSON4_llm_response_{model_number}_{task_number}.json")
output_filename = os.path.join(script_directory, f"JSON5_solved_models_from_llm_{model_number}_{task_number}.json")

# Load the data from the input file
with open(input_filename, 'r') as f:
    data = json.load(f)

# Process each variation in the data
for variation in data['variations']:
    # Get the LLM code from the variation
    llm_code = variation['llm_model']
    
    # Preprocess the code
    preprocessed_code = preprocess_code(llm_code)
    # Store the preprocessed code in the variation
    variation['llm_model_preprocessed'] = preprocessed_code
    # Execute the code and get the solver's output
    solver_output = run_code_and_get_output(preprocessed_code)
    # Store the output in the variation
    variation['llm_optimum'] = solver_output

# Save the processed data to the output file
with open(output_filename, 'w') as f:
    json.dump(data, f, indent=4)
