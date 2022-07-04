h1, h2, h3, w1,w2,w3 = map(int, input().split())
def gen(x): # 和がxになる
    ans = []
    for i in range(1, 30):
        for j in range(1, 30):
            for h in range(1, 30):
                if i + j + h == x:
                    ans.append((i, j, h))
    return ans
can1 = gen(h1) # 和がh1になるi,h,jを列挙
can2 = gen(h2) # 和がh2になるi,h,jを列挙
can3 = gen(h3) # 和がh3になるi,h,jを列挙
ans = 0
for pat1 in can1:
    for pat2 in can2:
        for pat3 in can3:
            # これで、各横はh1,h2,h3になっている。さて、縦についてOK?
            if pat1[0]+pat2[0]+pat3[0] != w1: continue
            if pat1[1]+pat2[1]+pat3[1] != w2: continue
            if pat1[2]+pat2[2]+pat3[2] != w3: continue
            ans += 1
print(ans)