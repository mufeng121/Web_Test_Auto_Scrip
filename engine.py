import os, sys
from tkinter import X
from plugins import SQL_injection as s
from plugins import xss_search as xss
from plugins import xss_search as xss

def main():
    # SQL injection
    # print('Enter your dictionary:')
    # x = input()
    # myAttack = s.SQL_injector(x)
    # myAttack.run()

    myAttack = xss.xss_search()
    myAttack.run()
    

if __name__ == "__main__":
    main()