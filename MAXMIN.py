def MAXMIN(L):
    MX=L[0]
    MN=L[0]
    for x in L:
        if MX<x:
            MX=x
    for y in L:
        if MN>y:
            MN=y
    return MX,MN
X=[38,56,43,72,89,77,98]
a,b=MAXMIN(X)
print('Maximum=',a,'Minimum=',b)
