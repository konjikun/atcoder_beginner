S, T = map(int,input().spllit())
ans = 0
for a in range (S + 1):
    for b in range(S + 1):
        for c in range(S + 1):
            if a + b + c <= S and a * b * c <= T:
                ans += 1
print(ans)
#7重までなら間に合う