def solution(N, A):
    result={i:0 for i in range(1,N+1)}
    lastMaxIdx=-1
    for i in range(len(A)-1,-1,-1):
        if(A[i]==N+1):
            lastMaxIdx=i
            break
    maxVal=0
    if(lastMaxIdx!=-1):
        for a in range(lastMaxIdx):
            if(A[a]!=N+1):
                result[A[a]]+=1
                maxVal=max(maxVal, result[A[a]])
        answer=[maxVal]*N
    else:
        answer=[0]*N
    for a in range(lastMaxIdx+1,len(A)):
        answer[A[a]-1]+=1
    return answer
print(solution(5, [3,4,4,6,1,4,4]))
print(solution(5, [3,4,4,6,1,4,6]))
print(solution(5, [3,4,4,1,1,4,1]))
print(solution(5, [6,6,6,6,6,6,6]))
