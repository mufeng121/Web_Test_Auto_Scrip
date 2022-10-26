from abc import ABC, abstractmethod
import requests

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
