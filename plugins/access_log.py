"""
This file is to automate the OWASP JUICESHOP TASK
EASTER EGG
ACCESS LOG
-------------------------------------------------
METHODOLOGY:
1. scan the subnet to find ftp, using brute force
2.1. find easter.egg in response
2.2.
3.1. scan the subnet using %25xx.md using brute force
"""
import re
from plugins import attack as a
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class access_file():

    def __init__(self):
        self.url = a.URL+ "/ftp" ## you need to write brute force command to obtain this ftp
        self.juice_session = a.requests.session()

    def generator(self):
        pass

    def parse_html(self, str):
        print(str)
        pattern = '<a.*?href="(ftp/easter.+)".*?>(.*?)</a>'
        try:
            href = re.findall(pattern, str)
            print(href[0][0])
            idx = href[0][0].find('"')
            print(idx)
            return href[0][0][:idx]
        except:
            print("{} NOT find, please use other script").format("easter")


    def find_easter_egg(self):
        response = self.juice_session.get(self.url)
        str = response.text
        return self.parse_html(str)

    def run(self):
        suburl = self.find_easter_egg())


