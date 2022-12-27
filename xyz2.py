old=input('Enter the string=')
old=old.upper()
new=()
L=len(old)
for x in range(L-1,-1,-1):
    new=new+old[x]
if old==new:
    print('Palindrome')
else:
    print('Not palindrome')
    
