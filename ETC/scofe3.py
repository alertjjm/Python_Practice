N=int(input())
spaces=[]
resultlist=[0]*N
dplist=[[0]*N for i in range(N)]
for i in range(N):
    spaces.append(list(input()))
    for j in range(N):
        if(spaces[i][j]=='1'):
            dplist[i][j]=1
            resultlist[0]+=1

for l in range(1,N):
    for i in range(0,N-l):
        for j in range(0,N-l):
            if(dplist[i][j]==l):
                status=True
                xstart=j+l
                ystart=i+l
                for k in range(l+1):
                    if(dplist[ystart][j+k]==0):
                        status=False
                        break
                for k in range(l+1):
                    if(dplist[i+k][xstart]==0):
                        status=False
                        break
                if(status):
                    dplist[i][j]=l+1
                    resultlist[l]+=1
print("total: "+str(sum(resultlist)))
for i in range(len(resultlist)):
    if(resultlist[i]==0):
        break
    else:
        print("size["+str(i+1)+"]: "+str(resultlist[i]))
