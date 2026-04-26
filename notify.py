from dotenv import load_dotenv
import os
import requests

load_dotenv()
TOPIC = os.getenv("TOPIC")
URL = f"https://ntfy.sh/{TOPIC}"

def notify(message):
    requests.post(
        URL,
        data=message
    )