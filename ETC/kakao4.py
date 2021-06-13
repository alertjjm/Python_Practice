from collections import deque
def solution(n, start, end, roads, traps):
    graph=[[] for i in range(n+1)]
    for road in roads:
        P,Q,S=road
        graph[P].append([Q,S,True])
        graph[Q].append([P,S,False])
    que=deque()
    que.append([start,0])
    result=-1
    while que:
        point,cost=que.popleft()
        if(point==end):
            if(result==-1):
                result=cost
            else:
                result=min(result,cost)
        else:
            if(result!=-1 and cost>=result):
                continue
            if(point in traps):
                for p in graph[point]:
                    if(p[2]==True):
                        p[2]=False
                        for q in graph[p[0]]:
                            if(q[0]==point):
                                if(q[2]==False):
                                    q[2]=True
                                else:
                                    q[2]=False
                    else:
                        p[2] = True
                        for q in graph[p[0]]:
                            if (q[0] == point):
                                if (q[2] == False):
                                    q[2] = True
                                else:
                                    q[2] = False
            for p in graph[point]:
                if(p[2]):
                    to,c=p[0],p[1]
                    que.append([to,cost+c])
    return result

print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3]))
print(solution(4,1,4,[[1, 2, 1],[2,1,1], [3, 2, 1], [2, 4, 1]],[2, 3]))