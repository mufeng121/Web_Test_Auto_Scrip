from . import attack as a
from .header_config import *
import http.cookiejar as cookielib

class admin_section(a.attack_inter):
    def __init__(self):
        # First trying to load cookies from local cookie file
        self.juice_session = a.requests.session()
        self.juice_session.cookies = cookielib.LWPCookieJar(filename="juiceShopCookies.txt")
        self.routeUrl = "http://localhost:3000/#/administration"

    def generator(self):
        #cookies = COOKIE
        headers = HEADER
        return headers

    def isLoginStatus(self, headers):
        response = self.juice_session.get(self.routeUrl, cookies=self.juice_session.cookies, allow_redirects = False)
        print(self.juice_session.cookies)
        if response.status_code == 200:
            print(response.text)
        else:
            print(response.status_code)
            print("Invalid cookie, please try login or SQL injection")

    def run(self):
        self.juice_session.cookies.load()
        headers = self.generator()
        self.isLoginStatus(headers)
