
import urllib.request, urllib.parse, urllib.error
import re

url = "https://en.wikipedia.org/wiki/"
topic = input();
wikiurl = url+ topic 
try :
	fhand = urllib.request.urlopen(wikiurl)
except :
	print("url not found")

#for line in fhand :
#	print(line.decode().strip())
lineno = 0
for line in fhand :
	lineno+= 1
	print(lineno, re.findall('Math',line.decode()))
