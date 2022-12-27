with open('abc.txt','r')as ab:
    data=ab.read()
f=open('new.txt','w')
e=''
for x in data:
    if ord(x)>=65 and ord(x)<=90:
        t=ord(x)
        t=t+32
        e=e+chr(t)
        f.write(e)
    elif ord(x)>=47 and ord(x)<=122:
        t=ord(x)
        t=t-32
        f.write(chr(t))
    else:
        e=e+x
        f.write(e)
f.close()
