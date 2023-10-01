import random 
def dis():
    p='+'
    l='-'
    n='|'
    s=' '
    i=j=0
    for i in range (0,3):
            print("\n",p,l*9,p,"\t",p,l*9,p,"\t",p,l*9,p)
            print("\n",n,s*9,n,"\t",n,s*9,n,"\t",n,s*9,n)
            print("\n",n,s*3,a[i][0],s*3,n,"\t",n,s*3,a[i][1],s*3,n,"\t",n,s*3,a[i][2],s*3,n)
            print("\n",n,s*9,n,"\t",n,s*9,n,"\t",n,s*9,n)
            print("\n",p,l*9,p,"\t",p,l*9,p,"\t",p,l*9,p)
            print()

def computerMove():
    r=random.choice(A)
    i=0
    j=0
    f=1
    print("computer Turn:",r)
    while i<3:
        j=0
        while j<3:
            if a[i][j]==r:
                f=0
                a[i][j]='X'
                break
            j+=1
        if f==0:
            break
        i+=1
    A.remove(r)
    dis()

def check():
    for i in range(0,3):
        if a[i][0]==a[i][1] and a[i][1]==a[i][2] and a[i][0]=='O':
            print("YOU WON THE GAME")
            return 5
        elif a[i][0]==a[i][1] and a[i][1]==a[i][2] and a[i][0]=='X':
            print("YOU LOST THE GAME")
            return 5
        elif a[0][i]==a[1][i] and a[1][i]==a[2][i] and a[0][i]=='X':
            print("YOU LOST THE GAME")
            return 5
        elif a[0][i]==a[1][i] and a[1][i]==a[2][i] and a[0][i]=='O':
            print("YOU WON THE GAME")
            return 5
    if a[0][0]==a[1][1] and a[1][1]==a[2][2] and a[0][0]=='O':
        print("YOU WIN")
        return 5
    elif a[0][0]==a[1][1] and a[1][1]==a[2][2] and a[0][0]=='X':
        print("YOU LOST")
        return 5
    elif a[2][0]==a[1][1] and a[1][1]==a[0][2] and a[2][0]=='O':
        print("YOU WIN")
        return 5
    elif a[2][0]==a[1][1] and a[1][1]==a[0][2] and a[2][0]=='X':
        print("YOU LOST")
        return 5
            
    
a=[['1','2','3'],['4','5','6'],['7','8','9']]
A=['1','2','3','4','5','6','7','8','9']
#dis()
#a[1][1]='x'
#A.remove(str(5))
dis()
mov=1
f=1
move=0
r1=[[0,1,2],[2,2,2],[1,1,1],[0,0,0]]
while move!=5 and mov!=5:
    n=input("enter number you want to making 'O':")
    mov+=1
    i=0
    j=0
    f=1
    while i<3:
        j=0
        while j<3:
            if a[i][j]==n:
                f=0
                a[i][j]='O'
                break
            j+=1
        if f==0:
            break
        i+=1
    dis()
    A.remove(n)
    move=check()
    if move==5:
        break
    computerMove()
    move=check()
    


