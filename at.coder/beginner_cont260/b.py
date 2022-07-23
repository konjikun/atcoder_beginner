N,X,Y,Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

As = A.copy()
Bs =B.copy()

result = []

for i in range(X):
    math = max(A)
    na = A.index(math)
    result.append(na+1)
    A.insert(na,-1)
    A.pop(na+1)
    B.insert(na,-1)
    B.pop(na+1)
    

for s in range(Y):
    english = max(B)
    na = B.index(english)
    result.append(na+1)
    A.insert(na,-1)
    A.pop(na+1)
    B.insert(na,-1)
    B.pop(na+1)
    

lists = []
for a in range(N):
    e = A[a] + B[a]
    lists.append(e)
    
c =0
for j in range (Z):
    all = max(lists)
    na = lists.index(all)
    result.append(na+1)
    lists.insert(na,-1)
    lists.pop(na+1)
    

result.sort()
for w in result:
    print(w) 

