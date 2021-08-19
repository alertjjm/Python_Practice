# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    leafSet=set([i for i in range(1,X+1)])
    for i in range(len(A)):
        if(A[i] in leafSet):
            leafSet.remove(A[i])
        if(len(leafSet)==0):
            return i
    return -1
print(solution(5, [1,3,1,4,2,3,5,4]))
print(solution(5, [1,3,1,4,2,3,5,4]))
