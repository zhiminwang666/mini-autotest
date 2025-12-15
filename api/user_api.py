class UserAPI:
    def __init__(self, client):
        self.client = client

    def login(self, username, password):
        data = {"username": username, "password": password}
        return self.client.post("/api/login", json=data)

    def get_profile(self):
        return self.client.get("/api/profile")