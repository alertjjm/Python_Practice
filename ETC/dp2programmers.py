def solution(m, n, puddles):
    map1= [[20000]*m for _ in range(n)]
    map1[0][0]=0
    for i in range(n):
        for j in range(m):
            if [i+1,j+1] in puddles:
                map1[i][j]=30000
            else:
                if(i-1>=0):
                    if(map1[i][j]>map1[i-1][j]+1):
                        map1[i][j]=map1[i-1][j]+1
                if(j-1>=0):
                    if(map1[i][j]>map1[i][j-1]+1):
                        map1[i][j]=map1[i][j-1]+1
    cnt=0
    backtrack=[]
    backtrack.append([n-1,m-1])
    while(cnt!=len(backtrack)-1 or cnt==0):
        ty,tx=backtrack[cnt]
        if(ty==0 and tx==0):
            cnt+=1
            continue
        del backtrack[cnt]
        if (ty - 1 >= 0):
            if(map1[ty-1][tx]==map1[ty][tx]-1):
                backtrack.append([ty-1,tx])
        if (tx - 1 >= 0):
            if(map1[ty][tx-1]==map1[ty][tx]-1):
                backtrack.append([ty,tx-1])
    for i in map1:
        print(i)
    return cnt+1
print(solution(4,3,[[1, 3], [3, 1]] ))