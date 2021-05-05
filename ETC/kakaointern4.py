dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dp(bd,x,y,ex,ey,pdx,pdy,mny,result):
    if(x==ex and y==ey):
        if(mny<result[0]):
            result[0]=mny
    else:
        for i in range(len(dx)):
            nextxpos=x+dx[i]
            nextypos=y+dy[i]
            if(0<=nextxpos<len(bd) and 0<=nextypos<len(bd) and bd[nextypos][nextxpos]==0):
                bd[nextypos][nextxpos]=2
                if((dx[i]==pdx and dy[i]==pdy) or (pdx==0 and pdy==0)):
                    dp(bd,nextxpos,nextypos,ex,ey,dx[i],dy[i],mny+100,result)
                else:
                    dp(bd,nextxpos,nextypos,ex,ey,dx[i],dy[i],mny+600,result)
                bd[nextypos][nextxpos]=0
def solution(board):
    end=[len(board)-1,len(board)-1]
    answerlist=[650*len(board)*len(board)]
    dp(board,0,0,end[0],end[1],0,0,0,answerlist)
    return answerlist[0]

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))