import heapq
INF=99999
V,E=map(int,input().split(' '))
K=int(input())
graphs=[[INF for i in range(V+1)] for j in range(V+1)]
visited=[False for i in range(V+1)]
distance=[INF for i in range(V+1)]
for i in range(E):
    u,va,w=map(int,input().split(' '))
    graphs[u][va]=w
q=[]
distance[K]=0
heapq.heappush(q,[distance[K],K])
distance[K]=0
while q:
    dis,idx=heapq.heappop(q)
    if (distance[idx] < dis):
        continue
    for w in range(V+1):
        if(distance[idx]+graphs[idx][w]<distance[w]):
            distance[w]=distance[idx]+graphs[idx][w]
            heapq.heappush(q,[distance[w],w])
for i in range(1,V+1):
    if(distance[i]==INF):
        print('INF')
    else:
        print(i)