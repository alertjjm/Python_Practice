N=int(input())
house=[]
dp=[[[0]*3 for i in range(N)] for j in range(N)]
for i in range(N):
    house.append(list(map(int,input().split())))
dp[0][0][0]=1
dp[0][1][0]=1
for i in range(2,N):
    if(house[0][i]==0):
        dp[0][i][0]=dp[0][i-1][0]
for i in range(1,N):
    for j in range(2,N):
        if(house[i][j]==0 and house[i-1][j]==0 and house[i][j-1]==0):
            dp[i][j][2]=dp[i-1][j-1][0]+dp[i-1][j-1][1]+dp[i-1][j-1][2]
        if(house[i][j]==0):
            dp[i][j][0]=dp[i][j-1][0]+dp[i][j-1][2]
            dp[i][j][1]=dp[i-1][j][1]+dp[i-1][j][2]
print(sum(dp[N-1][N-1]))
