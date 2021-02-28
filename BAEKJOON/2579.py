N=int(input())
stairs=[]
for i in range(N):
    stairs.append(int(input()))
if(N<=2):
    print(sum(stairs))
else:
    dplist=[0 for i in range(N+1)]
    dplist[0]=0
    dplist[1]=stairs[0]
    dplist[2]=stairs[0]+stairs[1]
    for i in range(3,N+1):
        dplist[i]=max(stairs[i-1]+dplist[i-2],stairs[i-1]+stairs[i-2]+dplist[i-3])
    print(dplist[N])