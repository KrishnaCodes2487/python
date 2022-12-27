L=list()
n=int(input('Enter size of list='))
for x in range(n):
    e=int(input('Enter element='))
    L.append(e)
NL=[m for m in L if m%5==0]
print(L)
print(NL)
L[0],L[-1]=L[-1],L[0]
print(L)
L[0]=L[0]+L[-1]
L[-1]=L[0]-L[-1]
L[0]=L[0]-L[-1]
print(L)
