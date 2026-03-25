from flask import request, jsonify
from models.user_model import find_user_by_email, create_user


def register():
    data = request.get_json()

    firstname = data.get("firstname")
    lastname = data.get("lastname")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "user")

    if not firstname or not lastname or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    if role not in ["user", "admin", "manager"]:
        return jsonify({"error": "Role must be user, admin, or manager"}), 400

    existing_user = find_user_by_email(email)
    if existing_user:
        return jsonify({"error": "Email already exists"}), 400

    user = create_user(firstname, lastname, email, password, role)

    return jsonify({
        "message": "User registered successfully",
        "user": user
    }), 201


def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = find_user_by_email(email)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if user["password"] != password:
        return jsonify({"error": "Wrong password"}), 401

    return jsonify({
        "message": "Login successful",
        "user": user
    }), 200