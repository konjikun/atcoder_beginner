N,X =list(map(int,input().split()))

lists = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
listus =[]

for i in lists:
    for _ in range(N):
        listus.append(i)

print(listus[X-1])
