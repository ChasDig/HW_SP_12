import json
from typing import List


# 3: Load json-file:
def load_json() -> list[dict]:
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


# 3: Create func: search page by meaning:
def search_page(meaning: str) -> list[dict]:

    result = []
    for buf in load_json():
        if meaning.lower() in buf['content'].lower():
            result.append(buf)

    return result


# 5: Load a new post in json-file:
def add_post(post: dict):

    posts: list[dict] = load_json()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)

    return posts


