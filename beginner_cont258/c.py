N, Q=map(int,input().split())
S =input()

query =[]
for _ in range(Q):
    h = list(map(int,input().split()))
    query.append(h)

def w(x):
    global S

    S =(S[len(S)-x:len(S)] +S[:len(S)-x])
    return S
    

def y(x):
    return S[x]

for i in query:
    if i[0] == 1:
        w(i[1])
    elif i[0] ==2:
        print(y(i[1]-1))
