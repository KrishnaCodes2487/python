L=([10,20,30,40],[100,200,300,400],[5,15,25,35],[3,9,18,27])
for b in range(len(L)):
    total=0
    for a in range(len(L[b])):
        total=total+L[b][a]
    print('sum of',b+1,'row=',total)
    
    
L=([10,20,30,40],[100,200,300,400],[5,15,25,35],[3,9,18,27])
total=0
for a in range(len(L)):
    for b in range(len(L[a])):
        if a+b==3:
         total=total+L[a][b]
print('Total sum of diagonal=',total)
