N=int(input())
dp=[[0,0] for i in range(1001)]
dp[1]=[0,1]
dp[2]=[1,1]
dp[3]=[1,2]
dp[4]=[3,3]
dp[5]=[5,6]
for i in range(6,1001):
    dp[i][0]=dp[i-1][0]+dp[i-1][1]
    if(i%2==1):
        dp[i][0]-=1
    dp[i][1]=dp[i-1][1]+dp[i-1][0]
print(dp[N][0])