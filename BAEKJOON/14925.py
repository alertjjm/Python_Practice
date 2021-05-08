M,N=map(int,input().split())
land=[]
for i in range(M):
    land.append(list(map(int,input().split())))
dp=[[1]*N for i in range(M)]
for i in range(M):
    if(land[i][0]!=0):
        dp[i][0]=0
for i in range(N):
    if(land[0][i]!=0):
        dp[0][i]=0
result=0
for i in range(1,M):
    for j in range(1,N):
        if(land[i][j]!=0):
            dp[i][j]=0
        else:
            dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
for i in range(M):
    for j in range(N):
        result=max(result,dp[i][j])
print(result)
