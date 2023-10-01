import random
print("ROCK-PAPER-SCISSORS")
n=int(input(("Choose one : 1-ROCK 2-PAPER 3-SCISSORS:\n")))
f=1
Elm=[1,2,3]
c=0
u=0
while 1:
    r=random.choice(Elm)
    print("computer choiced :",r)
    if (n==1 and r==1)or (n==2 and r==2)or(n==3 and r==3):
        print(" Draw no score added")
    elif (n==1 and r==2)or (n==2 and r==3)or(n==3 and r==1):
        print("COMPUTER WINS ")
        c+=1
    elif (n==1 and r==3)or(n==2 and r==1)or(n==3 and r==2):
        print("YOU WIN")
        u+=1
    '''f=int(input(("if you want to continue press 1")))
        if f!=1:
        break
        else:'''
    n=int(input(("Choose one : 1-ROCK 2-PAPER 3-SCISSORS:\n")))
    if n not in Elm:
        break
print("Your Score:",u," Computer Score:",c)
        
    
