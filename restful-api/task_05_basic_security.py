#!/usr/bin/python3
"""
task_05_basic_security.py

Implements Basic Authentication (Flask-HTTPAuth) and JWT authentication
(Flask-JWT-Extended) with role-based access control.

Endpoints:
- GET  /basic-protected : Basic Auth protected
- POST /login           : returns JWT access token
- GET  /jwt-protected   : JWT protected
- GET  /admin-only      : JWT protected + admin role required
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return False
    return check_password_hash(user["password"], password)


@auth.error_handler
def basic_auth_error(status=401):
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Basic auth protected endpoint."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Authenticate user and return a JWT access token.

    Expects JSON:
    {
        "username": "user1",
        "password": "password"
    }
    """
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not password or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    identity = {"username": username, "role": user["role"]}
    access_token = create_access_token(identity=identity)

    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """JWT protected endpoint."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Admin-only endpoint protected by JWT + role check.

    Non-admin -> 403 with {"error": "Admin access required"}
    """
    identity = get_jwt_identity()
    role = identity.get("role") if isinstance(identity, dict) else None

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
