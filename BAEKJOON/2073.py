D,P=map(int, input().split())
dp=[0]*(D+1)
pipes=[]
dp[0]=10**6
for i in range(P):
    L,C=map(int, input().split())
    pipes.append([L,C])
    for j in range(D,L-1,-1):
        dp[j] = max(dp[j], min(dp[j - L], C))
print(dp[D])