N=int(input())
ways=list(input())
dplist=[0]*N
dplist[0]=1
if(ways[1]=='1'):
    dplist[1]=1
for i in range(2,N):
    if(ways[i]=='1' and ways[i-1]=='1'):
        dplist[i]+=dplist[i-1]
    if (ways[i] == '1' and ways[i - 2] == '1'):
        dplist[i]+=dplist[i-2]
print(dplist.pop())