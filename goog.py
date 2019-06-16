import requests
from bs4 import BeautifulSoup

# Scrape google news site. Look for articles about EOS.
# Google news has a list of articles. Inside the articles, h3 tags have the news title and anchors.

data = requests.get('https://news.google.com/search?q=eos')

# print (data.status_code) # gets the HTML 
# print (data.headers)     # Gets the HTML codes
# print (data.content)     # Gets the data headers and web page (HTML)
# print (data.text)        # Gets the web page (HTML)

soup = BeautifulSoup(data.text, 'html.parser')
articles = soup.find_all("article")

urls=[]
for article in articles:
	h3tags=article.find('h3')
	anchor=h3tags.find("a")
	urls.append("https://news.google.com"+anchor.attrs['href'][1:])  # Remove the leading dot (".") from href.

print (urls)


	# print (anchor.attrs)           # attrs - prints all attributes.
	# print (anchor.attrs['href'])   # attra['href'] - only the 'href' attributes

