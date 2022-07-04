H,W = map(int,input().split())
S = [input() for i in range(H)]

vercical = 0
position =[]
for i in S:
    vercical += 1
    horizontal =0
    for w in i:         #ver と  hor は1 origin
        horizontal += 1
        if w == 'o':
            position.append(horizontal)
            position.append(vercical) # list[0,1]がver hor ver hor順
          
ans = abs(position[1] - position[3]) + abs(position[0] - position[2])
print(ans)
