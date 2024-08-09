import time
import requests
from dotenv import load_dotenv
import os
import threading

# Load environment variables from .env file
load_dotenv()

class APITokenManager:
    def __init__(self):
        self.token = None
        self.token_expiration_time = None
        self.token_url = os.getenv('TOKEN_URL')
        self.token_headers = {
            'client_id': os.getenv('CLIENT_ID'),
            'client_secret': os.getenv('CLIENT_SECRET'),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': os.getenv('COOKIE')
        }
        self.token_data = {
            'client_id': os.getenv('API_CLIENT_ID'),
            'grant_type': 'client_credentials',
            'client_secret': os.getenv('API_CLIENT_SECRET'),
            'scope': os.getenv('API_SCOPE')
        }
        self.lock = threading.Lock()
        self.refresh_token()

    def refresh_token(self):
        with self.lock:
            response = requests.post(self.token_url, headers=self.token_headers, data=self.token_data)
            response_data = response.json()
            self.token = response_data['access_token']
            self.token_expiration_time = time.time() + 280  # Refresh 20 seconds before expiry
        threading.Timer(270, self.refresh_token).start()  # Refresh every 270 seconds

    def get_token(self):
        with self.lock:
            return self.token
