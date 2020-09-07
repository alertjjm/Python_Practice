n,m=map(int, input().split(" "))
out=[]
a=[0]*m
result=[]
def permu(index, n,m):
    visited = [False] * n
    if index==m:
        result.append(' '.join(map(str, out)))
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i]=True
            out.append(i+1)
            permu(index+1,n,m)
            visited[i]=False
            out.pop()
permu(0,n,m)
for i in result:
    print(i)