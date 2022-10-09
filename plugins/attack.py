from abc import ABC, abstractmethod
import requests

class attack_inter(ABC):
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def generator(self):
        pass

    @abstractmethod
    def run(self):
        pass
