s = input("Enter string:- ")
l = list(s.split(','))

negative=[]

if len(l)==1 and l[0]=="":
    print(0)
else:
    sum = 0
    for num in l:
        if int(num)<0:
            negative.append(int(num))
        else:
            sum+=int(num)
    
    if len(negative)>0:
        print("negatives not allowed:-",end=" ")
        print(negative)
    else:
        print(sum)