import math
a,b,d = map(int,input().split())

asd = math.sin(d) * a
acd = math.cos(d) * a
bsd = math.sin(d) * b
bcd = math.cos(d) * b
print(math.sin(d))

x = acd - bsd
y = asd + bcd
print(x,y)