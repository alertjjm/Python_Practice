N=int(input())
edges=[]
cities=[]

for i in range(N):
    fromCity,toCity,resource=input().split()
    resource=int(resource)
    if(fromCity in cities):
        fnum=cities.index(fromCity)
    else:
        cities.append(fromCity)
        fnum=cities.index(fromCity)
    if(toCity in cities):
        tnum=cities.index(toCity)
    else:
        cities.append(toCity)
        tnum=cities.index(toCity)
    edges.append([resource,fnum,tnum])
parents=[i for i in range(len(cities))]
edges.sort(key=lambda x:x[0])
answer=0
def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return x
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
for edge in edges:
    cost,f, t = edge
    if (find(parents, f) != find(parents, t)):
        answer += cost
        union(parents, f, t)
print(answer)