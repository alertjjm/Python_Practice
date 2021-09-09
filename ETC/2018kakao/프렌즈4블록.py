def markSweepAndCompact(m,n,board):
    result=0
    erase=[[False]*n for _ in range(m)]
    ##mark
    for i in range(m-1):
        for j in range(n-1):
            val=board[i][j]
            if(val!='0' and board[i][j+1]==val and board[i+1][j]==val and board[i+1][j+1]==val):
                erase[i][j]=True
                erase[i][j+1]=True
                erase[i+1][j]=True
                erase[i+1][j+1]=True
    ##sweep
    for i in range(m):
        for j in range(n):
            if(erase[i][j]):
                result+=1
                board[i][j]='0'
    ##compact
    while True:
        cnt=0
        for i in range(m-1):
            for j in range(n):
                if(board[i+1][j]=='0' and board[i][j]!='0'):
                    cnt+=1
                    board[i+1][j]=board[i][j]
                    board[i][j]='0'
        if(cnt==0):
            break
    return result

def solution(m, n, board):
    answer = 0
    for r in range(m):
        board[r]=list(board[r])
    while True:
        cnt=markSweepAndCompact(m,n,board)
        if(cnt==0):
            break
        else:
            answer+=cnt
    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))