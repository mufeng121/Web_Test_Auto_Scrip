# SOURCE FILE:    user_generate.py
# PROGRAM:        JuiceShop automating attack application -- supplementary class
# FUNCTIONS:      Collect existing user's authentication (cookie & header) which could used to bypass authentication
#                 You can choose to generate user using the following three ways:
#                    1. load existing user from json
#                    2. run REPETITIVE_REGISTRATION to register a customer user
#                    3. run ADMIN_REGISTRATION to register a admin user
#          
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Yoyo Wang
#
# NOTES:
# if you choose to pick a user from 2,3. You need to run set_user
# otherwise, you can set self.email = "YOU PICK FROM Json"
#--------------------------------------------------------------------------------------

import time
from plugins import attack as a
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from plugins import repetitive_registration as usrReg
from plugins import admin_registration as admReg

#---------------------------------------------------------------------------------------
#Class: login
#Inherit: Attack
#----------------------------------------------------------------------------------------
class login(a.attack_inter):

#-----------------------------------------
#FUNCTION: __init__ 
#ARGUMENTS: N/A
#RETURNS: void
#Description: Initial class variables
#-----------------------------------------------------------------------------------------------
    def __init__(self):
        # REST session
        self.juice_session = a.requests.session()
        # url to registrate a new user
        self.url = a.URL + '/rest/user/login'
        # moke user password
        self.password = '123456'

#-----------------------------------------
#FUNCTION set_user
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: create and register a new user
#             
#NOTES:
#-----------------------------------------------------------------------------------------------
    def set_user(self):
        self.usr = usrReg.repetitive_registration()  ## this user is a normal user
        #self.usr = admReg.admin_registration()  ## this user is an admin
        self.email, self.password, self.id = self.usr.run()

#-----------------------------------------
#FUNCTION generator
#ARGUMENTS: N/A
#RETURNS: json_data  --> will be embedded into POST request json field. 
#Description: This function is used to generate needed data from REST requests
#             
#NOTES:
#-----------------------------------------------------------------------------------------------
    def generator(self,):
        json_data = {
            'email': self.email,
            'password': self.password,
        }
        return json_data

#-----------------------------------------
#FUNCTION password_login
#ARGUMENTS: N/A
#RETURNS: response  --> response for POST request. 
#Description: This function is to login using Username and Password
#             After successfully login, we will save the user credentials (cookies & header)
#             Then, in the following cases, we can bypass authentication using cookies and headers.
#             
#NOTES:
#-----------------------------------------------------------------------------------------------
    def password_login(self):
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

#-----------------------------------------
#FUNCTION credential_login
#ARGUMENTS: email --> existing user's email
#RETURNS: N/A
#Description: bypass authentication using cookies and headers.
#             
#NOTES:
#-----------------------------------------------------------------------------------------------
    def credential_login(self, email):
        print("---------------------------------------------")
        print("Now let us login using cookie and header")
        print("Who am i")
        new_cookie, new_header = a.get_auth(email)
        response = self.juice_session.get(a.URL + '/rest/user/whoami',
                                             cookies=new_cookie, headers=new_header, verify=False)
        print("Now let us load our UserId to json ----")
        a.set_userId(email,response)

#-----------------------------------------------------------------------
#FUNCTION run
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: This is the main function.
#             1. (optional) create a new user
#             2. user login by using password 
#             3. collect credentials (cookies & header) after login
#             4. bypass login by using credentials
#             
#NOTES: None
#-----------------------------------------------------------------------------------------------
    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log',
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        logger = a.logging.getLogger("create a login session using user")
        a.logging.info(logger)
        a.logging.info('Started')
        self.set_user()  ## this is need if we do not have records of existing users.
        self.password_login()
        self.credential_login(email=self.email)
        a.logging.info('Finished')


