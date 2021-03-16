N=int(input())
A=list(map(int, input().split()))
dplist=[1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if(A[j]>A[i]):
            dplist[i]=max(dplist[i],dplist[j]+1)
print(dplist)