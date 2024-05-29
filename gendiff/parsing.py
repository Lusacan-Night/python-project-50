import json
import yaml

def parse_file(filepath):
    if filepath.endswith("json"):
        with open(filepath, 'r') as file:
            json_file = json.load(file)
            return json_file
        
    elif filepath.endswith("yml") or filepath.endswith("yaml"):
        with open(filepath, 'r') as file:
            yaml_file = yaml.safe_load(file)
            return yaml_file