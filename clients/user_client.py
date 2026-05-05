from clients.base_client import BaseClient
from config import LOGIN_PATH, REGISTER_PATH


class UserClient(BaseClient):
    def register_user(self, payload):
        return self.post(REGISTER_PATH, json=payload)

    def login_user(self, email, password):
        return self.post(LOGIN_PATH, json={"email": email, "password": password})

