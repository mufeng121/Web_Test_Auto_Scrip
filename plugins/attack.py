# SOURCE FILE:    attack.py
# PROGRAM:        JuiceShop automating attack application -- Interface
# FUNCTIONS:      The interface for all attack plugine to inherit. 
#                 Import all required Python libraries. 
#                 Initial basic abstract functions
#          
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Hugh Song
#
# NOTES
#--------------------------------------------------------------------------------------
from abc import ABC, abstractmethod
import requests
import logging
from .header_config import *
import http.cookiejar as cookielib

from .user_handler import *

#--------------------------------------------------------------------------------------
#Global Variables: URL
#Notes: There are two options for using Juiceshop server
#       Option 1: using nodejs to host Juiceshop server on your local machine; uncomment first URL.
#       Option 2: using online public server; uncomment second URL
#       Option 2 is unstable, Option 1 need some installation on your local machine. 
#--------------------------------------------------------------------------------------
URL = "http://localhost:3000"
#URL = "https://juice-shop.herokuapp.com"

class attack_inter(ABC):
    # Used to generate all REST requests needed data like json, header, and cookie
    @abstractmethod
    def generator(self):
        pass
    
    # Polymorphic of generator function. Taking one argument
    @abstractmethod
    def generator(self,myScript):
        pass
    
    # This is the main function for plugin to send REST requests.
    @abstractmethod
    def run(self):
        pass

