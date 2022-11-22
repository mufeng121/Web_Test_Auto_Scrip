import json
from plugins.header_config import *

# auth_write --> set_auth
def set_auth(username, response):
    new_token = response.json()["authentication"]['token']
    header = TEST_HEADER
    header["Authorization"] = "Bearer "+new_token
    cookie = TEST_COOKIE
    cookie["token"] = new_token
    user = {}

    try:
        with open('user.json', 'r', encoding='utf-8') as fc:
            user = json.loads(fc.read())

        with open('user.json', 'w') as fc:
            user[username]["cookie"] = cookie
            user[username]["header"] = header
            fc.write(json.dumps(user,indent=4, sort_keys=True))

    except:
        with open('user.json', 'w') as fc:
            user[username] = {"cookie":cookie, "header" : header}
            fc.write(json.dumps(user,indent=4, sort_keys=True))
# auth_load --> get_auth
def get_auth(username):
    user = {}
    try:
        with open('user.json', 'r', encoding='utf-8') as f:
            user = json.loads(f.read())

            cookies = user[username]["cookie"]
            headers = user[username]["header"]
        return cookies, headers
    except:
        print("User is not found in user.json!")
        return None

# bid_write --> set_basket_id
# only can add bid for existing user
def set_basket_id(username, response):
    bid = response.json()["authentication"]["bid"]
    user = {}
    try:
        with open('user.json', 'r', encoding='utf-8') as fc:
            user = json.loads(fc.read())
        with open('user.json', 'w') as fh:
            user[username]["bid"] = bid
            fh.write(json.dumps(user,indent=4, sort_keys=True))
    except:
        with open('user.json', 'w') as fh:
            fh.write(json.dumps(user,indent=4, sort_keys=True))
        print("user no found")

# bid_write --> set_basket_id
# only can add bid for existing user
def get_basket_id(username):
    user = {}
    try:
        with open('user.json', 'r', encoding='utf-8') as f:
            user = json.loads(f.read())
            bid = user[username]["bid"]
        return bid
    except:
        print("Cannot find user or basket Id!")
        return None


# bid_load --> get_bid
def get_userId(username):
    user = {}
    try:
        with open('user.json', 'r', encoding='utf-8') as f:
            user = json.loads(f.read())
            userId = user[username]["userId"]
        return userId
    except:
        print("Cannot find user or user Id!")
        return None

def set_userId(username, response):
    userId = response.json()["user"]["id"]
    user = {}
    try:
        with open('user.json', 'r', encoding='utf-8') as fc:
            user = json.loads(fc.read())
        with open('user.json', 'w') as fh:
            user[username]["userId"] = userId
            fh.write(json.dumps(user,indent=4, sort_keys=True))
    except:
        with open('user.json', 'w') as fh:
            fh.write(json.dumps(user,indent=4, sort_keys=True))
        print("user no found")