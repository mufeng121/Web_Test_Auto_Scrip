import json

def write_cookie(user, cookie):
    cookies = None
    try:
        with open('cookies.json', 'r', encoding='utf-8') as f:
            cookies = json.loads(f.read())

        with open('cookies.json', 'w') as f:
            cookies[user] = cookie
            f.write(json.dumps(cookies))
    except:
        with open('cookies.json', 'w') as f:
            cookies = {user:cookie}
            f.write(json.dumps(cookies))

def load_cookie(user):
    try:
        with open('cookies.json', 'r', encoding='utf-8') as f:
            cookies = json.loads(f.read())
        return cookies[user]
    except:
        return None

print(load_cookie('admin'))
#write_cookie('hugh', "hehe")