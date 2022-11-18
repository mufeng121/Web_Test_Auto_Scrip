Preparation:   
    1. According to which web server you use, uncomment line 6 or 7 in attack.py
    2. According to which web server you use, uncomment line 10 or 11 in header_config.py
    3. recommend give '777' permission to all files

Attack plugin running flow:
    1. (Mandatory)SQL injection without any input (get admin access)
    2. (Mandatory) login()  (to create some new test users)
    3. (Optional) other SQL injections
    4. (Optional) admin_registration()
    5. admin_section
    5. test_captcha_bypass()
    5. test_get_coupon_class()
    5. upload_size()

Note: after decided which plugin is used, please execute 'engine.py' under "Web_Test_Auto_Scrip" directory (Especially when using IDE like VSCode)
All automatically created json file should be outside of "plugins" folder

Git Push Rule:
    1. Please DO NOT add/commit/push any automatically created json file.
        (uncomment "clear_up()" in the last line of engine.py to clean up)

