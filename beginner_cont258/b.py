N =int(input())
A = a = [list(map(int, input().split())) for l in range(N)]

c =0
e =-1
f =-1
d =[[]]
for i in A:
    e +=1
    for s in i:
        f+=1
        if s > c :
            d.append(A[e[f]])

print(d)