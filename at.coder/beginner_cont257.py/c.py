import sys
N = int(input())
S = input()
W = list(map(int,input().split()))

chi =[]
ada =[]
a = -1

for s in S:
    s =int(s)
    if s ==1:
        a +=1
        ada.append(W[a])
    else:
        a +=1
        chi.append(W[a])

if len(ada) ==N or len(chi) == N:
    print(N)
    sys.exit()

result =N

if min(ada) > max(chi):
    print(result)

for i in range(N):
    if min(ada) <= max(chi):
        result -= 1
        ada.remove(min(ada))

    if N % 2 == 0:
        if len(ada) == N /2:
            break
    else:
        if len(ada) == N //2 +1:
            break

print(result)
