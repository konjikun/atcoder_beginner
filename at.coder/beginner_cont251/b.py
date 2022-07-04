N,W = list(map(int,input().split()))
A = list(map(int,input().split()))

A.sort()
ans =0

for d in A: #１つのペア
    if d >= W:
        A.remove(d)
    elif d < W:
        ans += 1

for a in A: #２つのペア
    for b in A:
        
        
    
