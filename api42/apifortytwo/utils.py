# utils.py
import requests
from django.conf import settings  

def post42(url, payload):
    url = "https://api.intra.42.fr" + url
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, headers=headers, data=payload)
    return response.json()


def get42(url, payload):
    url = "https://api.intra.42.fr" + url
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.get(url, headers=headers, params=payload)

    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return None
    else:
        print(f"Error: {response.status_code}, Content: {response.content}")
        return None
    

def fetch_campus_users():
    wtoken = post42("/oauth/token", {
        "grant_type": "client_credentials",
        "client_id": settings.UID,
        "client_secret": settings.SECRET
    })

    if not wtoken or "access_token" not in wtoken:
        return []

    campus_users = []
    page = 1

    # Dosyayı döngü dışında aç
    while True:
        users_url = f"/v2/campus/49/users?page[number]={page}&page[size]=100"
        page_users = get42(users_url, {"access_token": wtoken["access_token"]})

        if not page_users:
            break
        campus_users.extend(page_users)
        page += 1
    return campus_users