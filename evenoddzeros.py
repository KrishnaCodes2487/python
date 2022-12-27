n=int(input('Enter the number='))
ec=0
oc=0
zc=0
while n!=0:
    r=n%10
    if r==0:
        zc=zc+1
    elif r%2==0:
        ec=ec+1
    else:
        oc=oc+1
    n=n//10             
print('Total even=',ec)
print('Total odd=',oc)
print('Total zeros=',zc)
