from locust import HttpUser, between
from dotenv import load_dotenv
import os
from helpers.rules import UserBehavior

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class GraphQLUser(HttpUser):
    wait_time = between(1, 5)
    tasks = [UserBehavior]
    host = os.getenv('HOST')
    token_manager = None

    def on_start(self):
        from helpers.token_manager import APITokenManager
        self.token_manager = APITokenManager()
