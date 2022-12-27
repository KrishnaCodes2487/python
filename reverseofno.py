n=int(input('Enter the value of n='))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print('Reverse=',rev)



n=int(input('Enter the value of n='))
m=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print('Reverse=',rev)
if m==rev:
    print(m,'is palindrome')
else:
    print(m,'is not palindrome')



n=int(input('Enter the value of n='))
m=n
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(' Total sum=',sum)
