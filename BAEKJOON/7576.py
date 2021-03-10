from collections import deque
M,N=map(int, input().split(' '))
H=1
box=[[0 for i in range(M)] for j in range(N)]
daylist=[[0 for i in range(M)] for j in range(N)]
for j in range(N):
    box[j]=list(map(int, input().split(' ')))

def checkfinished():
    global box
    for j in range(N):
        if(0 in box[j]):
            return False
    return True

q=deque()
def bfs():
    global q
    global box
    dxlist=[-1,1,0,0]
    dylist=[0,0,-1,1]
    while len(q)>0:
        n,m=q.popleft()
        for i in range(len(dxlist)):
            posy = n + dylist[i]
            posx = m + dxlist[i]
            if(0<=posy<N and 0<=posx<M):
                if(box[posy][posx]==0):
                    box[posy][posx]=1
                    daylist[posy][posx]=daylist[n][m]+1
                    q.append([posy,posx])
for j in range(N):
    for k in range(M):
        if(box[j][k]==1):
            q.append([j,k])

bfs()
maxlist=[]
for j in range(N):
    maxlist.append(max(daylist[j]))
if(checkfinished()):
    print(max(maxlist))
else:
    print(-1)