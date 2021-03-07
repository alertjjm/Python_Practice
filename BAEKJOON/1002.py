import math
T=int(input())
result=[]
for i in range(T):
    x1, y1, r1, x2, y2, r2=map(float,input().split())
    rs=float(r1+r2)
    rm=float(abs(r1-r2))
    distance=((x1-x2)**2+(y1-y2)**2)**0.5
    if(distance==0):
        if(r1==r2):
            result.append(-1)
        else:
            result.append(0)
    else:
        if (distance == rs or distance == rm):
            result.append(1)
        elif(distance<rs and distance>rm):
            result.append(2)
        else:
            result.append(0)
for r in result:
    print(r)