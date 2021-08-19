def solution(N):
    status = False
    maxcount = 0
    count = 0
    while (N != 0):
        rest = N % 2
        if (rest == 0 and status):
            count += 1
        elif (rest == 1):
            status = True
            maxcount = max(count, maxcount)
            count = 0
        N = N // 2
    return maxcount


print(solution(9))
print(solution(529))
print(solution(20))
print(solution(15))
print(solution(32))
