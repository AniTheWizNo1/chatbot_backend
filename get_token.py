import firebase_admin
from firebase_admin import auth, credentials
import requests

email = "aniket10das@gmail.com"
password = "AniTheWizN@1"

API_KEY = "AIzaSyDNZNxqYaycYkN7R2j5-LZZPnLhRmKlsx4"  # Go to Firebase > Project Settings > General > Web API Key

# Step 1: Sign in the user
url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
payload = {
    "email": email,
    "password": password,
    "returnSecureToken": True
}

res = requests.post(url, json=payload)
data = res.json()

if "idToken" in data:
    print("\n✅ Firebase ID Token:\n")
    print(data["idToken"])
else:
    print("\n❌ Error:", data)
