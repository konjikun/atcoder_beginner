H, W = map(int, input().split())
S = [input() for _ in range(H)]
P = []
for row in range(H):
    for col in range(W):
        if S[row][col] == "o":
            P.append((row, col))
ar, ac = P[0]
br, bc = P[1]
ans = abs(ar - br) + abs(ac - bc)
print(ans)
