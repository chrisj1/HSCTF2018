import requests
from BeautifulSoup import BeautifulSoup

class Bot:
	def __init__(self, id, count):
		self.id = id
		self.count = count

url = "http://206.189.179.133/search/"

querystring = {"q":"spambot"}

cookies = dict(PHPSESSID='8o1lvera5dtse161m49bq1j1b6')

response = requests.request("POST", url, params=querystring, cookies=cookies)

r = response.text
links = []
soup = BeautifulSoup(r)
for link in soup.findAll('a'):
    if link.get('href') is not None and "spambot" in link.get('href'):
    	links.append(link)

results = []
for link in links:
	url2 = "http://206.189.179.133/user/"
	link = link.getText().lower().replace(' ', '').replace('#', '')

	querystring2 = {"user":link}
	response2 = requests.request("POST", url2, params=querystring2, cookies=cookies)
	text = response2.text
	#a class="post_author"
	soupmessages2 = BeautifulSoup(text)
	
	s = soupmessages2.findAll("a")
	bot = Bot(link[-5:], len(s))
	results.append(bot)

results.sort(key=lambda x: x.count)
for res in results:
	print res.id, res.count

