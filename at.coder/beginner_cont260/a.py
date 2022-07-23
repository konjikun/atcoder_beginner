import sys
i = input()

S =[]
for a in i:
    S.append(a)

if S[0] !=S[1]:
    if S[0] != S[2]:
            print(S[0])
            sys.exit()

if S[1] != S[0]  :
    if S[1] !=S[2]:
        print(S[1])
        sys.exit()

if S[2] != S[0] :
    if  S[2] != S[1]:
        print(S[2])
        sys.exit()

print('-1')
