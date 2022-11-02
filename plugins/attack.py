from abc import ABC, abstractmethod
import requests
from .header_config import *
import http.cookiejar as cookielib
from .cookie_handler import *

class attack_inter(ABC):

    @abstractmethod
    def generator(self):
        pass

    @abstractmethod
    def generator(self,myScript):
        pass

    @abstractmethod
    def run(self):
        pass
