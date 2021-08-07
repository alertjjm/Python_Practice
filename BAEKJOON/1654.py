K,N=map(int,input().split())
lanline=[]
for i in range(K):
    lanline.append(int(input()))
left=0
right=2**31-1
result=-1
while(left<=right):
    mid=(left+right)//2
    cnt=0
    for lan in lanline:
        cnt+=lan//mid
    if(cnt<N):
        right=mid-1
    else:
        result=max(result,mid)
        left=mid+1
print(result)