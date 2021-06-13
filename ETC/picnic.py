C=int(input())
def friendrecur(visited,isfriend):
    if(False not in visited):
        return 1
    cnt=0
    for i in range(len(visited)):
        if(not visited[i]):
            break
    for j in range(i+1,len(visited)):
        if((not visited[i]) and (not visited[j]) and isfriend[i][j]):
            visited[i]=True
            visited[j]=True
            cnt+=friendrecur(visited,isfriend)
            visited[i]=False
            visited[j]=False
    return cnt
for i in range(C):
    n,m=map(int,input().split())
    isfriend=[[False]*n for _ in range(n)]
    friendlist=list(map(int,input().split()))
    for j in range(m):
        f1,f2=friendlist[2*j],friendlist[2*j+1]
        isfriend[f1][f2]=True
        isfriend[f2][f1]=True
    visited=[False]*n
    print(friendrecur(visited,isfriend))