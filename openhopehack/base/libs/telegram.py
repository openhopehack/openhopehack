import requests
import logging


class Telegram:
    def __init__(self, token: str, logger: logging.Logger):
        self.token = token
        self.logger = logger
        self.telegram_api_url = f"https://api.telegram.org/bot{self.token}/sendMessage"

    def send_message(self, chat_id: int, text: str) -> bool:
        payload = {"chat_id": chat_id, "text": text}
        try:
            response = requests.post(self.telegram_api_url, json=payload)
            response.raise_for_status()
            self.logger.info(f"Message sent to Telegram: {response.text}")
            return True
        except requests.RequestException as e:
            self.logger.error(f"Error sending message to Telegram: {e}")
            return False
