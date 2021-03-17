N=int(input())
dplist=[0]*(31)
dplist[2]=3
if(N<=2):
    print(dplist[N])
else:
    for i in range(4,N+1,2):
        dplist[i]=dplist[i-2]*3
        for j in range(4,i,2):
            dplist[i]+=2*dplist[i-j]
        dplist[i]+=2
    print(dplist)