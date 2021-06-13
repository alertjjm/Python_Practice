def isDistant(place):
    L=5
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for i in range(L):
        for j in range(L):
            if(place[i][j]=='P'):
                visited = [[0] * L for i in range(L)]
                stack=[]
                stack.append([i,j,i,j])
                visited[i][j]=1
                while stack:
                    y,x,checky,checkx=stack.pop()
                    for d in range(len(dx)):
                        nexty=y+dy[d]
                        nextx=x+dx[d]
                        if(0<=nexty<L and 0<=nextx<L and visited[nexty][nextx]==0 and place[nexty][nextx]!='X'):
                            if(place[nexty][nextx]=='P'):
                                if (abs(checky - nexty) + abs(checkx - nextx) <= 2):
                                    if(place[(checky+nexty)//2][(checkx+nextx)//2]!='X'):
                                        return False
                            else:
                                visited[nexty][nextx]=1
                                stack.append([nexty,nextx,checky,checkx])
    return True
def solution(places):
    answer = []
    for place in places:
        if(isDistant(place)):
            answer.append(1)
        else:
            answer.append(0)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
                ["XPXPX", "PXPXP", "XPXPX", "PXPXP","XPXPX"],
                ["OOPOO",
                 "OOXOO",
                 "OOPOO",
                 "OOOOO",
                 "OOOOO"]
                ]))

