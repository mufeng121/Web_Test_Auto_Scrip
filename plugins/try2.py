import json
import requests

from plugins import attack as a
from plugins import header_config as hc

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print(a.TEST_COOKIE == hc.TEST_COOKIE)
print(a.TEST_COOKIE)

new_token = "23479"
new_cookie = {}
new_cookie = a.TEST_COOKIE.copy()
new_cookie["token"] = new_token
#print(new_cookie)
print(a.TEST_COOKIE["token"] == new_token)
print(a.TEST_COOKIE)

from urllib import parse

data = [
    ('ProductId', 2),
    ('BasketId', "6"),
    ('BasketId', "5"),
    ('quantity', 1),
]

data_byte = parse.urlencode(data).encode("utf-8")

url = a.URL + '/api/BasketItems/'
email = 'test257@gmail.com'

cookie, header = a.auth_load("admin")
print(header)