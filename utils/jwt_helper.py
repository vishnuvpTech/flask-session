import jwt
from datetime import datetime, timedelta
from flask import current_app




def generate_token(payload, expires=60):
    payload['exp'] = datetime.utcnow() + timedelta(minutes=expires)
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm="HS256")