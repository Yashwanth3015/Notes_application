import requests

from utils.config import API_URL, EMAIL, PASSWORD


class APIClient:

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):

        url = f"{API_URL}/users/login"

        payload = {
            "email": EMAIL,
            "password": PASSWORD
        }

        response = requests.post(url, json=payload)

        return response.json()["data"]["token"]

    def get_headers(self):

        return {
            "x-auth-token": self.token
        }

    def get_notes(self):

        return requests.get(
            f"{API_URL}/notes",
            headers=self.get_headers()
        )

    def create_note(self, title, description, category="Work"):

        payload = {
            "title": title,
            "description": description,
            "category": category
        }

        return requests.post(
            f"{API_URL}/notes",
            json=payload,
            headers=self.get_headers()
        )

    def delete_note(self, note_id):

        return requests.delete(
            f"{API_URL}/notes/{note_id}",
            headers=self.get_headers()
        )