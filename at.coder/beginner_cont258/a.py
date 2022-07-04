K = int(input())

h = 21
m=K
if K >=60 and m -60 <10:
    print('22:0'+ str(K-60))
elif  K >=60 and m -60 >=10:
    print('22:' + str(K-60) )
elif K < 10:
    print('21:0'+ str(K))
else:
    print('21:'+ str(K))