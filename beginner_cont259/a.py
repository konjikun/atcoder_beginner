N,M,X,T,D = map(int,input().split())

if M < X :
    result = T - (X -M) *D
else:
    result =T
print(result)