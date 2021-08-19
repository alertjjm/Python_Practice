from collections import deque
def solution(A, K):
    # write your code in Python 3.6
    if(len(A)==0):
        return A
    Aq=deque(A)
    for i in range(K):
        item=Aq.pop()
        Aq.appendleft(item)
    return list(Aq)

print(solution([3, 8, 9, 7, 6], 3))
print(solution([0,0,0],1))
print(solution([1,2,3,4],4))
print(solution([1],4))
print(solution([],4))