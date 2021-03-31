import bisect
N=int(input())
arr=[0]+list(map(int,input().split()))
d=[0]*(N+1)
lis=[-99999999999999]
for i in range(1,N+1):
    if(lis[-1]<arr[i]):
        lis.append(arr[i])
        d[i]=len(lis)-1
    else:
        l=bisect.bisect_left(lis,arr[i])
        d[i]=l
        lis[l]=arr[i]
print(max(d))
res = []
maxval=max(d)
for i in range(N, 0, -1):
    if d[i] == maxval:
        res.append(arr[i])
        maxval -= 1
res.reverse()
for r in res:
    print(r,end=' ')
