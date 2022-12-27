n=input('Enter the string in upper case=')
s=''
for a in n:
    s=s+(chr(ord(a)+32))
print('String in lower case=')
print(s)
