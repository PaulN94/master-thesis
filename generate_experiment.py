import json
import os
import traceback  # For better error descriptions

def read_config(file_name):
    """Read the JSON configuration file and return its content."""
    with open(file_name, 'r') as f:
        return json.load(f)

def is_deepest_level(data):
    """Check if the current dictionary is at the deepest level."""
    for key, value in data.items():
        if isinstance(value, dict) and ("select" in value or any(isinstance(v, dict) for v in value.values())):
            return False
    return True

def create_folders(data, base_path, settings):
    """Recursive function to create folders from the JSON structure."""
    for key, value in data.items():
        if isinstance(value, dict):
            if value.get("select"):  # Check if 'select' key is present and true
                new_folder_path = os.path.join(base_path, key)
                print(f"Creating folder: {new_folder_path}")  # Debugging
                os.makedirs(new_folder_path, exist_ok=True)
                
                # Check if the current dictionary is at the deepest level
                if is_deepest_level(value):
                    num_experiments = int(settings["experiments_per_model"])
                    for i in range(1, num_experiments + 1):
                        experiment_folder = os.path.join(new_folder_path, f"experiment r={i}")
                        print(f"Creating experiment folder: {experiment_folder}")  # Debugging
                        os.makedirs(experiment_folder, exist_ok=True)
                else:
                    nested_dicts = {k: v for k, v in value.items() if isinstance(v, dict)}
                    create_folders(nested_dicts, new_folder_path, settings)
            else:
                # If 'select' key is not present or set to false, continue recursively without creating a new folder
                nested_dicts = {k: v for k, v in value.items() if isinstance(v, dict)}
                create_folders(nested_dicts, base_path, settings)

if __name__ == "__main__":
    # Check for each configuration file and create the respective folder structure
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
                
                # Process the initial "selection" content
                create_folders(data["selection"], base_path, settings)
            except Exception as e:
                print(f"Error processing {config_file}: {e}")
                print(traceback.format_exc())  # Print the full traceback for better understanding
