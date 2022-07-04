N,K,Q =list(map(int,input().split()))
A = list(map(int,input().split()))#*K
L =list(map(int,input().split()))#*Q

a = len(A) -1
A.append(-3)
A.append(-4)
for s in L:
    if A[s -1] != N and A[s-1] != A[s]-1:
        A[s-1] =A[s-1] +1
A.remove(-3)
A.remove(-4)

print(*A, sep =' ')
