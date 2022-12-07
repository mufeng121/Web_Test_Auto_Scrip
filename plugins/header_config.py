# SOURCE FILE:    header_config.py
# PROGRAM:        JuiceShop automating attack application -- token tamplate
# Description:    Provide very basic Cookie and Header tamplate  
#                  
# DATE:           Dec 6, 2022
# REVISIONS:      N/A
# PROGRAMMER:     Hugh Song
#
# NOTES
#--------------------------------------------------------------------------------------

TEST_COOKIE = {
    'language': 'en',
    'welcomebanner_status': 'dismiss',
    'cookieconsent_status': 'dismiss',
    #'continueCode': 'WaDV1LvjPGkLhxtvUWHWTXSniaZfPJH2luVxSEaUnBhOOIkosJx0rygYlN8n',
    'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MjIsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJ0ZXN0MzU1QGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoidW5kZWZpbmVkIiwicHJvZmlsZUltYWdlIjoiL2Fzc2V0cy9wdWJsaWMvaW1hZ2VzL3VwbG9hZHMvZGVmYXVsdC5zdmciLCJ0b3RwU2VjcmV0IjoiIiwiaXNBY3RpdmUiOnRydWUsImNyZWF0ZWRBdCI6IjIwMjItMTEtMDUgMDE6NDI6NDQuOTMzICswMDowMCIsInVwZGF0ZWRBdCI6IjIwMjItMTEtMDUgMDI6NDU6NDYuOTExICswMDowMCIsImRlbGV0ZWRBdCI6bnVsbH0sImlhdCI6MTY2NzYxOTcxOCwiZXhwIjoxNjY3NjM3NzE4fQ.dShk5yC4Fv8vRW3G8LCQMKOcp1QcaEh8j-c_awG2AY7jVCBQVBu70kIoJjKoozgWV-XHyGGM453h-pVdVZtgbLWn2u5oVHwupkNFdMT296X1joHnL29bFQcUNQY5QpiWrjsf_GC9mWZYuavorrxib1grpD-bkd6n-BEpQ1R-Mz4',
}

TEST_HEADER = {
    'Host': "localhost:3000",
    #'Host': 'juice-shop.herokuapp.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': '',
}

