"""
This file will create a login session using user that is not admin
It will then save the cookie to cookies.json
#################################################################3
Remark: You need to register a user before you run this code
Hint: You can use TASK REPETITIVE REGISTRATION
"""

from plugins import attack as a
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class test_user_login_class(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/rest/user/login'
        self.email = 'test81@gmail.com'
        self.password = '123456'

    def change_email(self, new_email):
        self.email = new_email

    def generator(self,):
        json_data = {
            'email': self.email,
            'password': self.password,
        }

        return json_data

    def run(self):
        json_data = self.generator()
        response = self.juice_session.post(self.url, json=json_data)
        print(response.status_code)
        if response.status_code == 401:
            print("The email address is NOT registered. You may need REPETITIVE REGISTRATION TO REGISTER A NEW USER")
        elif response.status_code == 200:
            print(response.request.headers)
            print(response.headers)
            new_token = response.json()["authentication"]['token']
            print(new_token)
            new_header = a.TEST_HEADER
            new_header["Authorization"] = "Bearer "+new_token
            print(new_header)
            new_cookie = a.TEST_COOKIE
            new_cookie["token"] = new_token
            print(new_cookie)
            a.write_cookie(self.email, new_cookie)
            print("1")
            print(new_cookie["token"] == new_token)
            print(a.TEST_COOKIE["token"] == new_token)
            print("2")
            print(a.TEST_COOKIE)
            print(new_cookie)
        return response.status_code, new_cookie, new_header

    def second_login(self, new_cookie, new_header):
        print(a.TEST_COOKIE == new_cookie)
        print(a.TEST_HEADER == new_header)
        print("who am i")
        response = self.juice_session.get(a.URL + '/rest/user/whoami',
                                          cookies=new_cookie, headers=new_header, verify=False)
        print(response.status_code)
        print(response.text)
        print("let's see administration")
        print(new_cookie["token"])
        res = self.juice_session.get(a.URL + '/rest/user/authentication-details',
                                          cookies=new_cookie, headers=new_header, verify=False)
        print(res.text)
        print(res.status_code)