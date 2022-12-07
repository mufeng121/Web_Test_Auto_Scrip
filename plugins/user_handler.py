# SOURCE FILE:    user_handler.py
# PROGRAM:        JuiceShop automating attack application -- Handler
# FUNCTIONS:      Setter and Getter of user data from user.json
# USER DATA:      auth (cookie, header)     
#                 user id
#                 user's basket id
#                 user's password
#                 user's shipping address id
#
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Hugh Song
#
# NOTES
#--------------------------------------------------------------------------------------
import json
from plugins.header_config import *

#-----------------------------------------
#FUNCTION set_auth
#ARGUMENTS: username --> username/email
#           response --> response for POST request
#RETURNS: N/A
#Description: 1. extract authentication token from response
#             2. insert authentication token into header and cookie
#             3. rewrite user's header and cookie in user.json
#     
#NOTES:
#-----------------------------------------------------------------------------------------------
def set_auth(username, response):
    new_token = response.json()["authentication"]['token']
    header = TEST_HEADER
    header["Authorization"] = "Bearer "+new_token
    cookie = TEST_COOKIE
    cookie["token"] = new_token
    user = {}

    try:
        with open('user.json', 'r', encoding='utf-8') as fc:
            user = json.loads(fc.read())

        with open('user.json', 'w') as fc:
            user[username]["cookie"] = cookie
            user[username]["header"] = header
            fc.write(json.dumps(user,indent=4, sort_keys=True))

    except:
        with open('user.json', 'w') as fc:
            user[username] = {"cookie":cookie, "header" : header}
            fc.write(json.dumps(user,indent=4, sort_keys=True))

#-----------------------------------------
#FUNCTION get_auth
#ARGUMENTS: username --> username/email
#           
#RETURNS: N/A
#Description: get user's cookie and header from user.json
#     
#NOTES:
#-----------------------------------------------------------------------------------------------
def get_auth(username):
    user = {}
    try:
        with open('user.json', 'r', encoding='utf-8') as f:
            user = json.loads(f.read())
            cookies = user[username]["cookie"]
            headers = user[username]["header"]
        return cookies, headers
    except:
        print("User is not found in user.json!")
        return None

#-----------------------------------------
#FUNCTION set_basket_id
#ARGUMENTS: username --> username/email
#           response --> response for POST request
#RETURNS: N/A
#Description: 1. extract user's basket id from respond 
#             2. insert user's basket id in user.json
#     
#NOTES:
# only can add bid for existing user
#-----------------------------------------------------------------------------------------------
def set_basket_id(username, response):
    bid = response.json()["authentication"]["bid"]
    user = {}
    try:
        with open('user.json', 'r', encoding='utf-8') as fc:
            user = json.loads(fc.read())
        with open('user.json', 'w') as fh:
            user[username]["bid"] = bid
            fh.write(json.dumps(user,indent=4, sort_keys=True))
    except:
        with open('user.json', 'w') as fh:
            fh.write(json.dumps(user,indent=4, sort_keys=True))
        print("user no found")

#-----------------------------------------
#FUNCTION get_basket_id
#ARGUMENTS: username --> username/email
#           
#RETURNS: N/A
#Description: get user's basket id from user.json
#     
#NOTES:
#-----------------------------------------------------------------------------------------------
def get_basket_id(username):
    user = {}
    try:
        with open('user.json', 'r', encoding='utf-8') as f:
            user = json.loads(f.read())
            bid = user[username]["bid"]
        return bid
    except:
        print("Cannot find user or basket Id!")
        return None

#-----------------------------------------
#FUNCTION get_userId
#ARGUMENTS: username --> username/email
#           
#RETURNS: N/A
#Description: get user id from user.json
#     
#NOTES:
#-----------------------------------------------------------------------------------------------
def get_userId(username):
    user = {}
    try:
        with open('user.json', 'r', encoding='utf-8') as f:
            user = json.loads(f.read())
            userId = user[username]["userId"]
        return userId
    except:
        print("Cannot find user or user Id!")
        return None

#-----------------------------------------
#FUNCTION set_userId
#ARGUMENTS: username --> username/email
#           response --> response for POST request
#RETURNS: N/A
#Description: 1. extract user id from respond 
#             2. insert user id in user.json
#     
#NOTES:
#-----------------------------------------------------------------------------------------------
def set_userId(username, response):
    userId = response.json()["user"]["id"]
    user = {}
    try:
        with open('user.json', 'r', encoding='utf-8') as fc:
            user = json.loads(fc.read())
        with open('user.json', 'w') as fh:
            user[username]["userId"] = userId
            fh.write(json.dumps(user,indent=4, sort_keys=True))
    except:
        with open('user.json', 'w') as fh:
            fh.write(json.dumps(user,indent=4, sort_keys=True))
        print("user no found")

#-----------------------------------------
#FUNCTION: set_password
#ARGUMENTS: username --> username/email
#           response --> response for POST request
#           password --> user password
#RETURNS: N/A
#Description:  insert user password in user.json
#     
#NOTES:
#-----------------------------------------------------------------------------------------------
def set_password(username, response, password):
    try:
        with open('user.json', 'r', encoding='utf-8') as fc:
            user = json.loads(fc.read())
        with open('user.json', 'w') as fh:
            user[username]["password"] = password
            fh.write(json.dumps(user, indent=4, sort_keys=True))
    except:
        with open('user.json', 'w') as fh:
            fh.write(json.dumps(user,indent=4, sort_keys=True))
        print("user no found")

#-----------------------------------------
#FUNCTION get_userAddressId
#ARGUMENTS: username --> username/email
#           
#RETURNS: N/A
#Description: get user's shipping address id from user.json
#     
#NOTES:
#-----------------------------------------------------------------------------------------------
def get_userAddressId(username):
    user = {}
    try:
        with open('user.json', 'r', encoding='utf-8') as f:
            user = json.loads(f.read())
            addressId = user[username]["userAddressId"]
        return addressId
    except:
        print("Cannot find user or user Id!")
        return None

#-----------------------------------------
#FUNCTION set_userAddressId
#ARGUMENTS: username --> username/email
#           id --> user's shipping address id
#RETURNS: N/A
#Description: 1. insert user's basket id in user.json
#     
#NOTES:
# only can add bid for existing user
#-----------------------------------------------------------------------------------------------
def set_userAddressId(username, id):
    user = {}
    try:
        with open('user.json', 'r', encoding='utf-8') as fc:
            user = json.loads(fc.read())
        with open('user.json', 'w') as fh:
            user[username]["userAddressId"] = id
            fh.write(json.dumps(user,indent=4, sort_keys=True))
    except:
        with open('user.json', 'w') as fh:
            fh.write(json.dumps(user,indent=4, sort_keys=True))
        print("user no found")