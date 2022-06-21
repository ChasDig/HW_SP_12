import json
from typing import List


# 3: Load json-file:
def load_picture() -> list[dict]:
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


# 3: Create func: search page by meaning:
def search_page(meaning: str) -> list[dict]:

    result = []
    for buf in load_picture():
        if meaning.lower() in buf['content'].lower():
            result.append(buf)

    return result


