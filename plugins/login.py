"""
This file will create a login session using user
#################################################################
You can choose to generate user using the following three ways:
1. load existing user from json
2. run REPETITIVE_REGISTRATION to register a customer user
3. run ADMIN_REGISTRATION to register a admin user
RE: if you choose to pick user from 2,3. You need to run set_user, set_info
otherwise, you can set self.email = "YOU PICK FROM Json"
#################################################################
"""

from plugins import attack as a
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from plugins import test_repetitive_registration as usrReg
from plugins import test_admin_registration as admReg

class login(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/rest/user/login'
        #self.email = 'test368@gmail.com' #test327@gmail.com'
        self.password = '123456'

    def set_user(self):
        self.usr = usrReg.test_repetitive_registration()  ## this user is a normal user
        #self.usr = admReg.admin_registration()

    def set_info(self):
        self.email, self.password, self.id = self.usr.run()

    def generator(self,):
        json_data = {
            'email': self.email,
            'password': self.password,
        }
        return json_data

    def password_login(self):
        """
        This function is to login using Username and Password
        After successfully login, we will save the user credentials such as
        cookies and headers. Then in the following cases, we can login only using
        cookies and headers.
        """
        print("--------------------------------------")
        print("Now let us login using username " + self.email + " and password " + self.password)
        json_data = self.generator()
        response = self.juice_session.post(self.url, json=json_data)
        print(response.status_code)
        if response.status_code == 200:
            a.set_auth(self.email,response)
            a.set_basket_id(self.email,response)
        print(response.text)
        return response

    def credential_login(self, email):
        print("---------------------------------------------")
        print("Now let us login using cookie and header")
        print("Who am i")
        new_cookie, new_header = a.get_auth(email)
        response = self.juice_session.get(a.URL + '/rest/user/whoami',
                                             cookies=new_cookie, headers=new_header, verify=False)
        print("Now let us load our UserId to json ----")
        a.set_userId(email,response)

    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', encoding='utf-8',
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        logger = a.logging.getLogger("create a login session using user")
        a.logging.info(logger)
        a.logging.info('Started')
        self.set_user()  ## this is need if we do not have records of existing users.
        self.set_info()
        self.password_login()
        self.credential_login(email=self.email)
        a.logging.info('Finished')


