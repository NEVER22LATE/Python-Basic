#Exercise 1:

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
    
