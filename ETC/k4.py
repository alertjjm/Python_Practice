from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)
result=999999999999999999999999
def bfs(s,c,end,graph,traps):
    global result
    point,cost=s,c
    if (point == end):
        result=min(result,cost)
    elif(cost<result):
        if (point in traps):
            gr=deepcopy(graph)
            for p in gr[point]:
                if (p[2] == True):
                    p[2] = False
                    for q in gr[p[0]]:
                        if (q[0] == point):
                            if (q[2] == False):
                                q[2] = True
                            else:
                                q[2] = False
                else:
                    p[2] = True
                    for q in gr[p[0]]:
                        if (q[0] == point):
                            if (q[2] == False):
                                q[2] = True
                            else:
                                q[2] = False
            for p in gr[point]:
                if (p[2]):
                    to, cos = p[0], p[1]
                    bfs(to, cost + cos,end, gr, traps)
        else:
            for p in graph[point]:
                if (p[2]):
                    to, cos = p[0], p[1]
                    bfs(to,cost+cos,end,graph,traps)

def solution(n, start, end, roads, traps):
    global result
    graph=[[] for i in range(n+1)]
    for road in roads:
        P,Q,S=road
        graph[P].append([Q,S,True])
        graph[Q].append([P,S,False])
    bfs(start,0,end,graph,traps)
    return result
print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3]))
print(solution(4,1,4,[[1, 2, 1],[2,1,1], [3, 2, 1], [2, 4, 1]],[2, 3]))