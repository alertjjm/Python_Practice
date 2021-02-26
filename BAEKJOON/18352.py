'''
메모리초과
INF= 3000
N,M,K,X=map(int,input().split(' '))
graphs=[[INF for i in range(N+1)] for j in range(N+1)]
for i in range(M):
    A,B=map(int,input().split(' '))
    graphs[A][B]=1
visited=[False for i in range(N+1)]
distance=[INF for i in range(N+1)]
def solve(n):
    for i in range(1,N+1):
        distance[i]=graphs[n][i]
    visited[n]=True
    distance[n]=0
    for i in range(1,N+1):
        mini=INF
        v=-1
        for j in range(1,N+1):
            if(distance[j]<mini and visited[j]==False):
                mini=distance[j]
                v=j
        visited[v]=True
        for w in range(1,N+1):
            if(visited[w]==False):
                if(distance[v]+graphs[v][w]<distance[w]):
                    distance[w]=distance[v]+graphs[v][w]
    result=[]
    for d in range(1,len(distance)):
        if(distance[d]==K):
            result.append(d)
    if(len(result)==0):
        print(-1)
    else:
        for r in result:
            print(r)
solve(X)'''
##성공
import sys
from collections import deque
INF= 300000
N,M,K,X=map(int,sys.stdin.readline().rstrip().split())
graphs=[[] for j in range(N+1)]
for i in range(M):
    A,B=map(int,sys.stdin.readline().rstrip().split())
    graphs[A].append(B)
visited=[False for i in range(N+1)]
distance=[INF for i in range(N+1)]
def solve(n):
    result = []
    global distance
    q=deque()
    q.append((n,0))
    visited[n]=True
    while q:
        m=q.popleft()
        depth=m[1]
        idx=m[0]
        if(depth==K):
            result.append(idx)
        elif depth<K:
            for con in graphs[idx]:
                if(visited[con]==False):
                    visited[con]=True
                    q.append((con, depth + 1))
    return result

result=solve(X)
'''for d in range(1,len(distance)):
    if(distance[d]==K):
        result.append(d)'''
if(len(result)==0):
    print(-1)
else:
    for r in result:
        print(r)
