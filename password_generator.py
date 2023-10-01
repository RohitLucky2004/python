import string
import random
alpbts=list(string.ascii_letters)
spclchr=['~','!','@','#','$','%','^','&','-','+','=','/','*','?','|']
numbers=['1','2','3','4','5','6','7','8','9']
password=random.choice(alpbts)
a=int(input("enter no of alphabits:\n"))-1
b=int(input("enter no of special symbols:\n"))
c=int(input("enter no of numbers:\n"))
d=a+b+c
s=[1,2,3]
while d!=0:
    i=random.choice(s)
    if i==1 and a!=0:
        al=random.choice(alpbts)
        password+=al
        a-=1
        d-=1
    elif i==2 and b!=0:
        al=random.choice(spclchr)
        password+=al
        b-=1
        d-=1
    elif i==3 and c!=0:
        al=random.choice(numbers)
        password+=al
        c-=1
        d-=1
    #print(password,al,i)
print("Genrated password:",password)
