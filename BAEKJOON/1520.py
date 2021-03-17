import sys
sys.setrecursionlimit(10**6)
M,N=map(int,input().split())
mapGraph=[]
for i in range(M):
    mapGraph.append(list(map(int,sys.stdin.readline().split())))
dplist=[[0]*N for _ in range(M)]
visited=[[0]*N for _ in range(M)]
dplist[0][0]=0
dplist[M-1][N-1]=1
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def dp(now):
    global dplist,visited
    xpos,ypos=now
    if(visited[ypos][xpos]!=0):
        return dplist[ypos][xpos]
    visited[ypos][xpos]=1
    for i in range(len(dx)):
        newxpos=xpos+dx[i]
        newypos=ypos+dy[i]
        if(0<=newxpos<N and 0<=newypos<M and mapGraph[ypos][xpos]>mapGraph[newypos][newxpos]):
            dplist[ypos][xpos]+=dp([newxpos,newypos])
    return dplist[ypos][xpos]
print(dp([0,0]))