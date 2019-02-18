# Write another program that prompts for a list of numbers 
# as above and at the end prints out both the maximum and 
# minimum of the numbers instead of the average.

# note for this exercise 
	# 1. three methods are available for inserting into a list append is used to add element to the end of the list 
	 # 2. insert is used to inset at any specific position in the list
	 #3 . extend is used to add elements to a list by adding on all the elements of the iterate you pass to it .

def print_max_and_min(list1) :
	max_so_far = 0.0
	min_so_far = 10000.0

	for val in list1 :
		if max_so_far > val :
			val = max_so_far
		elif min_so_far < val : 
			val = min_so_far

	print(max_so_far, min_so_far)

while True :
	list1 = []  
	num = input()
	if num == 'done' :
		break 
	try :
		listnum = float(num)
	except :
		print("Invalid Input :")
		continue 	
	list1.append(listnum)

for number in list1:
	print(number)
print_max_and_min(list1)
