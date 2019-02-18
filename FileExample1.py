

# Reading file example

try :
	fhandle = open('file_Example.txt','r')
except : 
	print("file not find")	

for line in fhandle :
	line = line.rstrip()
	print(line.upper())

