from collections import deque
M,N,H=map(int, input().split(' '))
box=[[[0 for i in range(M)] for j in range(N)] for k in range(H)]
daylist=[[[0 for i in range(M)] for j in range(N)] for k in range(H)]
for i in range(H):
    for j in range(N):
        box[i][j]=list(map(int, input().split(' ')))

def checkfinished():
    global box
    for i in range(H):
        for j in range(N):
            if(0 in box[i][j]):
                return False
    return True

q=deque()
def bfs():
    global q
    global box
    dhlist=[-1,1,0,0,0,0]
    dxlist=[0,0,-1,1,0,0]
    dylist=[0,0,0,0,-1,1]
    while len(q)>0:
        h,n,m=q.popleft()
        for i in range(len(dhlist)):
            posh = h + dhlist[i]
            posy = n + dylist[i]
            posx = m + dxlist[i]
            if(0<=posh<H and 0<=posy<N and 0<=posx<M):
                if(box[posh][posy][posx]==0):
                    box[posh][posy][posx]=1
                    daylist[posh][posy][posx]=daylist[h][n][m]+1
                    q.append([posh,posy,posx])
for i in range(H):
    for j in range(N):
        for k in range(M):
            if(box[i][j][k]==1):
                q.append([i,j,k])

bfs()
maxlist=[]
for i in range(H):
    for j in range(N):
        maxlist.append(max(daylist[i][j]))
if(checkfinished()):
    print(max(maxlist))
else:
    print(-1)