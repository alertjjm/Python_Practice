import sys
sys.setrecursionlimit(10**6)
N,M=map(int, input().split())
distances=[]
dplist=[[-1 for i in range(501)] for j in range(10001)]
for i in range(N):
    distances.append(int(input()))
def dp(pos,m):
    ret=0
    if(pos==N-m):
        return 0
    if(pos>N-m):
        return -99999999
    if(dplist[pos][m]>=0):
        return dplist[pos][m]
    if(m<M):
        if(m>0):
            ret=max(dp(pos+1,m+1)+distances[pos],dp(pos+m,0))
        if(m==0):
            ret=max(dp(pos+1,m+1)+distances[pos],dp(pos+1,0))
    elif(m==M):
        ret=dp(pos+m,0)
    dplist[pos][m]=ret
    return ret
print(dp(0,0))
