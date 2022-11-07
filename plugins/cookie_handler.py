import json
from .header_config import *

def write_cookie(user, cookie, header):
    cookies = None
    headers = None
    try:
        with open('cookies.json', 'r', encoding='utf-8') as fc:
            cookies = json.loads(fc.read())

        with open('headers.json', 'r', encoding='utf-8') as fh:
            headers = json.loads(fh.read())

        with open('cookies.json', 'w') as fc:
            cookies[user] = cookie
            fc.write(json.dumps(cookies))

        with open('headers.json', 'w') as fh:
            headers[user] = header
            fh.write(json.dumps(headers))  

    except:
        with open('cookies.json', 'w') as fc:
            cookies = {user:cookie}
            fc.write(json.dumps(cookies))

        with open('headers.json', 'w') as fh:
            headers = {user:header}
            fh.write(json.dumps(headers)) 

def load_cookie(user):
    try:
        with open('cookies.json', 'r', encoding='utf-8') as fc:
            cookies = json.loads(fc.read())

        with open('headers.json', 'r', encoding='utf-8') as fh:
            headers = json.loads(fh.read())

        return cookies[user], headers[user]
    except:
        return None, None

def modify_cookie_header(response):
    new_token = response.json()["authentication"]['token']
    new_header = TEST_HEADER
    new_header["Authorization"] = "Bearer "+new_token
    new_cookie = TEST_COOKIE
    new_cookie["token"] = new_token

    return new_cookie, new_header