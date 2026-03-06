import requests

def search_items(keyword):

    url=f"https://api.bunjang.co.kr/api/1/find_v2.json?q={keyword}&order=date"

    r=requests.get(url)

    data=r.json()

    items=[]

    for item in data["list"]:

        items.append({

            "id":item["pid"],

            "title":item["name"],

            "price":int(item["price"]),

            "image":item["product_image"],

            "link":f"https://m.bunjang.co.kr/products/{item['pid']}"

        })

    return items