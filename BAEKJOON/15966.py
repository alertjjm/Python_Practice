N=int(input())
dplist=[0 for j in range(N+1)]
nums=list(map(int, input().split()))
for i in range(N):
    dplist[i]=1
    for j in range(0,i):
        if(nums[j]+1==nums[i]):
            dplist[i]=max(dplist[i],dplist[j]+1)
print(dplist[N-1])