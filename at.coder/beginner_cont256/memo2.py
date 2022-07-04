N = int(input())
LR = [map(int,input().split())for _ in range(N)]
L,R=[list(i) for i in zip (*LR)]

a =0
b = 0
lmax =min(L)
rmax =max(R)

numl =L.index(lmax)
numr =R.index(rmax)

x =[]
y =[]

if L[numr] < R[numl]:
    x.append(lmax)
    y.append(rmax)
else:
    R.remove(numr)

c =-1
for s in range (len(x)):
    c +=1
    print(x[c],y[c])
    