N=int(input())
result=[]
def dp(m, visited, relations):
    first=-1
    for i in range(len(visited)):
        if(visited[i]==0):
            first=i
            break;
    if(first==-1):
        return 1
    count=0
    for i in range(first,m):
        if(visited[i]==0 and relations[first][i]==1):
            visited[i]=1
            visited[first]=1
            count=count+dp(m,visited,relations)
            visited[first]=0
            visited[i]=0
    return count


for i in range(N):
    n,m=map(int, input().split(" "))
    relations=[[0 for i in range(n)] for j in range(n)]
    visited = [0 for i in range(n)]
    temp=list(map(int,input().split(" ")))
    pairlist=[]
    for j in range(len(temp)//2):
        pairlist.append([temp[2*j],temp[2*j+1]])
    for pair in pairlist:
        relations[pair[0]][pair[1]]=1
        relations[pair[1]][pair[0]]=1
    result.append(dp(n,visited,relations))
for i in result:
    print(i)