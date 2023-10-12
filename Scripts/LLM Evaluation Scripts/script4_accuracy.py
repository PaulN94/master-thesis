import json

# Load the experiment settings
with open('experiment_settings.json', 'r') as settings_file:
    settings = json.load(settings_file)

# Extract model and task numbers from settings
model_number = settings["optimization_models"].split("Model")[1].split(":")[0].strip()
task_number = settings["tasks"].split("Task")[1].split(":")[0].strip()

# Form the input and output file names
input_filename = f"JSON6_evaluated_{model_number}_{task_number}.json"
output_filename = f"JSON7_accuracy_{model_number}_{task_number}.json"

# Load the JSON data from the input file
with open(input_filename, 'r') as file:
    json_data = json.load(file)

# Your data processing remains unchanged
overall_correct_questions = 0
overall_total_questions = 0
questionsets = {}

for var in json_data["variations"]:
    qset = int(var["id"].split(".")[2])
    if qset not in questionsets:
        questionsets[qset] = {"total": 0, "correct": 0}
    questionsets[qset]["total"] += 1
    overall_total_questions += 1
    if var["correct"]:
        questionsets[qset]["correct"] += 1
        overall_correct_questions += 1

percentage_correct = (overall_correct_questions / overall_total_questions) * 100
final_score = 0
all_correct_questionsets = []
not_all_correct_questionsets = []
questionset_accuracy = {}
total_questionsets = len(questionsets)

for qset_num, qset in questionsets.items():
    qset_percentage = (qset["correct"] / qset["total"]) * 100
    questionset_accuracy[qset_num] = f"{qset_percentage:.2f}%"
    if qset["total"] == qset["correct"]:
        final_score += 1
        all_correct_questionsets.append(qset_num)
    else:
        not_all_correct_questionsets.append(qset_num)

accuracy = (final_score / total_questionsets) * 100

accuracy_dict = {
    "percentage_correct": f"{percentage_correct:.2f}%",
    "overall_accuracy": f"{accuracy:.2f}%",
    "all_correct_questionsets": all_correct_questionsets,
    "not_all_correct_questionsets": not_all_correct_questionsets,
    "questionset_accuracy": questionset_accuracy
}

# Write to the output file
with open(output_filename, 'w') as file:
    json.dump(accuracy_dict, file, indent=4)

print(f"The percentage of correct questions is: {percentage_correct:.2f}%")
print(f"The overall accuracy is: {accuracy:.2f}%")
print(f"Details have been written to {output_filename}.")
