import sys
sys.setrecursionlimit(10**6)
N=9
sudoku=[[] for j in range(N)]
zerolist = []  # x,y
for i in range(N):
    sudoku[i]=list(map(int, sys.stdin.readline().split()))
for i in range(N):
    for j in range(N):
        if(sudoku[i][j]==0):
            zerolist.append([j, i])
flag=False
def recursive(idx):
    global sudoku
    global zerolist
    global flag
    if(flag):
        return
    if(len(zerolist)==idx):
        for i in range(N): #y
            if(0 in sudoku[i]):
                return
        for line in sudoku:
            for item in line:
                print(item,end=' ')
            print()
        flag=True
        return
    x,y=zerolist[idx]
    startx=(x//3)*3
    endx=startx+3
    starty=(y//3)*3
    endy=starty+3
    numlist=[1,2,3,4,5,6,7,8,9]
    for i in range(startx,endx):
        for j in range(starty,endy):
            item=sudoku[j][i]
            if item in numlist:
                numlist.remove(item)
    for i in range(N):
        item1=sudoku[y][i]
        item2=sudoku[i][x]
        if item1 in numlist:
            numlist.remove(item1)
        if item2 in numlist:
            numlist.remove(item2)
    if(len(numlist)==0):
        return
    for num in numlist:
        sudoku[y][x]=num
        recursive(idx+1)
        sudoku[y][x]=0
recursive(0)

