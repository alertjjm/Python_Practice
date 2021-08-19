def solution(A):
    inputDict=set()
    for item in A:
        if item in inputDict:
            inputDict.remove(item)
        else:
            inputDict.add(item)
    return inputDict.pop()
print(solution([9,3,9,3,9,7,9]))