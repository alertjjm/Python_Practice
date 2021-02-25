G=int(input())
P=int(input())
planes=[]
ports=[i for i in range(G+1)]
def find(u):
    if(u==ports[u]):
        return u
    ports[u]=find(ports[u])
    return ports[u]
def union(u,v):
    u=find(u)
    v=find(v)
    ports[u]=v
for i in range(P):
    planes.append(int(input()))
cnt=0
for plane in planes:
    idx=find(plane)
    if(idx==0):
        break
    else:
        union(idx,idx-1)
        cnt+=1
print(cnt)