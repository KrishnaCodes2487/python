a=1
while a<=10:
    print("KOCO3")
    a=a+1

    
n=int(input('Enter the value of n='))
fact=1
a=1
while a<=n:
    fact=fact*a
    a=a+1
    print('Factorial of',n,'is=',fact)

n=int(input('Enter the value of n='))
fact=1
a=1
for a in range(1,n+1):
    fact=fact*a
    print('Factorial of',n,'is=',fact)

    
dc=0
n=int(input('Enter the value of n='))
for a in range(1,n+1):
    if n%a==0:
        dc=dc+1
if dc==2:
    print(n,'is prime number')
else:
    print(n,'is not prime number')


    
