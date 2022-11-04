"""
This file will create a login session using user that is not admin
It will then save the cookie to cookies.json
TEST CASE: user: testeee@gmail.com Pass:123456
"""

from plugins import attack as a
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class test_user_login_class(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/rest/user/login'
        self.email = 'test121@gmail.com'
        self.password = '123456'

    def change_email(self, new_email):
        self.email = new_email

    def generator(self,):
        json_data = {
            'email': self.email ,
            'password': self.password,
        }

        return json_data

    def run(self):
        json_data = self.generator()
        response = self.juice_session.post(self.url, json=json_data)
        print(response.status_code)
        if response.status_code == 200:
            print(response.headers)
        return response.status_code