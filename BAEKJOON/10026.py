N=int(input())
picture=[]
for i in range(N):
    picture.append(list(input()))
visiteda=[[0]*N for i in range(N)]
aresult=0
bresult=0
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for a in range(N):
    for b in range(N):
        if(visiteda[a][b]==0):
            stack = []
            stack.append([a, b])
            comparecolor=picture[a][b]
            visiteda[a][b] = 1
            while stack:
                y,x=stack.pop()
                for i in range(len(dx)):
                    nextx=x+dx[i]
                    nexty=y+dy[i]
                    if(0<=nextx<N and 0<=nexty<N and picture[nexty][nextx]==comparecolor and visiteda[nexty][nextx]==0):
                        stack.append([nexty,nextx])
                        visiteda[nexty][nextx]=1
            aresult+=1
visiteda=[[0]*N for i in range(N)]
for a in range(N):
    for b in range(N):
        if(visiteda[a][b]==0):
            stack = []
            stack.append([a, b])
            comparecolor=picture[a][b]
            visiteda[a][b] = 1
            while stack:
                y,x=stack.pop()
                for i in range(len(dx)):
                    nextx=x+dx[i]
                    nexty=y+dy[i]
                    if(0<=nextx<N and 0<=nexty<N and (picture[nexty][nextx]==comparecolor or (picture[nexty][nextx]=='R' and comparecolor=='G') or (picture[nexty][nextx]=='G' and comparecolor=='R') ) and visiteda[nexty][nextx]==0):
                        stack.append([nexty,nextx])
                        visiteda[nexty][nextx]=1
            bresult+=1
print(aresult,bresult)


