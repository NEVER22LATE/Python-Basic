

#Exercise 6: Read the documentation of the string methods at
#https://docs.python.org/library/stdtypes.html#string-methods You
#might want to experiment with some of them to make sure you
#understand how they work. strip and replace are particularly useful.


data = "abcdefghijklmnopqrstuvwxyz"

index = data.find('a')

data.replace("abc","aaaaabbbbb")  # the original string is unchanged

print(data)

data1 = data.replace("abc", "aaaaaaaaaaaaaa")

print(data1)

print(data1.replace('a','xx')) #qill replace each instace a with xx

print(data1.replace('a','xx',1)) # will replace only first instance 

index = data.find('a')

print(index, data.find('a'))
