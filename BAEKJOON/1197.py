N,E=map(int,input().split())
edges=[]
vectors=[i for i in range(10000)]
def find(u):
    if(u==vectors[u]):
        return u
    vectors[u]=find(vectors[u])
    return vectors[u]
def union(u,v):
    u=find(u)
    v=find(v)
    vectors[v]=u
for i in range(E):
    temp=list(map(int,input().split()))
    edges.append([temp[2],temp[0]-1,temp[1]-1])
edges.sort(key=lambda x:x[0])
L=len(edges)
result=0
cnt=0
for i in range(L):
    value,y,x=edges[i]
    if(find(y)!=find(x)):
        result+=value
        cnt+=1
        union(y,x)
    if(cnt==N-1):
        break
print(result)