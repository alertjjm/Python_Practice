N=int(input())
A=list(map(int,input().split(' ')))
dplist=[1 for i in range(N+1)]
for i in range(N):
    mini=0
    for j in range(i):
        if(A[i]>A[j]):
            dplist[i]=max(dplist[i],dplist[j]+1)
print(max(dplist))