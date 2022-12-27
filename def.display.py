def display(L):
    total=0
    for x in range (len(L)):
        total=total+L[x]
    return total
X=[38,56,43,72,89,77,98]
S=display(X)
print('Total sum=',S)
