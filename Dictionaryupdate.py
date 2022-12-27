D={}
T=('A','B','C','D','E')
X=(10,20,30,40,50)
Z=zip(T,X)
for a,b in Z:
    D.update({a:b})
print(D)


T=('A','B','C')
L=(1,2,3)
M=(10.9,4.6,2.8)
Z=zip(T,L,M)
N=list(Z)
print(N)
