R,C=map(int,input().split())
board=[]
for i in range(R):
    board.append(list(input()))
dirx=[0,0,-1,1]
diry=[-1,1,0,0]
alpha=[False]*30
result=0
def dfs(y,x,depth):
    global result
    result=max(result,depth)
    for i in range(len(dirx)):
        ypos=y+diry[i]
        xpos=x+dirx[i]
        if(0<=ypos<R and 0<=xpos<C and alpha[ord(board[ypos][xpos])-ord('A')]==False):
            alpha[ord(board[ypos][xpos])-ord('A')]=True
            dfs(ypos,xpos,depth+1)
            alpha[ord(board[ypos][xpos]) - ord('A')] = False
alpha[ord(board[0][0])-ord('A')]=True
dfs(0,0,1)
print(result)