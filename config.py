import os
from dotenv import load_dotenv


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    BIND_ADDRESS = os.getenv("BIND_ADDRESS", "0.0.0.0")
    PORT = os.getenv("PORT", 8080)

    def __init__(self):
        load_dotenv()
