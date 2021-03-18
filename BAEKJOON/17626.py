N=int(input())
cnt=N
dp=[0,1]
for i in range(2,N+1):
    minvalue=999999
    j=1
    while(j*j<=i):
        minvalue=min(minvalue,dp[i-(j*j)]+1)
        j+=1
    dp.append(minvalue)
print(dp.pop())