a=int(input('Enter first number='))
b=int(input('Enter second number='))
while a!=b:
    if a>b:
        a=a-b
        else:
            b=b-a
    HCF=a
    print('HCF=',HCF)
