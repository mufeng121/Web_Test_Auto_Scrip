Installation instruction:
    1. Make sure you are using python3
    2. Required libraries: 
        "request"  if you do not have it installed, try command --> python3 -m pip install Requests
        "pandas"   if you do not have it installed, try command --> python3 -m pip install pandas
    3. (Optional) Using VSCode as your IDE

Preparation instruction:   
    1. According to which web server you use, uncomment line 28 or 29 in attack.py
    2. According to which web server you use, uncomment line 21 or 22 in header_config.py
    3. Recommend give '777' permission to all files.
    4. Make sure you run the application by using root permission.
    5. All payloads dictionaries(Eg: common.txt & SQL_injection_payloads.txt) should be placed inside plugins folder

Excution instruction:
    There are only two executable main entrance:
    1. engine.py : execute this script with flags to perform attacks on Juice-shop web server. 
         NOTES: valid command example
         python3 engine.py
         python3 engine.py -h
         python3 engine.py -s
         python3 engine.py -s -p "jim@juice-sh.op' --" -u jim
         python3 engine.py -s -p ./plugins/SQL_injection_payloads.txt
         python3 engine.py -ad
         python3 engine.py -addUser
         python3 engine.py -xss
         python3 engine.py -addAdminUser
         python3 engine.py -login -role admin
         python3 engine.py -login -role normal
         python3 engine.py -captcha
         python3 engine.py -uploadF
         python3 engine.py -payback -u test195@gmail.com
         python3 engine.py -deFStar
         python3 engine.py -bjLogin
         python3 engine.py -forGe -attacker test195@gmail.com -victim bjoern.kimminich@gmail.com
         python3 engine.py -chrSpe -u test23@gmail.com
         python3 engine.py -temPdt
         python3 engine.py -acsFile 
         python3 engine.py -basket -attacker test23@gmail.com -victim test259@gmail.com
         (For detail about commands' usage, please check the comments in engine.py or plugins)
    2. "/label/Labeling.py" : After you finish attacking and collecting pcap file, execute this script to label all collected traffics with corresponding attack label. 
         python3 Labeling.py
         Note: RIVER edit here

Attack plugin running flow:
    1. (Mandatory) SQL injection into admin account (get admin access) --> command: python3 engine.py -s
    2. (Mandatory) Get some existing users' email addresses from administration page --> command: python3 engine.py -ad
    3. (Mandatory) Create some new users and record their crediential info into user.json --> command: python3 engine.py -login -role normal    or    python3 engine.py -login -role admin
                   (command will only create one user each execution, you need run it at least two times.)
    4. Then, you can use your created fake users or existing users (depend on challenges) to rest of attacks. Execution order for rest of attacks does not matter.  
    5. Create users without recording their credential into user.json --> command: python3 engine.py -addUser   or   python3 engine.py -addAdminUser
    5. SQL injection into other users' account --> command: python3 engine.py -s -p "jim@juice-sh.op' --" -u jim
    5. Using attacker's account to change victim's feedback and reviews --> command: python3 engine.py -forGe -attacker test195@gmail.com -victim bjoern.kimminich@gmail.com
    5. test_get_coupon_class() || You MUST need admin record 
    5. fivestar_delet() || You MUST need admin record
    5. basket() || You MUST need two customer user record
    5. forged() || You MUST need two customer user record
    5. Christmas_Special() || You MUST need one customer record
    5. access_log() || This function needs interaction between the user, user can specify which confidential file they want to access
    5. product_tempering || You MUST need admin record
    ... (there are totally 19 commands you can run.)

Note: after decided which plugin is used, please execute 'engine.py' under "Web_Test_Auto_Scrip" directory (Especially when using IDE like VSCode)
All automatically created json file should be outside of "plugins" folder

Git Push Rule:
    1. Please DO NOT add/commit/push any automatically created json file.
        (uncomment line 188 and comment 189 in the engine.py  and execute it to clean up)