from flask import Blueprint, request, jsonify
from utils.jwt_helper import generate_token
from extensions.limiter import limiter


auth_bp = Blueprint("auth", __name__)




@auth_bp.post('/login')
@limiter.limit("5/minute")
def login():
    data = request.json or {}


    username = data.get("username")
    password = data.get("password")


    if username == "admin" and password == "admin123":
        token = generate_token({"user": username})
        return jsonify(token=token)


    return jsonify(error="Invalid credentials"), 401


    