n=int(input())
chess=[False]*n
chess=[chess]*n
out=[]
c=0
def dfs():
    global chess,c
    for i in range(n):
        for j in range(n):
            #updown
            if(len(out)>n):
                c=c+1
                return
            if(chess[i][j]!=True):
                if([i,j] not in out):
                    out.append([i,j])
                else:
                    return
                t = min(i, j)
                for k in range(n):
                    chess[k][j]=True
                    chess[i][k]=True
                    try:
                        chess[i-t+k][j-t+k]=True
                    except:
                        pass
                    try:
                        chess[0+k][i+j-k]=True
                    except:
                        pass
            else:
                return
            dfs()
            chess = [False] * n
            chess = [chess] * n
dfs()
print(c)