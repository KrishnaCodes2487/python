for x in range(1,11):
    for y in range(1,6):
        print(x+y)


for x in range(1,6):
    for y in range(1,x+1):
        print(y,end=" ")
print()


for x in range(1,11):
    for y in range(1,11):
        print(x*y,end=" ")
print()


for x in range(1,11):
    for y in range(1,11):
        print(x,'*',y,'=',x*y)
