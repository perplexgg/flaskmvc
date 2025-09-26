import json
import os

DATA_FILE = os.path.join(os.getcwd(), "data.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"students": {}, "staff": [], "hour_entries": []}
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except Exception:
            return {"students": {}, "staff": [], "hour_entries": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
