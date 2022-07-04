N = int(input())
S = [input() for _ in range(N)]

r =[]
tim =[]
b = 0
s = str(b)
time = 0
for i in S:
    for _ in range(8000):
        leal = time % 10
        if i[leal] == s:
            time += 1
            r.append(_)
            break
        else:
            time += 1
    if len(r) == N:
        tim.append(time)
        break
print(time-1)