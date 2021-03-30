import sys
sys.setrecursionlimit(10**6)
N=int(input())
workparents=[i for i in range(N+1)]
graph=[[] for i in range(N+1)]
time=[0]*(N+1)
for i in range(N):
    works=list(map(int,sys.stdin.readline().split()))
    T=works.pop(0)
    M=works.pop(0)
    time[i + 1] = T
    for w in works:
        graph[i+1].append(w)
result= 10000000
visited=[False]*(N+1)
q=[1]
dplist=[-1]*(N+1)
dplist[1]=time[1]
def dp(n):
    global dplist
    temp=time[n]
    templist=[]
    for j in graph[n]:
        if(dplist[j]==-1):
            templist.append(dp(j))
        else:
            templist.append(dplist[j])
    dplist[n]=temp+max(templist) if len(templist)!=0 else temp
for i in range(1,N+1):
    dp(i)
print(max(dplist))
