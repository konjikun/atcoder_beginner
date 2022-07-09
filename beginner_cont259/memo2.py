S= (input())
T=(input())

a =0

for t in T:
    if S[a] == t:
            a+=1
            continue

    else:
        while True:
            if S[a] != t and (S[a-1] == t == S[a-2] or S[a+1] == t ==S[a+2]):
                S = S[:a] + S[a-1] + S[a:]
                a+=1
            else:
                break

    a=0

if S ==T:
    print('Yes')
else:
    print('No')

