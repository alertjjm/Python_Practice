def solution(A):
    N = len(A)
    answer = [A[0]] * (N + 6)

    for i in range(1, N):
        answer[i + 6] = max(answer[i : i + 6]) + A[i]

    return answer[-1]
print(solution([1,-2,0,9,-1,-2]))
print(solution([1,-2,0,9,-1,-2, 5,-5,5]))
print(solution([1,2,3,4,5,6,7,8,9,10,11]))
print(solution([1,2,3]))
print(solution([-1,2]))
print(solution([1,-2]))