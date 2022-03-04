import json
import requests

sign_in_url = "http://localhost:9099/identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=fake-key"

def sign_in_test_user():
    response = requests.post(sign_in_url, json={ "email": "test@vibe.com", "password": "password123"})

    return response.json()