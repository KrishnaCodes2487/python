L=[37,56,43,29,81,64,97,85,74,13,46]
result=False
S=int(input('Enter the element you want to search='))
for x in range(len(L)):
    if S==L[x]:
        print(S,'found at index location=',x)
        result=True
if result==False:
    print(S,'does not exist')
