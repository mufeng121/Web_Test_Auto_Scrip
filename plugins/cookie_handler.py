import json
from plugins.header_config import *

def auth_write(user, cookie, header):
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

def auth_writer(user):
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

def auth_load(user):
    try:
        with open('cookies.json', 'r', encoding='utf-8') as f:
            cookies = json.loads(f.read())[user]
        with open('headers.json', 'r', encoding='utf-8') as f:
            headers = json.loads(f.read())[user]
        return cookies, headers
    except:
        return None

def bid_write(user, bid):
    try:
        with open('bids.json', 'r', encoding='utf-8') as fc:
            bids = json.loads(fc.read())

        with open('bids.json', 'w') as fh:
            bids[user] = bid
            fh.write(json.dumps(bids))

    except:
        with open('bids.json', 'w') as fc:
            bids = {user:bid}
            fc.write(json.dumps(bids))


def get_bid(response):
    return response.json()["authentication"]["bid"]

def bid_load(user):
    try:
        with open('bids.json', 'r', encoding='utf-8') as f:
            bid = json.loads(f.read())[user]
        return bid
    except:
        return None