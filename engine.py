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
# PROGRAMMER:     Hugh Song
#
# NOTES: valid command example
#     python3 engine.py -s
#     python3 engine.py -s -p "jim@juice-sh.op' --" -u jim
#     python3 engine.py -s -p ./plugins/SQL_injection_payloads.txt
#     python3 engine.py -ad
#     python3 engine.py -adduser
#     python3 engine.py -addAdminUser
#     python3 engine.py -adduser
#     python3 engine.py -login
#     python3 engine.py -captcha
#     python3 engine.py -uploadF
#     python3 engine.py -payback -u test195@gmail.com
#     python3 engine.py -deFStar
#     python3 engine.py -bjLogin
#     python3 engine.py -forGe -attacker test195@gmail.com -victim bjoern.kimminich@gmail.com
#     python3 engine.py -chrSpe -u test23@gmail.com
#     python3 engine.py -acsFile 
#     python3 engine.py -basket -attacker test23@gmail.com -victim test259@gmail.com
#---------------------------------------------------------------------------------
import os, sys
from tkinter import X
import argparse
from plugins import SQL_injection as s
from plugins import xss_search as xss
from plugins import admin_section as ad
from plugins import captcha_bypass as tcb
from plugins import repetitive_registration as rr
from plugins import get_coupon as gc
from plugins import admin_registration as regAdm
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


#-----------------------------------------------------------------------------------------------
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


#-----------------------------------------------------------------------------------------------
#FUNCTION main
#ARGUMENTS: void
#RETURNS: void
#Description: main thread
#NOTES:
#1.read command line arguments
#2.determine using which plugin
#-----------------------------------------------------------------------------------------------
def main():
    #command line argument setting
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--s", help="Login through sql injection -s -p[SQL payload, dictionary name (Optional)] -c[username (optional)]", action="store_true")
    parser.add_argument("-p", "--p", help="associated with flag -s, to provide specific SQL injection payload", action="store")
    parser.add_argument("-u", "--u", help="associated with flag -s, -payback, -chrSpe to provide specific username", action="store")
    parser.add_argument("-ad", "--ad", help="admin setion attack", action="store_true")
    parser.add_argument("-addUser", "--addUser", help="repetitive registration attack", action="store_true")
    parser.add_argument("-addAdminUser", "--addAdminUser", help="repetitive registration attack", action="store_true")
    parser.add_argument("-login", "--login", help="login and collect user credential", action="store_true")
    parser.add_argument("-captcha", "--captcha", help="captcha bypass attack", action="store_true")
    parser.add_argument("-uploadF", "--uploadF", help="upload big pdf file", action="store_true")
    parser.add_argument("-xss", "--xss", help="xss injection", action="store_true")
    parser.add_argument("-coupon", "--coupon", help="BULLY CHATBOT attack (has BUG)", action="store_true")
    parser.add_argument("-payback", "--payback", help="payback time attack", action="store_true")
    parser.add_argument("-deFStar", "--deFStar", help="delete all five star feedbacks", action="store_true")
    parser.add_argument("-bjLogin", "--bjLogin", help="login BJOERN Challenge", action="store_true")
    parser.add_argument("-forGe", "--forGe", help="FORGED FEEDBACK & FORGED REVIEW", action="store_true")
    parser.add_argument("-attacker", "--attacker", help="associated with flag -forGe, to provide attacker's email", action="store")
    parser.add_argument("-victim", "--victim", help="associated with flag -forGe, to provide victim's email", action="store")
    parser.add_argument("-temPdt", "--temPdt", help="PRODUCT TAMPERING", action="store_true")
    parser.add_argument("-acsFile", "--acsFile", help="access sensitive files: easter, package, suspicious", action="store_true")
    parser.add_argument("-chrSpe", "--chrSpe", help="buy Chrismas special item", action="store_true")
    parser.add_argument("-basket", "--basket", help="using attacker's crediential to view victim's basket and add items into it", action="store_true")
    # parser.parse_args(['-h'])
    args = parser.parse_args()
    myAttack = None
    if args.s:
        myAttack = s.SQL_injector()
        if args.p and args.u:
            myAttack.run(args.p, args.u)
        elif args.p:
            myAttack.run(args.p)
        else:
            myAttack.run()
    elif args.ad:
        myAttack = ad.admin_section()
        myAttack.run()
    elif args.login:
        myAttack = ul.login()
        myAttack.run()
    elif args.addUser:
        myAttack = rr.repetitive_registration()
        myAttack.run()
    elif args.addAdminUser:
        myAttack = regAdm.admin_registration()
        myAttack.run()
    elif args.captcha:
        myAttack = tcb.captcha_bypass()
        myAttack.run()
    elif args.uploadF:
        myAttack = uz.upload_size()
        myAttack.run()
    elif args.xss:
        myAttack = xss.xss_search()
        myAttack.run()
    elif args.coupon:
        myAttack = gc.get_coupon()
        myAttack.run()
    elif args.payback and args.u:
        myAttack = pt.paybackTime(args.u)
        myAttack.run()
    elif args.deFStar:
        myAttack = deStar.delete_fiveStar()
        myAttack.run()
    elif args.bjLogin:
        myAttack = bjLogin.login_bjoern()
        myAttack.run()
    elif args.bjLogin:
        myAttack = bjLogin.login_bjoern()
        myAttack.run()
    elif args.forGe and args.attacker and args.victim:
        myAttack = forGe.forged(args.attacker, args.victim)
        myAttack.run()
    elif args.temPdt:
        myAttack = temPdt.temper()
        myAttack.run()
    elif args.acsFile:
        myAttack = acsFile.access_file()
        myAttack.run()
    elif args.chrSpe and args.u:
        myAttack = chrSpe.Chrismas_special(args.u)
        myAttack.run()
    elif args.basket and args.attacker and args.victim:
        myAttack = mb.manipulate_basket(args.attacker, args.victim)
        myAttack.run()
    else:
        parser.parse_args(['-h'])

if __name__ == "__main__":
    clean_up()
    # main()