H,W = map(int,input().split())
R,C = map(int,input().split())

result =2

if (H ==1 or W == 1):
    if R==H or C ==W:
        result-=1
    if H ==1 and W ==1:
        result=0
        
if R !=1 and R!= H:
    result+=1

if C !=1 and C !=W and W :
    result +=1

print(result)