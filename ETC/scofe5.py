import sys
sys.setrecursionlimit(10**6)
N,M=map(int,input().split())
products=[]
dplist=[0]*M
dx=[0,-1,1]
dy=[1,0,0]
dirlen=len(dx)
for i in range(M):
    products.append(list(input()))
starts=[]
for i in range(N):
    if(products[0][i]=='c'):
        starts.append(i)
result=[]
visited=[[0]*N for i in range(M)]
def dfs(counts,ypos,xpos):
    global visited
    if(ypos==M-1):
        result.append(counts)
        return
    newxpos = xpos + dx[0]
    newypos = ypos + dy[0]
    if (0 <= newxpos < N and 0 <= newypos < M and visited[newypos][newxpos]==0 and products[newypos][newxpos]=='.'):
        visited[newypos][newxpos]=1
        dfs(counts,newypos,newxpos)
        visited[newypos][newxpos] = 0
    for i in range(1,dirlen):
        newxpos=xpos+dx[i]
        newypos=ypos+dy[i]
        if(0<=newxpos<N and 0<=newypos<M and visited[newypos][newxpos]==0 and products[newypos][newxpos]=='.'):
            visited[newypos][newxpos] = 1
            dfs(counts+1,newypos,newxpos)
            visited[newypos][newxpos] = 0
for start in starts:
    visited = [[0] * N for i in range(M)]
    visited[0][start] = 1
    dfs(0,0,start)
if(len(result)==0):
    print(-1)
else:
    print(min(result))



