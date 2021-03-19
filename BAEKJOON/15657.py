N,M=map(int,input().split())
numbers=list(map(int,input().split()))
numbers.sort()
result=[]
def dfs(num,now):
    if num==M:
        result.sort()
        print(' '.join(map(str,result)))
        return
    else:
        for i in range(now,N):
            result.append(str(numbers[i]))
            dfs(num+1,i)
            result.pop()
dfs(0,0)
