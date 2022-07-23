import math
a,b,d = map(int,input().split())

asd = math.sin(math.radians(d)) * a
acd = math.cos(math.radians(d)) * a
bsd = math.sin(math.radians(d)) * b
bcd = math.cos(math.radians(d)) * b

x = acd - bsd
y = asd + bcd
print(x,y)