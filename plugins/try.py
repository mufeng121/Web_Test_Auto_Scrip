import json
def set_auth(username, cookie, header):
    user = {}

    try:
        with open('user.json', 'r', encoding='utf-8') as fc:
            user = json.loads(fc.read())

        if user[username] == None:
            print("no usersssss")
        
        with open('user.json', 'w') as fc:
            user[username]["cookie"] = cookie
            user[username]["header"] = header
            fc.write(json.dumps(user))

    except:
        with open('user.json', 'w') as fc:
            user[username] = {"cookie":cookie, "header" : header}
            fc.write(json.dumps(user))
       

def set_basket_id(username, bid):
    user = None
    try:
        with open('user.json', 'r', encoding='utf-8') as fc:
            user = json.loads(fc.read())
        
        with open('user.json', 'w') as fh:
            user[username]["bid"] = bid
            fh.write(json.dumps(user))

    except:
        # with open('bids.json', 'w') as fc:
        #     bids = {user:bid}
        #     fc.write(json.dumps(bids))
        with open('user.json', 'w') as fh:
            fh.write(json.dumps(user))
        print("user no found")

set_auth("aa","hah","www")
#set_basket_id("Hugh", 12)
#set_basket_id("dd", 12)