import sys
N,M=map(int,input().split())
numbers=list(map(int,input().split()))
numbers.sort()
result=[]
visited=[0]*(N+1)
def dfs(num,res):
    if num==M:
        print(' '.join(res))
        return
    else:
        for i in range(N):
            if(visited[i]==0):
                visited[i]=1
                res.append(str(numbers[i]))
                dfs(num+1,res)
                res.pop()
                visited[i]=0
dfs(0,[])


