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

    def generator(self):
        #cookies = COOKIE
        headers = a.HEADER

        json_data = {
            'email': 'testeee@gmail.com' ,
            'password': '123456',
        }

        return headers, json_data

    def run(self):
        headers, json_data = self.generator()
        response = self.juice_session.post(self.url, json=json_data)
        print(response.status_code)
        if response.status_code == 200:
            print(response.text)
            res_payload_dict = response.json()
            print("Valid script: ", json_data['email'])
            new_token = res_payload_dict["authentication"]['token']
            print(response.headers)
            new_cookie = a.COOKIE
            new_cookie["token"] = new_token
            a.write_cookie('newuser', new_cookie)
            print(new_cookie)
            print("end write")
            print(a.load_cookie('newuser'))
