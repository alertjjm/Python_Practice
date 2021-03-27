import sys
N,Q=map(int,input().split())
prodcutList=[i for i in range(500001)]
for i in range(N-1):
    upper,lower=map(int,sys.stdin.readline().rstrip().split())
    prodcutList[lower]=upper
resultlist=[]
for i in range(Q):
    upper,lower=map(int,sys.stdin.readline().rstrip().split())
    cur=lower
    st=True
    while(prodcutList[cur]!=cur):
        cur=prodcutList[cur]
        if(cur==upper):
            resultlist.append("yes")
            st=False
            break
    if(st):
        resultlist.append("no")
for r in resultlist:
    print(r)