import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SECRET_KEY_FALLBACKS = [os.getenv("OLD_SECRET_KEY")] # Key rotation


    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"


    MAX_CONTENT_LENGTH = 4 * 1024 * 1024 # 4MB
    MAX_FORM_MEMORY_SIZE = 2 * 1024 * 1024


    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    RATELIMIT_DEFAULT = "10/minute"