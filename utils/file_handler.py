import json

def load_json(filename):
    with open(f"data/{filename}", "r") as f:
        return json.load(f)