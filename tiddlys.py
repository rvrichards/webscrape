import requests
from bs4 import BeautifulSoup

#There are many "rtfm.tiddlyspot.com/" files: java, ruby, linux, go, python, eos, ...
# file="misc"
file="eos"
filename=file+".txt"
data = requests.get('http://'+file+'.rtfm.tiddlyspot.com/')
f= open(filename,"w+")
soup = BeautifulSoup(data.text, 'html.parser')


# Find only the code that I have added. aka Tiddlers
# This means all div tags that have a changecount attribute.
inputTag = soup.find_all(attrs={"changecount" : True })

for tag in inputTag:
	f.write ("title=> %s \n" % tag['title'])
	f.write ("tag===> %s \n \n" % tag)

f.close()

print ("Results written to file: %s \n" % filename)
