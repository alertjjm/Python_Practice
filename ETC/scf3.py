import sys
N,Q=map(int,input().split())
prodcutList=[i for i in range(N+1)]
dplist=[[-1]*(N+1) for _ in range(N+1)]
for i in range(N-1):
    upper,lower=map(int,sys.stdin.readline().rstrip().split())
    dplist[upper][lower]=1
    prodcutList[lower]=upper
resultlist=[]
for i in range(Q):
    upper,lower=map(int,sys.stdin.readline().rstrip().split())
    cur=lower
    if(dplist[upper][lower]!=-1):
        if(dplist[upper][lower]==1):
            resultlist.append("yes")
            continue
        else:
            resultlist.append("no")
            continue
    st=True
    while(prodcutList[cur]!=cur):
        cur=prodcutList[cur]
        dplist[cur][lower]=1
        if (dplist[upper][cur] != -1):
            if (dplist[upper][cur] == 1):
                resultlist.append("yes")
                st=False
                break
            else:
                resultlist.append("no")
                st=False
                break
        if(cur==upper):
            resultlist.append("yes")
            st=False
            break
    if(st):
        dplist[upper][lower] = 0
        resultlist.append("no")
for r in resultlist:
    print(r)