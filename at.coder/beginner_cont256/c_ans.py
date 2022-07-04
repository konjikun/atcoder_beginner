h1,h2,h3,w1,w2,w3 = map(int,input().split())
 
x = [[0]*3 for i in range(3)]
ans = 0
 
for i in range(1,30):
    x[1][1] = i
 
    for j in range(1,30):
        x[1][0] = j
 
        x[1][2] = w2 - (x[1][1] + x[1][0])
        if x[1][2] < 1:
            continue 
        
        for k in range(1,30):
            x[0][1] = k
 
            x[2][1] = h2 - (x[1][1] + x[0][1])
            if x[2][1] < 1:
                continue
            
            for l in range(1,30):
                x[0][0] = l
 
                x[0][2] = w1 - (x[0][0] + x[0][1])
                x[2][0] = h1 - (x[0][0] + x[1][0])
                x[2][2] = w3 - (x[2][0] + x[2][1])
 
                if x[2][2] != h3 - (x[0][2] + x[1][2]):
                    continue
 
                if x[0][2] < 1 or x[2][0] < 1 or x[2][2] < 1:
                    continue
                
                ans += 1
 
print(ans)  