import json

# Read the JSON5 file
input_file = 'JSON5_solved_transformed_models_knapsack_transform.json'
with open(input_file, 'r') as f:
    data = json.load(f)

# Loop through each entry and compare 'solver_output' and 'llm_optimum'
for entry in data['variations']:
    solver_output = entry['solver_output']
    llm_optimum = entry['llm_optimum']
    
    # Add the 'correct' field based on the comparison
    entry['correct'] = (solver_output == llm_optimum)

# Save the updated data to a new JSON6 file
output_file = 'JSON6_evaluated_knapsack_transform.json'
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)
