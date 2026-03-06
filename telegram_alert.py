import requests
import json

with open("config.json","r",encoding="utf-8") as f:
    config=json.load(f)

TOKEN=config["telegram_token"]
CHAT_ID=config["telegram_chat_id"]

def send_message(text):

    url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data={
        "chat_id":CHAT_ID,
        "text":text
    }

    requests.post(url,data=data)