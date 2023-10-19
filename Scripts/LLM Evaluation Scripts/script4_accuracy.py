import json
import os  # for path manipulations

# Get the directory of the currently executing script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the experiment_settings.json file
settings_path = os.path.join(script_directory, 'experiment_settings.json')

# Load the experiment settings
with open(settings_path, 'r') as settings_file:
    settings = json.load(settings_file)

# Extract model and task numbers from settings
model_number = settings["optimization_models"].split("Model")[1].split(":")[0].strip()
task_number = settings["tasks"].split("Task")[1].split(":")[0].strip()

# Form the input and output file names
input_filepath = os.path.join(script_directory, f"JSON6_evaluated_{model_number}_{task_number}.json")
output_filepath = os.path.join(script_directory, f"JSON7_accuracy_{model_number}_{task_number}.json")

# Load the JSON data from the input file
with open(input_filepath, 'r') as file:
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
questionset_correctness = {}  # Updated variable name
total_questionsets = len(questionsets)

for qset_num, qset in questionsets.items():
    qset_percentage = (qset["correct"] / qset["total"]) * 100
    questionset_correctness[qset_num] = f"{qset_percentage:.2f}%"
    if qset["total"] == qset["correct"]:
        final_score += 1
        all_correct_questionsets.append(qset_num)
    else:
        not_all_correct_questionsets.append(qset_num)

accuracy_value = (final_score / total_questionsets) * 100  # Renamed the variable for clarity

accuracy_dict = {
    "percentage_correct": f"{percentage_correct:.2f}%",
    "accuracy": f"{accuracy_value:.2f}%",  # Updated key name
    "all_correct_questionsets": all_correct_questionsets,
    "not_all_correct_questionsets": not_all_correct_questionsets,
    "questionset_correctness": questionset_correctness
}

# Write to the output file
with open(output_filepath, 'w') as file:
    json.dump(accuracy_dict, file, indent=4)
