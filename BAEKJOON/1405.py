NUM,E,W,S,N=map(int, input().split(" "))
problist=[E/100,W/100,S/100,N/100]
graph=[[0 for i in range(51)]for j in range(51)]
dxdir=[1,-1,0,0]
dydir=[0,0,-1,1] #동서남북
def dfs(depth,x,y,gh):
    ret=0
    gh[y][x]=1
    if(depth==0):
        return 1
    for i in range(len(dxdir)):
        xpos=x+dxdir[i]
        ypos=y+dydir[i]
        if(graph[ypos][xpos]==1):
            continue
        ret+=dfs(depth-1,xpos,ypos,gh)*problist[i]
        gh[ypos][xpos]=0
    return ret
print(dfs(NUM,25,25,graph))