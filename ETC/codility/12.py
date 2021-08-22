# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque
def solution(K,A):
    Aq=deque(A)
    cnt=0
    while Aq:
        left=Aq.popleft()
        if(left>=K):
            cnt+=1
        else:
            if(len(Aq)==0):
                return cnt
            right=Aq.popleft()
            newLeft=left+right
            if(newLeft>=K):
                cnt+=1
            else:
                Aq.appendleft(newLeft)
    return cnt
print(solution(4,[1,2,3,4,1,1,3,1,1]))
print(solution(4,[1,2,3,4,1,1,3,1,1,1,1]))