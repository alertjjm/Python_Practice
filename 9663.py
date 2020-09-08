n=int(input())
row=[-1]*n
result=0
def iscaught(x):
    for i in range(x):
        if(row[x]==row[i] or abs(row[x]-row[i])==abs(x-i)):
            return False
    return True

def dfs(x):
    global result
    if x==n:
        result+=1
    else:
        for i in range(n):
            row[x]=i
            if(iscaught(x)):
                dfs(x+1)

dfs(0)
print(result)