import json
import os
import traceback
import shutil

def read_config(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)

def is_deepest_level(data):
    for key, value in data.items():
        if isinstance(value, dict) and ("select" in value or any(isinstance(v, dict) for v in value.values())):
            return False
    return True

def write_experiment_settings_to_file(folder_path, settings, path_info, experiment_name):
    experiment_data = {}
    experiment_data.update(settings)
    experiment_data.update(path_info)
    experiment_data["experiments"] = experiment_name
    
    with open(os.path.join(folder_path, "experiment_settings.json"), 'w') as f:
        json.dump(experiment_data, f, indent=4)

def copy_scripts_to_folder(folder_type, experiment_folder):
    source_folder = ""
    if folder_type == "LLM Evaluations":
        source_folder = os.path.join(os.getcwd(), "Scripts", "LLM Evaluation Scripts")
    elif folder_type == "Question Generation":
        source_folder = os.path.join(os.getcwd(), "Scripts", "Question Generation Scripts")
    
    for file_name in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, file_name)
        dest_file_path = os.path.join(experiment_folder, file_name)
        shutil.copy2(source_file_path, dest_file_path)

def create_folders(data, base_path, settings, folder_type, path_info={}):
    for key, value in data.items():
        if isinstance(value, dict):
            category = key
            for subkey, subvalue in value.items():
                if subvalue.get("select"):
                    new_folder_path = os.path.join(base_path, subkey)
                    print(f"Creating folder: {new_folder_path}")
                    os.makedirs(new_folder_path, exist_ok=True)
                    
                    updated_path_info = path_info.copy()
                    updated_path_info[category] = subkey

                    if is_deepest_level(subvalue):
                        num_experiments = int(settings.get("experiments_per_model", 1))
                        for i in range(1, num_experiments + 1):
                            experiment_name = f"experiment r={i}"
                            experiment_folder = os.path.join(new_folder_path, experiment_name)
                            print(f"Creating experiment folder: {experiment_folder}")
                            os.makedirs(experiment_folder, exist_ok=True)
                            
                            write_experiment_settings_to_file(experiment_folder, settings, updated_path_info, experiment_name)
                            
                            copy_scripts_to_folder(folder_type, experiment_folder)
                    else:
                        nested_dicts = {k: v for k, v in subvalue.items() if isinstance(v, dict)}
                        create_folders(nested_dicts, new_folder_path, settings, folder_type, updated_path_info)
                else:
                    nested_dicts = {k: v for k, v in subvalue.items() if isinstance(v, dict)}
                    create_folders(nested_dicts, base_path, settings, folder_type, path_info)

if __name__ == "__main__":
    configs = [
        ("llm_evaluation_config.json", "LLM Evaluations"),
        ("question_generation_config.json", "Question Generation")
    ]
    
    for config_file, top_folder in configs:
        if os.path.exists(config_file):
            print(f"\nProcessing {config_file}\n")
            try:
                data = read_config(config_file)
                settings = data.get("settings", {})
                base_path = os.path.join(os.getcwd(), top_folder)
                
                create_folders(data.get("selection", {}), base_path, settings, top_folder)
            except Exception as e:
                print(f"Error processing {config_file}: {e}")
                print(traceback.format_exc())
