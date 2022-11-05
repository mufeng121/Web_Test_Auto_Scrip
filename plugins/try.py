#test = "mudic.txt"
#test1 = "sdasdaweqwedasd--"
#print(test[-4:])

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from plugins import attack as a

URL = "https://juice-shop.herokuapp.com/rest/user/whoami"

header = {'Host': 'juice-shop.herokuapp.com',
          'Sec-Ch-Ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
          'Accept': 'application/json, text/plain, */*',
          'Sec-Ch-Ua-Mobile': '?0',
          'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MjIsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJ0ZXN0MzU1QGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoidW5kZWZpbmVkIiwicHJvZmlsZUltYWdlIjoiL2Fzc2V0cy9wdWJsaWMvaW1hZ2VzL3VwbG9hZHMvZGVmYXVsdC5zdmciLCJ0b3RwU2VjcmV0IjoiIiwiaXNBY3RpdmUiOnRydWUsImNyZWF0ZWRBdCI6IjIwMjItMTEtMDUgMDE6NDI6NDQuOTMzICswMDowMCIsInVwZGF0ZWRBdCI6IjIwMjItMTEtMDUgMDI6NDU6NDYuOTExICswMDowMCIsImRlbGV0ZWRBdCI6bnVsbH0sImlhdCI6MTY2NzYxNjY4NSwiZXhwIjoxNjY3NjM0Njg1fQ.Dl-8-NTpvpF7Q3rgQpYbu-jqaITl6uAEXFz8Fue47CqEm865hCPJ1Dr3Zm6hNM4xkOHMliUZk_2LygpOC1IpRNGaIoLwyz8_t2R5FYn5pmGE96bbqfc7fDn4dM0WplFZSqY7fy0d7nxgqmIKBVdk_-UoFkRuFKv4YQOa4gKTmj4',          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Safari/537.36',
          'Connection': 'close'}
cookie = {'language': 'en', 'welcomebanner_status': 'dismiss', 'cookieconsent_status': 'dismiss',
          #'continueCode': 'pphytRIns8UqHYurh8tMTmFkf4SBt5i9fnSLHWPu9MtrMTpni1ZfkYSVZHJDuE9hbnt1jcxqC9qSMBU4DTJZCqJspaiQMS7XtVVINMTDnCegs8li9Nf18cwOHJx',
          'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MjIsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJ0ZXN0MzU1QGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoidW5kZWZpbmVkIiwicHJvZmlsZUltYWdlIjoiL2Fzc2V0cy9wdWJsaWMvaW1hZ2VzL3VwbG9hZHMvZGVmYXVsdC5zdmciLCJ0b3RwU2VjcmV0IjoiIiwiaXNBY3RpdmUiOnRydWUsImNyZWF0ZWRBdCI6IjIwMjItMTEtMDUgMDE6NDI6NDQuOTMzICswMDowMCIsInVwZGF0ZWRBdCI6IjIwMjItMTEtMDUgMDI6NDU6NDYuOTExICswMDowMCIsImRlbGV0ZWRBdCI6bnVsbH0sImlhdCI6MTY2NzYxNjY4NSwiZXhwIjoxNjY3NjM0Njg1fQ.Dl-8-NTpvpF7Q3rgQpYbu-jqaITl6uAEXFz8Fue47CqEm865hCPJ1Dr3Zm6hNM4xkOHMliUZk_2LygpOC1IpRNGaIoLwyz8_t2R5FYn5pmGE96bbqfc7fDn4dM0WplFZSqY7fy0d7nxgqmIKBVdk_-UoFkRuFKv4YQOa4gKTmj4'}


response = requests.post(url=a.URL, cookies = cookie, headers= header, verify=False)
print(response)
