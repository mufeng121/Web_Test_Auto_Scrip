import os, sys
from tkinter import X
from plugins import cookie_handler
from plugins import SQL_injection as s
from plugins import xss_search as xss
from plugins import admin_section as ad
from plugins import captcha_bypass as tcb
# from plugins import test_encoding_website as ew
from plugins import test_repetitive_registration as rr
from plugins import test_get_coupon as gc
from plugins import basket as mb
from plugins import login as ul
from plugins import test_user_generate as usrGen
from plugins import test_admin_registration as regAdm
from plugins import test_forged_feedback_review as forGe
from plugins import upload_size as uz


def main():
    # SQL injection
    # with dictionary
    #print('Enter your dictionary:')
    #x = input()
    #myAttack = s.SQL_injector()

    # with nothing
    # myAttack = s.SQL_injector()

    # with specific user email
    # myAttack = s.SQL_injector()
    # myAttack.run('jim@juice-sh.op\' --', 'jim')

    # with no-exist email
    # myAttack = s.SQL_injector()
    # code = myAttack.run('hugh@juice-sh.op\' --', 'hugh')
    # if code !=200:
    #     print("user not exist")

    # myAttack = xss.xss_search()

    # myAttack = tcb.test_captcha_bypass()

    # myAttack = gc.test_get_coupon_class()

    # myAttack = ad.admin_section()

    #myAttack = mb.manipulate_basket()
    # #myAttack = forGe.forged()


    # myAttack = regAdm.admin_registration()
    # myAttack = ul.login()
    
    # myAttack.password_login()
    # myAttack.credential_login('test327@gmail.com')
    # myAttack.delete_fiveStar()

    # response, new_cookie, new_header = myAttack.run()

    # myAttack.second_login(new_cookie, new_header)

    # newUsr = usrGen.new_user_generate()
    # print(newUsr.generate_email())

    myAttack = uz.upload_size()

    myAttack.run()


if __name__ == "__main__":
    main()