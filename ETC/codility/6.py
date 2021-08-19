def solution(A):
    S=0
    minval=1e6
    total = sum(A)
    for i in range(len(A)-1):
        S+=A[i]
        left=S
        right=total-left
        minval=min(minval, abs(left-right))
    return minval
print(solution([3,1,2,4,3]))
print(solution([3,1,2,4,10]))
print(solution([200,0]))
print(solution([0,200]))