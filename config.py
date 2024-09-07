import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    BIND_ADDRESS = os.getenv("BIND_ADDRESS", "0.0.0.0")
    PORT = os.getenv("PORT", 8080)
