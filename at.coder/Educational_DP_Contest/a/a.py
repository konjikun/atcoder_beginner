N = int(input())
h = list(map(int,input().split()))
A = [abs(h[i]-h[i+1]) for i in range (N)]
B = [abs(h[i]-h[i+2]) for i in range (N)]
print(A)