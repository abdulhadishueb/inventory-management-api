import json
import os

FILE = "users.json"


def load_users():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)


def find_user_by_email(email):
    users = load_users()

    for user in users:
        if user["email"] == email:
            return user

    return None


def create_user(firstname, lastname, email, password, role):
    users = load_users()

    new_user = {
        "id": len(users) + 1,
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "password": password,
        "role": role
    }

    users.append(new_user)
    save_users(users)

    return new_user