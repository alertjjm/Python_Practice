from collections import deque
def solution(n, path, order):
    answer = True
    graph=[[] for i in range(n)]
    for a in path:
        graph[a[0]].append(a[1])
        graph[a[1]].append(a[0])
    before={y:x for x,y in order}
    after={x:y for x,y in order}
    visited=[0]*n
    wait=[0]*n
    q=deque()
    q.append(0)
    while(q):
        p=q.popleft()
        if p in before and visited[before[p]]==0 and wait[p]==0:
            wait[p]=1
            continue
        elif p in after:
            if(wait[after[p]]==1):
                q.append(after[p])
        for i in graph[p]:
            if visited[i]==0:
                q.append(i)
        visited[p]=1
    return True if sum(visited)==n else False

print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[8,5],[6,7],[4,1]]))
print(solution(9,[[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]],[[4,1],[5,2]]))
print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[4,1],[8,7],[6,5]]))