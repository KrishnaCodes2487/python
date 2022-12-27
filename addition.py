total=0
for a in range(1,11):
    total=total+a
    print('Sum',total)
    print()
N=int(input('Enter the last no of series'))
for a in range(1,N+1,2):
    total=total+a
    print('Sum',total)
    print()
N=int(input('Enter the last no of series'))
even=0
odd=0
for a in range(1,N+1):
    if a%2==0:
        even=even+a
    else:
            odd=odd+a
            print('Even sum=',even)
            print('odd sum=',odd)
