def minFlipsMonoIncr(s):
    L = len(s)
    dp = [[0] * 2 for _ in range(L)]
    if(s[0]=='1'):
        dp[0][0]=1
    else:
        dp[0][1]=1
    for i in range(L-1):
        if(s[i+1]=='1'):
            dp[i+1][1]=min(dp[i][0],dp[i][1])
            dp[i+1][0]=dp[i][0]+1
        else:
            dp[i+1][1]=min(dp[i][0],dp[i][1])+1
            dp[i+1][0]=dp[i][0]
    return min(dp[-1])

print(minFlipsMonoIncr("00110"))
print(minFlipsMonoIncr("010110"))
print(minFlipsMonoIncr("00011000"))