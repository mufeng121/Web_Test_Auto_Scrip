
import base64
a = 'bjoern.kimminich@gmail.com'
temp = a[::-1]
password = base64.b64encode(temp.encode("latin1")).decode("utf8")
print(password)
