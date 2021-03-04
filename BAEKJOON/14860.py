N,M=map(int,input().split()) #M: 높이 N: 너비
DIVISION=10**9+7
result=1
templist=[[0 for i in range(N+1)] for j in range(M+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        x=i
        y=j
        while(x!=0 and y!=0):
            if(x>=y):
                x=x-y*(x//y)
            else:
                y=y-x*(y//x)
        if(x==0):
            item=y
        else:
            item=x
        templist[j][i]=item
        result*=item
for line in templist:
    print(line)
print(result%DIVISION)