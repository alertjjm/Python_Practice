N,M=map(int,input().split())
mp=[]
dp=[[0 for i in range(M)] for j in range(N)]
for i in range(N):
    mp.append(list(input()))
for i in range(N):
    for j in range(M):
        if(mp[i][j]=='1'):
            dp[i][j]=1
for i in range(N):
    for j in range(M):
        if(mp[i][j]=='1'):
            if(i==0 or j==0):
                dp[i][j]=1
            else:
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
maxitem=0
for i in range(N):
    for j in range(M):
        if(maxitem<dp[i][j]):
            maxitem=dp[i][j]
print(pow(maxitem,2))