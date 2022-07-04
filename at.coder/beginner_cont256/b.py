N =int(input())
A = list(map(int,input().split()))

P =0
listx =[0,0,0,0]

for i in (A):
    listx[0] += 1
    listy =listx.copy()
    b =0
    for s in listy:
        b +=1
        if s  ==1 and b-1 + i < 4:
            listx[b-1+i] +=1
            listx[b-1] -= 1
        elif s ==1 and b-1 + i >= 4:
            P += 1
            listx[b-1] -= 1
print(P)
