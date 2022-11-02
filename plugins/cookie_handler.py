import json
import requests

def write_cookie(cookie):
    with open('cookies.json', 'w') as f:
        f.write(json.dumps(cookie))
        return

def load_cookie():
    try:
        with open('cookies.json', 'r', encoding='utf-8') as f:
            cookies = json.loads(f.read())
        return cookies
    except:
        return None