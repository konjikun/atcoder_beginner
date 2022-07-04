N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

c = max(A)
d = 0 #おいしさ最大
e = []
for a in A:
    if a == c:
        e.append(d)
    d += 1

def result():
    for i in e:
        for b in B:
            if i+1 == b:
                return 'Yes'
    return 'No'

print(result())
    
    

    
    
