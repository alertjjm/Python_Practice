N=int(input())
gamepan=[[] for i in range(N)]
dplist=[[-1 for i in range(N)] for j in range(N)]
for i in range(N):
    gamepan[i]=list(map(int, input().split()))
dplist[0][0]=1
def dp(x,y):
    if(x<0 or y<0 or x>=N or y>=N):
        return 0
    if(dplist[y][x]>=0):
        return dplist[y][x]
    result=0
    for i in range(x):
        if(gamepan[y][i]+i==x):
            result+=dp(i,y)
    for i in range(y):
        if(gamepan[i][x]+i==y):
            result+=dp(x,i)
    dplist[y][x]=result
    return result
print(dp(N-1,N-1))