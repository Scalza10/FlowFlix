from flask import request, jsonify
from models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash


def register_user():
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]

    # Check if user already exists
    user = User.query.filter_by(Username=username).first()
    if user:
        return jsonify({"message": "User already exists!"}), 400

    # Create new user
    new_user = User(username, email, password)
    db.session.add(new_user)
    db.session.commit()

    # Create JWT token
    access_token = create_access_token(
        identity={"username": new_user.Username, "email": new_user.Email}
    )
    return (
        jsonify(
            {
                "message": "Registration successful! Redirecting shortly...",
                "access_token": access_token,
            }
        ),
        200,
    )


def login_user():
    username = request.json["username"]
    password = request.json["password"]

    # Check if user exists
    user = User.query.filter_by(Username=username).first()
    if user is None:
        return jsonify({"message": "User does not exist!"}), 400

    # Check if password is correct
    if not check_password_hash(user.PasswordHash, password):
        return jsonify({"message": "Invalid password!"}), 400

    # Create JWT token
    access_token = create_access_token(
        identity={"username": user.Username, "email": user.Email}
    )
    return jsonify({"message": "Login successful!", "access_token": access_token}), 200


@jwt_required()
def protected_route():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
