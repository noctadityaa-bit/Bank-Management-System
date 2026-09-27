import json

def load_accounts():
    with open("accounts.json", "r") as file:
        return json.load(file)

def save_accounts(accounts):
    with open("accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)