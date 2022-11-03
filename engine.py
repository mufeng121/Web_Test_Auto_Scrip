import os, sys
from tkinter import X
from plugins import SQL_injection as s
from plugins import xss_search as xss
from plugins import admin_section as ad
# from plugins import test_encoding_website as ew
from plugins import test_repetitive_registration as rr
from plugins import test_get_coupon as gc
from plugins import test_view_basket as vb
from plugins import test_user_login as ul

def main():
    #SQL injection
    #print('Enter your dictionary:')
    #x = input()
    #myAttack = s.SQL_injector(x)

    #myAttack = xss.xss_search()
    
    #myAttack = gc.test_get_coupon_class()

    #myAttack = ad.admin_section()

    myAttack = rr.test_repetitive_registration()

    #myAttack = vb.test_view_basket_class()

    #myAttack = ul.test_user_login_class()
    #response = myAttack.run()

    myAttack.run()

if __name__ == "__main__":
    main()