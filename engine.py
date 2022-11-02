import os, sys
from tkinter import X
from plugins import SQL_injection as s
from plugins import xss_search as xss
from plugins import test_encoding_website as ew
from plugins import test_repetitive_registration as rr
from plugins import test_get_coupon as gc

def main():
    # SQL injection
    # print('Enter your dictionary:')
    # x = input()
    # myAttack = s.SQL_injector(x)
    # myAttack.run()

    myAttack = xss.xss_search()
    myAttack.run()
    

    myAttack = gc.test_get_coupon_class()
    myAttack.run()

if __name__ == "__main__":
    main()