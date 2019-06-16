import requests
from bs4 import BeautifulSoup

data = requests.get('http://rtfm.ca/eos')
soup = BeautifulSoup(data.text, 'html.parser')

# Print out all the anchor tags
for anchor in soup.find_all('a'):
	print (anchor.text, anchor.get('href'))
