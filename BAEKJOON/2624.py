T=int(input())
k=int(input())
coins=[]
for i in range(k):
    p,n=map(int,input().split())
    coins.append([p,n])
coins.sort(key=lambda x:-x[0])
dp=[[0]*(T+1) for _ in range(len(coins)+1)]
dp[0][0]=1
for i in range(1,len(coins)+1):
    val, num = coins[i-1]
    for j in range(num+1):
        for l in range(T+1):
            if(l+j*val<=T):
                dp[i][l+j*val]+=dp[i-1][l]
print(dp[-1][-1])