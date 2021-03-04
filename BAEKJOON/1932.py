N=int(input())
triangle=[[] for i in range(N)]
dplist=[[-1 for i in range(N+1)] for j in range(N+1)]
for i in range(N):
    triangle[i]=list(map(int,input().split()))
dplist[N-1]=triangle[N-1]

def dp(x,y):
    if(dplist[y][x]!=-1):
        return dplist[y][x]
    else:
        dplist[y][x]=max(dp(x,y+1)+triangle[y][x],dp(x+1,y+1)+triangle[y][x])
        return dplist[y][x]
print(dp(0,0))