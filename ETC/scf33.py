import sys
N,Q=map(int,input().split())
prodcutList=[{i} for i in range(N+1)]
for i in range(N-1):
    upper,lower=map(int,sys.stdin.readline().split())
    prodcutList[lower]=prodcutList[lower].union(prodcutList[upper])
for i in range(Q):
    upper,lower=map(int,sys.stdin.readline().split())
    if(upper in prodcutList[lower]):
        print("yes")
    else:
        print("no")