import sys
N=int(input())
tap=list(map(int,sys.stdin.readline().split()))
stack=[]
result=[]
for i in range(N):
    item=tap[i]
    while stack:
        popitem=stack[-1]
        if(popitem[0]>=item):
            result.append(popitem[1]+1)
            st=False
            break
        else:
            stack.pop()
    if(not stack):
        result.append(0)
    stack.append([item,i])
for r in result:
    print(r,end=' ')