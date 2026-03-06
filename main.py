import json
import time

from search import search_items
from filter import check_product
from telegram_alert import send_message
from database import is_new


with open("config.json","r",encoding="utf-8") as f:
    config=json.load(f)

products=config["products"]
interval=config["search_interval"]


print("🔥 번장 매물 사냥봇 시작")


while True:

    print("🔎 매물 검색중...")

    for product in products:

        for keyword in product["required_keywords"]:

            items=search_items(keyword)

            for item in items:

                title=item["title"]
                price=item["price"]

                if not check_product(title,price,product):
                    continue

                if not is_new(item["id"]):
                    continue

                msg=f"""
🔥 매물 발견

{title}

가격: {price}

{item['link']}
"""

                send_message(msg)

                print("✅ 발견:",title)

    print(f"⏱ {interval}초 후 다시 검색")

    time.sleep(interval)