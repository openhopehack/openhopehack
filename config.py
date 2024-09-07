import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "SUPER_SECRET_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    BIND_ADDRESS = os.getenv("BIND_ADDRESS", "0.0.0.0")
    PORT = os.getenv("PORT", 8080)
    GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
    GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
