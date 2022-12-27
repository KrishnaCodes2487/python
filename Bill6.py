import string as S
A=list(S.ascii_uppercase)
N=list(range(1,27))
D={k:v for (k,v) in zip(A,N) if v%2==0}
D1={k:v for (k,v) in zip(A,N) if v%2!=0}
print(D)
print(D1)
