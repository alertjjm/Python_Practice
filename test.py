import math
t=int(input())
li=[]
for i in range(t):
    n,x=map(int, input().split())
    li.append((n,x))
for n,x in li:
    if n<=2:
        print(1)
    else:
        if (n-2)%x==0:
            print((n-2)//x+1)
        else:
            print(math.floor((n-2)/x)+2)

