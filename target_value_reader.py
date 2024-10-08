import json

def load_target_values(json_path='target_values.json'):
    try:
        with open(json_path, 'r') as json_file:
            target_values = json.load(json_file)
        print("Loaded target values successfully!")
        return target_values
    except FileNotFoundError:
        print("Error: target_values.json file not found.")
        return None

# Load target values into the program
target_values = load_target_values()
