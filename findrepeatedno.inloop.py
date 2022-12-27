L=[37,56,43,29,81,64,97,85,74,13,46]
count=0
result=False
S=int(input('Enter the element you want to search='))
for x in range(len(L)):
    if S==L[x]:
        count=count+1
        result=True
print(S,'is present',count,'times')
