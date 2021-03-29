import sys
N,M=map(int,input().split())
parents=[i for i in range(N+1)]
def find(u):
    if(parents[u]!=u):
        return find(parents[u])
    return u
def union(u,v):
    global parents
    a=find(u)
    b=find(v)
    if(a<b):
        parents[b]=a
    else:
        parents[a]=b
edges=[]
for i in range(M):
    A,B,C=map(int,sys.stdin.readline().split())
    edges.append([A,B,C])
edges.sort(key=lambda x:x[2])
result=[]
for edge in edges:
    a,b,v=edge
    if(find(a)!=find(b)):
        union(a,b)
        result.append(v)
print(sum(result)-max(result))