import heapq
que = []
N, L = map(int, input().split())
nlist = list(map(int, input().split()))
idx = 0
result=[]
for i in range(N):
    heapq.heappush(que, (nlist[i], i))
    if (len(que) <= L):
        result.append(que[0][0])
    else:
        left=i-L+1
        while(len(que)!=0 and que[0][1]<left):
            heapq.heappop(que)
        result.append(que[0][0])
for r in result:
    print(r,end=' ')