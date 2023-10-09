import json

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

# Read input JSON file
with open('JSON4_llm_response_knapsack_transform.json', 'r') as f:
    data = json.load(f)

# Run Python code for each variation
for variation in data['variations']:
    knapsack_code = variation['knapsack_model_transformed']
    solver_output = run_code_and_get_output(knapsack_code)
    variation['llm_optimum'] = solver_output

# Write new JSON file with solver outputs
with open('JSON5_solved_transformed_models_knapsack_transform.json', 'w') as f:
    json.dump(data, f, indent=4)
