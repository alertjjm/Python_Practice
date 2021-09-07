answer = 10**9
enterVal = [-1,-1,-1]
dr=[1,-1,0,0]
dc=[0,0,-1,1]
def isCompleted(board):
    status=True
    for row in board:
        for item in row:
            if(item!=0):
                return False
    return status
def isAvailable(r,c,l):
    if (0 <= r < l and 0 <= c < l):
        return True
    else:
        return False
def availableCtrl(r,c, board):
    baser, basec=r,c
    result =[]
    for l in range(len(dr)):
        while True:
            nextr = r + dr[l]
            nextc = c + dc[l]
            if (nextr < 0 or nextr >= len(board) or nextc < 0 or nextc >= len(board)):
                if(baser!=r and basec!=c):
                    result.append([r,c])
                break
            else:
                if(board[nextr][nextc]!=0):
                    result.append([nextr, nextc])
                    break
                r,c=nextr,nextc
    print(result)
    return result

def dfs(row, col, board, visited, mov):
    global answer
    global enterVal
    #이동회수가 정답보다 커지면 break
    if(mov>=answer):
        return
    # 다찾으면 answer min 업뎃
    if(isCompleted(board)):
        answer=min(answer,mov)
        return
    #현재위치에 카드가 있으면 엔터눌러보기 또는 무시
    if(board[row][col]!=0):
        if(enterVal[2]==-1):
            enterVal=[row,col,board[row][col]]
            dfs(row, col, board, visited, mov+1)
        elif(enterVal[2]==board[row][col]):
            r,c,v=enterVal
            if(not (r==row and c==col)):
                board[r][c]=0
                board[row][col]=0
                dfs(row, col, board, visited, mov+1)
                board[r][c]=v
                board[row][col]=v
    #위아래좌우
    for l in range(len(dr)):
        nextr=row+dr[l]
        nextc=col+dc[l]
        if(isAvailable(nextr, nextc, len(board)) and visited[nextr][nextc]==0):
            visited[nextr][nextc]=1
            dfs(nextr, nextc, board, visited, mov+1)
            visited[nextr][nextc]=0
    #ctrl 위아래좌우
    dirs=availableCtrl(row, col, board)
    for d in dirs:
        nextr, nextc=d
        if(visited[nextr][nextc]==0):
            visited[nextr][nextc]=1
            dfs(nextr, nextc, board, visited, mov+1)
            visited[nextr][nextc]=0
def solution(board, r, c):
    global answer
    l=len(board)
    visited=[[0]*l for _ in range(l)]
    visited[r][c]=1
    dfs(r,c, board, visited, 0)
    return answer


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
