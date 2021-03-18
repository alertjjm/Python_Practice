N,K=map(int, input().split())
dplist=[[0]*(N+1) for i in range(K+1)]
for i in range(N+1):
    dplist[1][i]=1
for i in range(1,K+1):
    for j in range(N+1):
        for k in range(j+1):
            dplist[i][j]+=dplist[i-1][k]
print(dplist[K][N]%1000000000)
