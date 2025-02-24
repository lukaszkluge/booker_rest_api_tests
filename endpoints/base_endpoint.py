import requests
from common.config import BASE_URL

class BaseEndpoint:
    """Bazowa klasa dla wszystkich endpointów"""

    def __init__(self):
        self.session = requests.Session()
        self.base_url = BASE_URL

    def get(self, endpoint, headers=None, params=None):
        return self.session.get(f"{self.base_url}{endpoint}", headers=headers, params=params)

    def post(self, endpoint, json=None, headers=None):
        return self.session.post(f"{self.base_url}{endpoint}", json=json, headers=headers)

    def put(self, endpoint, json=None, headers=None):
        return self.session.put(f"{self.base_url}{endpoint}", json=json, headers=headers)

    def delete(self, endpoint, headers=None):
        return self.session.delete(f"{self.base_url}{endpoint}", headers=headers)