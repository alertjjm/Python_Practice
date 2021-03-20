import sys
N,M=map(int,input().split())
clothes=[]
dplist=[[-1]*N for i in range(M)]
for i in range(M):
    clothes.append(list(map(int,sys.stdin.readline().rstrip().split())))

def dp(counts,ypos,xpos):
    global dplist
    if(ypos==M-1 and xpos==N-1):
        return counts
    if(dplist[ypos][xpos]!=-1):
        return dplist[ypos][xpos]
    #right
    result=[]
    rightx=xpos+1
    righty=ypos
    downx=xpos
    downy=ypos+1
    if(rightx<N):
        result.append(dp(counts+clothes[righty][rightx],righty,rightx))
    if(downy<M):
        result.append(dp(counts + clothes[downy][downx],downy,downx))
    dplist[ypos][xpos]=max(result)
    return dplist[ypos][xpos]
print(dp(clothes[0][0],0,0))