import json

# Load the JSON data from the file
with open('JSON6_evaluated_knapsack_transform.json', 'r') as file:
    data = json.load(file)

# Initialize a counter for 'correct' field
correct_count = 0

# Iterate over each item in the 'variations' list
for variation in data['variations']:
    # If the 'correct' field is true, increment the counter
    if variation['correct'] == True:
        correct_count += 1

# Calculate the percentage
total_variations = len(data['variations'])
percentage_correct = (correct_count / total_variations) * 100

# Prepare the output as a dictionary with the accuracy
output = {
    "accuracy": f"{percentage_correct:.2f}%"
}

# Write the output to a new JSON file
with open('JSON7_accuracy_knapsack_transform.json', 'w') as outfile:
    json.dump(output, outfile, indent=4)
