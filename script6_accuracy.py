import json

# Load the JSON data from the file
with open('JSON6_evaluated_knapsack_transform.json', 'r') as file:
    json_data = json.load(file)

# Initialize counters for overall correct questions and total questions
overall_correct_questions = 0
overall_total_questions = 0

# Initialize an empty dictionary to hold count of correct answers per questionset
questionsets = {}

# Iterate through the variations in the JSON data
for var in json_data["variations"]:
    # Extract the questionset number from the id
    qset = int(var["id"].split(".")[2])
    
    # Check if the questionset is already in the dictionary
    if qset not in questionsets:
        questionsets[qset] = {"total": 0, "correct": 0}
    
    # Increment the total count for this questionset and overall total questions
    questionsets[qset]["total"] += 1
    overall_total_questions += 1

    # If the answer is correct, increment the correct count for this questionset and overall correct questions
    if var["correct"]:
        questionsets[qset]["correct"] += 1
        overall_correct_questions += 1

# Calculate the percentage of correct questions of all questions
percentage_correct = (overall_correct_questions / overall_total_questions) * 100

# Initialize a counter for the final score
final_score = 0

# Lists to hold questionsets with all correct answers and those without
all_correct_questionsets = []
not_all_correct_questionsets = []

# Dictionary to store the accuracy percentage for each question set
questionset_accuracy = {}

# Count the number of questionsets
total_questionsets = len(questionsets)

# Iterate through the questionsets to calculate the final score, populate the lists, and store accuracy percentage
for qset_num, qset in questionsets.items():
    qset_percentage = (qset["correct"] / qset["total"]) * 100
    questionset_accuracy[qset_num] = f"{qset_percentage:.2f}%"
    
    if qset["total"] == qset["correct"]:
        final_score += 1
        all_correct_questionsets.append(qset_num)
    else:
        not_all_correct_questionsets.append(qset_num)

# Calculate the overall accuracy
accuracy = (final_score / total_questionsets) * 100  # as a percentage

# Create a new dictionary with the accuracy, lists, and individual question set accuracy percentages
accuracy_dict = {
    "percentage_correct": f"{percentage_correct:.2f}%",
    "overall_accuracy": f"{accuracy:.2f}%",
    "all_correct_questionsets": all_correct_questionsets,
    "not_all_correct_questionsets": not_all_correct_questionsets,
    "questionset_accuracy": questionset_accuracy
}

# Write the accuracy and lists to a new JSON file
with open('JSON7_accuracy_knapsack_transform.json', 'w') as file:
    json.dump(accuracy_dict, file, indent=4)

# Confirmation message
print(f"The percentage of correct questions is: {percentage_correct:.2f}%")
print(f"The overall accuracy is: {accuracy:.2f}%")
print("Details have been written to JSON7_accuracy_knapsack_transform.json.")
