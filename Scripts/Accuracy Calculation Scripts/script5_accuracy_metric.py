import os
import json

# Compute averages from the data list
def compute_averages(data_list):
    total_files = len(data_list)
    avg_accuracy = sum(item[0] for item in data_list) / total_files
    avg_percentage_correct = sum(item[1] for item in data_list) / total_files
    avg_qset_correctness = {}
    for key in data_list[0][2]:
        avg_qset_correctness[key] = f"{sum(float(item[2][key].replace('%','')) for item in data_list) / total_files:.2f}%"
    return avg_accuracy, avg_qset_correctness, avg_percentage_correct

# Initialize variables and get current directory path
curr_dir = os.path.dirname(os.path.abspath(__file__))
data_list = []
settings_data = {}
all_experiments_have_data = True

# Loop through each experiment folder and extract data
for folder in os.listdir(curr_dir):
    if folder.startswith("experiment r="):
        settings_file = os.path.join(curr_dir, folder, "experiment_settings.json")
        if os.path.exists(settings_file):
            with open(settings_file, 'r') as f:
                settings_data = json.load(f)
                llm_str = settings_data.get("llms", "").split(":")[0].strip()
                llm_number = int(llm_str.replace("LLM", "")) if "LLM" in llm_str else None
                task_str = settings_data.get("tasks", "").split(":")[0].strip()
                task_number = int(task_str.replace("Task", "")) if "Task" in task_str else None
            found_accuracy_file = False
            for file in os.listdir(os.path.join(curr_dir, folder)):
                if file.startswith("JSON7_accuracy"):
                    found_accuracy_file = True
                    with open(os.path.join(curr_dir, folder, file), 'r') as f:
                        data = json.load(f)
                        data_list.append([
                            float(data['accuracy'].replace('%', '')),
                            float(data['percentage_correct'].replace('%', '')),
                            data['questionset_correctness']
                        ])
                    break
            if not found_accuracy_file:
                all_experiments_have_data = False

# Handle cases where not all experiment folders have data or no valid data is found
# If valid data exists, compute averages and save to a JSON file
if not all_experiments_have_data:
    print("Please finish all experiments first, before calculating the accuracy metric")
elif not data_list:
    print("No valid data found in the experiment folders.")
else:
    avg_accuracy, avg_qset_correctness, avg_percentage_correct = compute_averages(data_list)
    result = {
        "llms": settings_data.get("llms", ""),
        "optimization_models": settings_data.get("optimization_models", ""),
        "tasks": settings_data.get("tasks", ""),
        "distribution": settings_data.get("distribution", ""),
        "ICL": settings_data.get("ICL", ""),
        "accuracy_metric": f"{avg_accuracy:.2f}%",
        "average_percentage_correct": f"{avg_percentage_correct:.2f}%",
        "average_questionset_correctness": avg_qset_correctness
    }
    output_file_name = f'JSON8_accuracy_metric_{llm_number}_{task_number}.json'
    output_file_path = os.path.join(curr_dir, output_file_name)
    with open(output_file_path, 'w') as f:
        json.dump(result, f, indent=4)
