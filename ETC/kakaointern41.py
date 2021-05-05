dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dp(bd,x,y):
    if(bd[y][x]!=1 and bd[y][x]!=0):
        return bd[y][x]
    result=650*len(bd)*len(bd)
    for i in range(len(x)):
        nextxpos = x + dx[i]
        nextypos = y + dy[i]
        if (0 <= nextxpos < len(bd) and 0 <= nextypos < len(bd) and bd[nextypos][nextxpos] != 1):
            if(0 <= nextxpos+dx[i] < len(bd) and 0 <= nextypos+dy[i] < len(bd)):
                temp=dp(bd,nextxpos+dx[i],nextypos+dy[i])+200
            


def solution(board):
    end=[len(board)-1,len(board)-1]
    answerlist=[650*len(board)*len(board)]
    dp(board,end[0],end[1])
    return answerlist[0]

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))