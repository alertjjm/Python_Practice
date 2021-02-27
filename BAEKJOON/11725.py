import sys
sys.setrecursionlimit(10**6)
N=int(input())
graphs=[[] for j in range(N+1)]
for i in range(N-1):
    a,b=map(int, input().split(' '))
    graphs[a].append(b)
    graphs[b].append(a)
parents=[0 for i in range(N+1)]
def dfs(x):
    for i in graphs[x]:
        if(parents[x]!=i):
            parents[i]=x
            dfs(i)
dfs(1)
for i in range(2,len(parents)):
    print(parents[i])