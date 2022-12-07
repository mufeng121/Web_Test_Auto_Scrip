# SOURCE FILE:    user_generate.py
# PROGRAM:        JuiceShop automating attack application -- supplementary class
# FUNCTIONS:      Used to randomly generate a new user email which is never registered. 
#                 This class invoked in plogins include repetitive_registration; admin_registration
#          
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Yoyo Wang
#
# NOTES:
#--------------------------------------------------------------------------------------
from plugins import SQL_injection as sqlin
import random
MAX_TEST = 40
MAX_LENGTH = 400

#---------------------------------------------------------------------------------------
#Class: new_user_generate
#Inherit: N/A
#-----------------------------------------------------------------------------------------------
class new_user_generate():

    def __init__(self):
        pass

#-----------------------------------------
#FUNCTION check
#ARGUMENTS: email --> randomly generated new user email address
#RETURNS: boolean --> whether this email is already registered 
#Description: This function is use SQL injection to test whether the input email address is registered or not 
#             
#NOTES:
# return True: User not exits! Email is available for registration
# return False: User exists! You need to generate new User email again
#-----------------------------------------------------------------------------------------------
    def check(self, email):
        """
        This function is used to check whether the email of
        the user is previously registried or not
        return: TRUE if not registried
        """
        test_LoginStatus = sqlin.SQL_injector()
        new_script = email + "\'--"
        response = test_LoginStatus.run(new_script, 'use{}'.format(email))
        if response == 200:
            print("User exists! You need to generate a new User")
            return False
        else:
            print("User not exits! Email is available for registration")
            return True

#-----------------------------------------
#FUNCTION check
#ARGUMENTS: N/A
#RETURNS: email --> a new user email which is never registered
#Description: Randomly generate a email address and ensure it is not previously registried
#             
#NOTES:
# Generated email address pattern: test{dd}@gmail.com   dd are 2 digits random number.
# Eg: test56@gmail.com
#-----------------------------------------------------------------------------------------------
    def generate_email(self):
        """
        This function is used to generate a new user email with some terminology.
        We may use some random function to do this.
        And we will call check function to verify if the email is registried or not
        """
        num = random.randint(0, MAX_LENGTH)
        email = 'test{}@gmail.com'.format(num)
        idx = 0
        while ( idx < MAX_TEST ):
            #print("This is {} time try with email".format(idx) )
            #print(email)
            if self.check(email):
                print("----------------------------")
                print("We generate new user with email")
                print(email)
                return email
            else:
                idx += 1
                num = random.randint(0, MAX_LENGTH)
                email = 'test{}@gmail.com'.format(num)
        print("Sorry, we cannot find new user")
