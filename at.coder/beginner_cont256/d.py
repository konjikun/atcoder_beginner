N = int(input())
LR = [map(int,input().split())for _ in range(N)]
L,R=[list(i) for i in zip (*LR)]

a =0
b = 0
lmin =min(L)
rmax =max(R)

numl =L.index(lmin)
numr =R.index(rmax)
a =[lmin]
b=0

for i in range (1,N):
    left = L[i]
    right = R[i-1]
    if L[i] > right:
        print(a[b],right)
        a.append(L[i])
        b +=1

if L[numr] < R[numl]:
    x = lmin
    y = rmax
    print(x,y)
else:
    print(a[b],rmax)