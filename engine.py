import os, sys
from tkinter import X
from plugins import SQL_injection as s
from plugins import xss_search as xss
from plugins import admin_section as ad
from plugins import captcha_bypass as tcb
# from plugins import test_encoding_website as ew
from plugins import test_repetitive_registration as rr
from plugins import test_get_coupon as gc

#from plugins import test_user_generate as usrGen
#from plugins import test_admin_registration as regAdm
#from plugins import test_forged_feedback_review as forGe
from plugins import login as ul
from plugins import basket as mb
from plugins import fivestar_delete as deStar
from plugins import upload_size as uz
from plugins import forged as forGe
from plugins import login_bjoern as bjLogin
from plugins import Product_Tampering as temPdt
from plugins import Christmas_Special as chrSpe



def clean_up():
    try:
        os.system("rm user.json")
    except:
        print("file already deleted!")


def main():
    # SQL injection
    # with dictionary
    #print('Enter your dictionary:')
    #x = input()
    #myAttack = s.SQL_injector()

    #with nothing
    myAttack = s.SQL_injector()
    myAttack.run()

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

    #myAttack = ad.admin_section()
    #response = myAttack.run()
    #print(response)

    myAttack = ul.login()
    myAttack.run()
    #myAttack = ul.login()
    #myAttack.run()
    #myAttack.credential_login()

    #myAttack = deStar.delete_fiveStar()
    #myAttack = mb.manipulate_basket()
    #myAttack.run()
    #myAttack = forGe.forged()
    #myAttack.run()
    #myAttack = bjLogin.login_bjoern()
    #myAttack.run()
    #myAttack = temPdt.temper()
    #myAttack.run()
    myAttack = chrSpe.Chrismas_special()
    myAttack.run()

    #myAttack = uz.upload_size()

    


if __name__ == "__main__":
    # main()
    clean_up()
    main()