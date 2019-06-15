import requests
from bs4 import BeautifulSoup

data = requests.get('http://rtfm.ca/eos')
soup = BeautifulSoup(data.text, 'html.parser')

# print (soup.find_all('a'))

for anchor in soup.find_all('a'):
	print (anchor.text, anchor.get('href'))



# for tr in tbody.find_all('tr'):
# 	place = tr.find_all('td')[0].text.strip()
# 	username = tr.find_all('td')[1].find_all('a')[1].text.strip()
# 	xp = tr.find_all('td')[3].text.strip()
# 	print(place, username, xp)
