import json
import os

# Define the base path for the data directory
DATA_DIR = 'config/user_data'

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Load existing data for a specific user
def load_data(user_id):
    user_file = os.path.join(DATA_DIR, f"{user_id}.json")
    if os.path.exists(user_file):
        with open(user_file, 'r') as file:
            return json.load(file)
    return {}

# Save data for a specific user
def save_data(user_id, data):
    user_file = os.path.join(DATA_DIR, f"{user_id}.json")
    with open(user_file, 'w') as file:
        json.dump(data, file, indent=4)

# Add a new record for a user
def add_record(user_id, name, position):
    data = load_data(user_id)
    data[name] = position
    save_data(user_id, data)

# Update an existing record for a user
def update_record(user_id, name, position):
    data = load_data(user_id)
    if name in data:
        data[name] = position
        save_data(user_id, data)
    else:
        print("Record not found.")

# Delete a record for a user
def delete_record(user_id, name):
    data = load_data(user_id)
    if name in data:
        del data[name]
        save_data(user_id, data)
    else:
        print("Record not found.")