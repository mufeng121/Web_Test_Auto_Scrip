"""
This file is used to solve the OWASP Juice-shop Task
PAYBACK TIME
Category: Improper Input Validation
GOAL: set the amount of sth in your basket to be negative
      after this you can checkout and gain money
METHODOLOGY:
step1. login to user A
    Hint: we can use the user created in repetitive registration
step2. Set the quantity of sth in your basket to be -1000000
setp3. Set address and checkout
"""

from plugins import login as usrLogin
from plugins import attack as a
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class paybackTime(a.attack_inter):

    def __init__(self):
        self.juice_session = a.requests.session()
        usr = usrLogin.test_user_login_class()
        response, self.cookie, self.header = usr.run()
        self.userid = usr.id

    #def manage_basekt

    def generator(self):
        pass

    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', encoding='utf-8',
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        logger = a.logging.getLogger("Payback Time")
        a.logging.info(logger)
        a.logging.info('Started')
        self.forged_feedback()
        self.forged_review()
        a.logging.info('Finished')