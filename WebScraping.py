 
try :
	hand = open('file_Example.txt')
except :
	print('File not found')

for line in hand :
	line = line.rstrip()
	if line.startswith('From') == True :
		print(line)


# parsing some of the html page

import urllib.request , urllib.parse, urllib.error
from bs4 import BeautifulSoup


fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand :
	words = line.decode().rstrip()

