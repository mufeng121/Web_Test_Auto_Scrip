from plugins import attack as a
from plugins import header_config as hc

print(a.TEST_COOKIE == hc.TEST_COOKIE)
print(a.TEST_COOKIE)

new_token = "23479"
new_cookie = {}
new_cookie = a.TEST_COOKIE.copy()
new_cookie["token"] = new_token
#print(new_cookie)
print(a.TEST_COOKIE["token"] == new_token)
print(a.TEST_COOKIE)