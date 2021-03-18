n=int(input())
boxes=list(map(int, input().split()))
dplist=[1]*n
for i in range(n):
    for j in range(i):
        if(boxes[j]<boxes[i]):
            dplist[i]=max(dplist[i],dplist[j]+1)
print(max(dplist))