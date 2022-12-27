def prime(L):
    for a in range(len(L)):
       dc=0
    for b in range (1,L[a]+1):
        if L[a]%b==0:
            dc=dc+1
      
    if dc==1 or dc==2:
        print(L[a])
