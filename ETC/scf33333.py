import sys
N,Q=map(int,sys.stdin.readline().split())
prodcutList=[{i} for i in range(N+1)]
dplist=[[-1]*(N+1) for _ in range(N+1)]
for i in range(N-1):
    upper,lower=map(int,sys.stdin.readline().split())
    prodcutList[lower]=prodcutList[lower].union(prodcutList[upper])
    for item in prodcutList[upper]:
        dplist[item][lower]=1
for i in range(Q):
    upper,lower=map(int,sys.stdin.readline().split())
    if(dplist[upper][lower]==1):
        print("yes")
    else:
        print("no")