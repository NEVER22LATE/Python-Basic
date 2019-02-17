
# Coursera Exercise 1


#Exercise 1:
Write a program which repeatedly reads numbers until the user enters "done". Once 
"done" is entered, Print out the total, count, and average of the numbers. If the 
user enters anything other than a number, detect their mistake usint try and except 
and print an error message and skip to the next number.

count = 0
tot = 0.0

while True :
    try :
        n = input() 
        if n == 'done' : 
            break
        else :
            num = float(n)
            count = count + 1
            tot = tot + num
            print(num, tot)
    except :
        print(n  ,"Invalid Number") 
    
print(tot,count,tot/count)
    

