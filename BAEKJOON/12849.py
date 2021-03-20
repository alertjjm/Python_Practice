D=int(input())
smap=[[1,2],
      [0,3],
      [0,3,4],
      [1,2,4,5],
      [2,3,5,6],
      [3,4,6,7],
      [4,5,7],
      [5,6]]
dplist=[0,0,0,0,0,0,0,1]
N=8
cnt=0
for i in range(D):
    newdp=[0]*N
    for j in range(N):
        for k in smap[j]:
            newdp[j]+=dplist[k]
    dplist=newdp
print(newdp.pop()%1000000007)

def dfs(now,minute):
    answer=0
    if(minute==0 and now==7):
        return 1
    elif(minute==0):
        return 0
    else:
        for j in smap[now]:
            key=str(minute-1)+","+str(j)
            if(key in dplist):
                answer+=dplist[key]
            else:
                answer+=dfs(j,minute-1)
        dplist[str(minute)+","+str(now)]=answer
        return answer%1000000007
