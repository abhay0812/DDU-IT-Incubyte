s = input("Enter string:- ")
l = list(s.split(','))

if len(l)==1 and l[0]=="":
    print(0)
else:
    sum = 0
    for num in l:
        sum+=int(num)
        
    print(sum)