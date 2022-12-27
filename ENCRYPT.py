def encrypt(str):
    e=''
    L=len(str)
    for x in range(L):
        if ord(str[x])>=88 and ord(str[x])<=90:
            e=e+chr((ord(str[x])-26)+3)
        else:
            e=e+chr(ord(str[x])+3)
I=input('enter input string=')
e=encrypt(I)
print('encrypted string=',I)
