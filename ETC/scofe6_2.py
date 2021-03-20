import sys
N,M=map(int,input().split())
clothes=[]
answer=[]
visited=[[0]*N for i in range(M)]
for i in range(M):
    clothes.append(list(map(int,sys.stdin.readline().rstrip().split())))
def dfs(counts,ypos,xpos):
    global answer
    if(ypos==M-1 and xpos==N-1):
        answer.append(counts)
    rightx=xpos+1
    righty=ypos
    downx=xpos
    downy=ypos+1
    if(rightx<N and visited[righty][rightx]==0):
        visited[righty][rightx]=1
        dfs(counts+clothes[righty][rightx],righty,rightx)
        visited[righty][rightx]=0
    if(downy<M and visited[downy][downx]==0):
        visited[downy][downx]=1
        dfs(counts + clothes[downy][downx],downy,downx)
        visited[downy][downx]=0
visited[0][0]=1
dfs(clothes[0][0],0,0)
print(max(answer))