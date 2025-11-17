from flask import Blueprint, jsonify


main_bp = Blueprint("main", __name__)


@main_bp.get('/')
def home():
    return jsonify(message="Secure Flask App Running")