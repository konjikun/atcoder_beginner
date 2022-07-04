N,K = map(int,input().split())
a = (input().split())

#K個となりを入れ替えられる

def nami ():
    for _ in range(100):
    
        mini = min(a)
        left1 = a.index(mini)
        if left1 != 0:
            a.pop(mini)
        elif left1 / K == 0:
            print('Yes')
        else:
            print('No')

nami()

if len(a) == 0:
    print('Yes')

