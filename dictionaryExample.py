
# write a program to find most frequent name in the dictionary

names = {}
while True : 
	name = input(" Enter the names: ")
	if name == 'done' :
		break 
	if name in names :	
		names[name] = names[name] + 1
	else  :
		names[name] = 1

maxfrequency = 0 
mostfrequentname = None 
for itr in names :
	if names [itr] > maxfrequency :
		maxfrequency = names[itr]
		mostfrequentname = itr
for itr in names :
	print(itr, names[itr]) 
print(mostfrequentname, maxfrequency)
