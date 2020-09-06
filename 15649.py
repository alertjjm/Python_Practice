n,m=map(int, input().split(" "))
out=[]
visited=[False]*n
a=[0]*m
result=[]
def permu(index, n,m):
    if index==m:
        temp=set(out)
        result.append(' '.join(map(str, temp)))
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i]=True
            out.append(i+1)
            permu(index+1,n,m)
            visited[i]=False
            out.pop()
permu(0,n,m)
result=list(set(result))
result.sort()

for i in result:
    print(i)