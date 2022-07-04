h1,h2,h3,w1,w2,w3=list(map(int,input().split()))

listh=[]

def ine(h):
    for i in range(1,29):
        for j in range(1,29):
            for s in range(1,29):
                if s + i + j ==h:
                    listh.append(i,j,s)
    return listh

h1s = ine(h1)
h2s = ine(h2)
h3s = ine(h3)

ans =0
for a in h1s:
    for b in h2s:
        for c in h3s:
            if a[0] + b[0] + c[0] != w1 : continue
            if a[1] + b[1] + c [1] != w2 : continue
            if a[2] + b[2] + c[2] != w3 : continue
            ans +=1
print(ans)
        
