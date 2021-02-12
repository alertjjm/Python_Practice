N,M=map(int, input().split())
dplist=[[0 for i in range(N)] for j in range(M)]
count()
for i in range(N):
    temp=list(map(int,input().split()))
    for j in range(M):
        dplist[i][j]=temp[j]
