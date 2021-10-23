s = input("Enter string:- ")
s = s.replace("n","o")
s = s.replace("\o",",")
l = list(s.split(','))

messege="ok"
for num in l:
    if num=="":
        messege = "NOT ok"
        
print(messege)