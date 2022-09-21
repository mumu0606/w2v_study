import requests
from bs4 import BeautifulSoup
import re
import json

URL_BASE = "https://pokemon.g-takumi.com/pokemon/"
PICTURE_BOOK_NUM = 151

picture_book = {}
pokeNameList = []

for i in range(1, PICTURE_BOOK_NUM + 1):
    response = requests.get("https://pokemon.g-takumi.com/pokemon/%d/" % i)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")

    # ポケモン名の取得
    name = re.sub('^No.\d{3}', '', soup.select_one("#base").get_text())

    # タイプ名の取得
    type = soup.select_one("#wrap > main > article > div.base > p > span").get_text()
    print(type)

    # 図鑑説明の取得
    comments = soup.select("#wrap > main > article > dl > dd.comment > p")
    combined_comment = ''
    for comment in comments:
        combined_comment += re.sub('^(赤緑|青|ピカチュウ)', '', comment.get_text())
    
    picture_book[name] = {
        "comment": combined_comment,
        "type": type
    }
    pokeNameList.append({
        "value": name,
        "lavel": name
    })

print(picture_book)

with open('picture_book.json', mode='w') as f:
    json.dump(picture_book, f, indent=2, ensure_ascii=False)
