def solution(A):
    intSet = set([i for i in range(1,len(A)+2)])
    for a in A:
        intSet.remove(a)
    return intSet.pop()