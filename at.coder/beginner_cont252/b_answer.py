# 入力の受け取り
N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

# Aの最大値
Amax=max(A)

# i=0~(K-1)
for i in range(K):
    # A[B[i]-1]=(Aの最大値)ならば
    if A[B[i]-1]==Amax:
        # 「Yes」を出力
        print("Yes")
        # 終了
        exit()

# 「No」を出力
print("No")