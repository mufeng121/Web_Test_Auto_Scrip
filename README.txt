Preparation:   
    1. According to which web server you use, uncomment line 28 or 29 in attack.py
    2. According to which web server you use, uncomment line 21 or 22 in header_config.py
    3. recommend give '777' permission to all files

Attack plugin running flow:
    1. (Mandatory) SQL injection without any input (get admin access)
    1.1 (Optional) admin_registration(), repetitive_registration() || registration is needed if we do not have record of existing cookie, header)
    2. (Mandatory) login()  || login using password and return cookie, header || Find self.email from bids.json file, if no records, goto 1.1
    3. (Optional) other SQL injections
    5. admin_section
    5. test_captcha_bypass()
    5. test_get_coupon_class() || You MUST need admin record
    5. upload_size()
    5. fivestar_delet() || You MUST need admin record
    5. basket() || You MUST need two customer user record
    5. forged() || You MUST need two customer user record
    5. Christmas_Special() || You MUST need one customer record
    5. access_log()



Note: after decided which plugin is used, please execute 'engine.py' under "Web_Test_Auto_Scrip" directory (Especially when using IDE like VSCode)
All automatically created json file should be outside of "plugins" folder

Git Push Rule:
    1. Please DO NOT add/commit/push any automatically created json file.
        (uncomment "clear_up()" in the last line of engine.py to clean up)


Log Tested:
    admin sql injection
    perticular user sql injection
    dictionary sql injection
    admin admin_section
    user login
    repetitive_registration
    basket
    