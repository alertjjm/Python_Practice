n,m=map(int, input().split(" "))
out=[]
a=[0]*m
result=[]
def permu(start, index, n,m):
    visited = [False] * n
    if index==m:
        result.append(' '.join(map(str, out)))
        return
    for i in range(start, len(visited)):
        if not visited[i]:
            visited[i]=True
            out.append(i+1)
            permu(i,index+1,n,m)
            visited[i]=False
            out.pop()
permu(0, 0,n,m)
for i in result:
    print(i)