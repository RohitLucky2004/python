x=input("Enter message to encrypt it:")
k=int(input("Enter shift key in digits"))
c=""
for i in range(0,len(x)):
    if x[i].isalpha() or x[i].isnumeric():
        if ord(x[i])+k>=123 and x[i].isalpha():
            n=ord(x[i])+k-123
            c+=chr(97+n)
        else:
            c+=chr(ord(x[i])+k)
    else:
       c+=x[i]
print("encrypted message:",c)
xi=""
for i in range(0,len(c)):
    if c[i].isalpha()or c[i].isnumeric():
        if ord(c[i])-k<97 and c[i].isalpha():
            n=ord(c[i])-97
            xi+=chr(123-(k-n))
        else:
            xi+=chr(ord(c[i])-k)
    else:
        xi+=c[i]
print("decrypted message:",xi)

        
