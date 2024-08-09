import logging
import os
from locust import TaskSet, task
from helpers.price_payload import query, variables

# Create logs directory if not exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Setup logging
logging.basicConfig(level=logging.INFO)
success_logger = logging.getLogger('locust_success')
success_handler = logging.FileHandler('logs/locust_success.log')
success_handler.setLevel(logging.INFO)
success_formatter = logging.Formatter('%(asctime)s - %(message)s')
success_handler.setFormatter(success_formatter)
success_logger.addHandler(success_handler)

error_logger = logging.getLogger('locust_errors')
error_handler = logging.FileHandler('logs/locust_errors.log')
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(message)s')
error_handler.setFormatter(error_formatter)
error_logger.addHandler(error_handler)

def get_price_task(l):
    l.client.headers['Authorization'] = f'Bearer {l.user.token_manager.get_token()}'
    payload = {"query": query, "variables": variables}
    with l.client.post("/financial/price", name="Financial Price", json=payload, headers=l.client.headers, catch_response=True) as response:
        response_time = round(response.elapsed.total_seconds(), 3)
        if response.status_code == 200:
            success_logger.info(f"Requisicao realizada com sucesso - Nome: get_price, Tempo de resposta: {response_time}s, Status Code: {response.status_code}")
        else:
            error_logger.error(f"Falha na requisicao - Nome: get_price, Tempo de resposta: {response_time}s, Status Code: {response.status_code}, Payload: {payload}, Response: {response.text}")

class UserBehavior(TaskSet):
    tasks = {
        get_price_task: 1
    }

    def on_start(self):
        self.client.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.user.token_manager.get_token()}'
        }
