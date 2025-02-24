from endpoints.base_endpoint import BaseEndpoint

class Auth(BaseEndpoint):
    """Klasa obsługująca autoryzację"""

    def login(self, username="admin", password="password123"):
        payload = {"username": username, "password": password}
        response = self.post("/auth", json=payload)
        return response