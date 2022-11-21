Preparation:   
    1. According to which web server you use, uncomment line 6 or 7 in attack.py
    2. According to which web server you use, uncomment line 10 or 11 in attack.py
    3. recommend give '777' permission to all files

Attack plugin running flow:
    1. (Mandatory) SQL injection without any input (get admin access)
    1.1 (Optional) admin_registration(), repetitive_registration() || registration is needed if we do not have record of existing cookie, header)
    2. (Mandatory) login()  || login using password and return cookie, header || Find self.email from bids.json file, if no records, goto 1.1
    3. (Optional) other SQL injections
    5. admin_section
    5. test_captcha_bypass()
    5. test_get_coupon_class()
    5. upload_size()

Note: after decided which plugin is used, please execute 'engine.py' under "Web_Test_Auto_Scrip" directory (Especially when using IDE like VSCode)
All automatically created json file should be outside of "plugins" folder

Git Push Rule:
    1. Please DO NOT add/commit/push any automatically created json file.

