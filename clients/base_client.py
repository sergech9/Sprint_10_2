import requests
from config import BASE_URL, VERIFY_SSL


class BaseClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Connection": "close"})

    def url(self, path):
        return f"{BASE_URL}{path}"

    def post(self, path, **kwargs):
        return self.session.post(self.url(path), verify=VERIFY_SSL, **kwargs)

    def patch(self, path, **kwargs):
        return self.session.patch(self.url(path), verify=VERIFY_SSL, **kwargs)

    def delete(self, path, **kwargs):
        return self.session.delete(self.url(path), verify=VERIFY_SSL, **kwargs)
