# SOURCE FILE:    engine.py
# PROGRAM:        JuiceShop automating attack application
# FUNCTIONS:      application's main entrance.
#                 Flag system: user need to use flag in terminal to invoke corresponding plugin
#                 Clean up function: clean all pycache and json file
#
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# DESIGNER:       Hugh Song, Yoyo Wang, River Chen
#
# PROGRAMMER:     Hugh Song, Yoyo Wang
#
# NOTES
# encode mode -c [cover image name] -s [secret image name] -st [name for new image]
# decode mode -st [steganographed image]
# eg: python3 -encode -c c1.png -s s1.png -st r1.png 
#     python3 -decode -st r1.png
#---------------------------------------------------------------------------------
import os, sys
from tkinter import X
from plugins import SQL_injection as s
from plugins import xss_search as xss
from plugins import admin_section as ad
from plugins import captcha_bypass as tcb
# from plugins import test_encoding_website as ew
from plugins import repetitive_registration as rr
from plugins import get_coupon as gc

#from plugins import test_user_generate as usrGen
#from plugins import admin_registration as regAdm
#from plugins import forged_feedback_review as forGe
from plugins import paybackTime as pt
from plugins import login as ul
from plugins import basket as mb
from plugins import fivestar_delete as deStar
from plugins import upload_size as uz
from plugins import forged as forGe
from plugins import login_bjoern as bjLogin
from plugins import Product_Tampering as temPdt
from plugins import Christmas_Special as chrSpe
from plugins import access_log as acsFile


#-----------------------------------------
#FUNCTION clean_up
#ARGUMENTS: N/A
#RETURNS: void
#Description: clean all pycache and json file.
#          
#NOTES:
# Developer need to run this function every time before push to Git repo. 
#-----------------------------------------------------------------------------------------------
def clean_up():
    try:
        os.system("rm user.json")
        os.system("rm -r ./plugins/__pycache__")
    except:
        print("file already deleted!")


#-----------------------------------------
#FUNCTION main
#ARGUMENTS: void
#RETURNS: void
#Description: main thread
#NOTES:
#1.read command line arguments
#2.determine using which plugin
#-----------------------------------------------------------------------------------------------
def main():
    # SQL injection
    # with dictionary
    # print('Enter your dictionary:')
    # x = input()
    # myAttack = s.SQL_injector()

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

    #myAttack = xss.xss_search()

    # myAttack = tcb.test_captcha_bypass()

    #myAttack = ul.login()
    #myAttack.run()
    #myAttack = ul.login()
    #myAttack.run()

    #myAttack = gc.get_coupon()
    #myAttack.run()

    #myAttack = ad.admin_section()
    #response = myAttack.run()
    #print(response)

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
    #myAttack = chrSpe.Chrismas_special()
    #myAttack.run()
    myAttack = acsFile.access_file()
    myAttack.run()

    # myAttack = uz.upload_size()
    #myAttack = pt.paybackTime()
    #myAttack.run()

    


if __name__ == "__main__":
    # main()
    clean_up()
    # main()