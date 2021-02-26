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
