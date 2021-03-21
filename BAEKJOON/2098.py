import sys
N=int(sys.stdin.readline())
cities=[]
dplist=[[10000000]*(1<<N) for i in range(N)]
end=(1<<N)-1
for i in range(N):
    cities.append(list(map(int,sys.stdin.readline().split())))

def dp(cur,visited):
    if visited==end:
        return cities[cur][0]
    if dplist[cur][visited]!=10000000: return dplist[cur][visited]
    for i in range(N):
        if(visited&(1<<i)==0 and cities[cur][i]):
            dplist[cur][visited]=min(dplist[cur][visited],dp(i,visited|1<<i)+cities[cur][i])
    return dplist[cur][visited]

print(dp(0,1<<0))