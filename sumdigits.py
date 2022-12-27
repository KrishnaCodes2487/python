s=0
def sum(n):
    global s
    if n!=0:
        r=n%10
        s=s+r
        n=n//10
        sum(n)
    return s
reg=int(input('Enter 10 digit reg no='))
p=sum(reg)
print('sum',p)
