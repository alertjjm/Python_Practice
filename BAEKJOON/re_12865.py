N,K=map(int,input().split())
dp=[[0]*(K+1) for _ in range(N+1)]
stuffs=[[]]
for i in range(N):
    stuffs.append(list(map(int,input().split())))
for i in range(1,N+1):
    weight,value=stuffs[i]
    for j in range(1,K+1):
        if(j-weight>=0):
            dp[i][j]=max(dp[i][j],dp[i-1][j-weight]+value,dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])