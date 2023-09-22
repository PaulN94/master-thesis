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

# Read JSON file
with open('JSON1_q_and_a_variations_knapsack_transformation.json', 'r') as f:
    data = json.load(f)

# Run Python code for each variation
for variation in data['variations']:
    answer_code = variation['answer_variation']
    solver_output = run_code_and_get_output(answer_code)
    variation['solver_output'] = solver_output

# Write new JSON file with solver outputs
with open('JSON2_q_and_a_variations_knapsack_transformation.json', 'w') as f:
    json.dump(data, f, indent=4)
