n=int(input('Enter the value of n='))
m=n
sum=0
while n!=0:
    r=n%10
    sum=sum+r
    n=n//10
print(' Total sum=',sum)
