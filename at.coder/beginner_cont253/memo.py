H,W = map(int,input().split())
S = []
for i in range(H):
    S.append(input())

def vertical():
    d = 0
    v = 0
    for i in S:
        ex = i.count('o') 

        if d == 1 and ex == 1:
            verti2 = v
            c = v
        elif ex == 1 or 2:  #１回目のoがあったら
            verti1 = v
            b = v
            d +=1
            if ex == 2 and d ==1: #２回目のoがあったら
                verti2 = v
                c = v
        else:
            break

    result_vertical = abs(verti1 - verti2) #縦移動完了
    
    if result_vertical == 0:
        mai = S[verti1]
        hor1 = mai.index('o')
        maimai = mai.lstrip('o')
        hor2 = maimai.index('o')
        hor2 += 1

        result_horizontal = abs(hor1 - hor2) #横移動完了
        result = result_horizontal + result_vertical
        return result
                    
    hor1 = S[b].index('o')
    hor2 = S[c].index('o')
 
    result_horizontal = abs(hor1-hor2)
 
    result = result_horizontal + result_vertical

    return result

print(vertical())
    