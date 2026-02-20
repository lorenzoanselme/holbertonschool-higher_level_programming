#!/usr/bin/python3
"""
Flask API application.

This module implements a simple RESTful API that manages users
stored in memory using a dictionary.

Available endpoints:
- GET / : Welcome message
- GET /data : Returns list of usernames
- GET /status : Returns API status
- GET /users/<username> : Returns a specific user
- POST /add_user : Adds a new user
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    """
    Return a welcome message.

    Returns:
        str: Welcome message for the API.
    """
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_data():
    """
    Return the list of usernames.

    Returns:
        Response: JSON list containing all usernames.
    """
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status", methods=["GET"])
def get_status():
    """
    Return API status.

    Returns:
        str: API status message.
    """
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Retrieve a specific user by username.

    Args:
        username (str): The username to retrieve.

    Returns:
        Response: JSON object of the user if found.
        Response: 404 error if user does not exist.
    """
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the API.

    Expected JSON format:
        {
            "username": "string",
            "name": "string",
            "age": int,
            "city": "string"
        }

    Returns:
        Response: 201 with user data if successful.
        Response: 400 if JSON is invalid or username missing.
        Response: 409 if username already exists.
    """
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
