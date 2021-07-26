N,M=map(int,input().split())
nums=[]
for i in range(N):
    nums.append(int(input()))
dp=[[-10**8]*(N) for _ in range(M+1)]
for i in range(N):
    dp[0][i]=nums[i]
dp[1][0]=nums[0]
for i in range(1,N):
    for j in range(i):
        dp[1][i]=max(dp[1][i],sum(nums[j:i+1]),nums[i])
for i in range(2,M+1):
    for j in range(2,N):
        for k in range(2,j+1):
            dp[i][j]=max(dp[i][j],dp[i-1][k-2]+sum(nums[k:j+1]))
print(max(dp[-1]))