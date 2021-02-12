import heapq
heap=[]
N=int(input())
for i in range(N):
    temp=list(map(int, input().split()))
    for t in temp:
        if(len(heap)<N):
            heapq.heappush(heap,t)
        else:
            if(heap[0]<t):
                heapq.heappop(heap)
                heapq.heappush(heap,t)

print(heapq.heappop(heap))

