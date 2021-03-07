width='IABCDEFGH'
king,dol,N=input().split()
king_x=width.index(king[0])
king_y=int(king[1])
dol_x=width.index(dol[0])
dol_y=int(dol[1])
N=int(N)
###############
acts=[]
for i in range(N):
    act=input()
    if(act=="R"):
        nextx=king_x+1
        nexty=king_y
    elif(act=="L"):
        nextx=king_x-1
        nexty=king_y
    elif (act == "B"):
        nextx = king_x
        nexty = king_y-1
    elif(act=="T"):
        nextx=king_x
        nexty=king_y+1
    elif (act == "RT"):
        nextx=king_x+1
        nexty=king_y+1
    elif(act=="LT"):
        nextx = king_x -1
        nexty = king_y+1
    elif (act == "RB"):
        nextx = king_x + 1
        nexty = king_y-1
    elif (act == "LB"):
        nextx = king_x -1
        nexty = king_y-1
    if(1<=nextx<=8 and 1<=nexty<=8):
        dx=nextx-king_x
        dy=nexty-king_y
        if(nextx==dol_x and nexty==dol_y):
            if(1<=dol_x+dx<=8 and 1<=dol_y+dy<=8):
                dol_x = dol_x + dx
                dol_y = dol_y + dy
            else:
                continue
        king_x = nextx
        king_y = nexty
print(width[king_x]+str(king_y))
print(width[dol_x]+str(dol_y))
