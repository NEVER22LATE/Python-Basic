# Introduction to newtwork


# Transport layer protocal - Socket 

import re
import socket

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect( ('github.com\\NEVER22LATE',80))

# HTTP protocal : retrive webpage 

# Getting data from the server


import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand :
	print(line.decode().strip())
