# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if(len(A)==0):
        return 0
    dp=[[0]*2 for _ in range(len(A))]
    dp[0][0]=-A[0]
    dp[0][1]=A[0]
    for i in range(1,len(A)):
        if(abs(dp[i-1][0]-A[i])<abs(dp[i-1][1]-A[i])):
            dp[i][0]=dp[i-1][0]-A[i]
        else:
            dp[i][0]=dp[i - 1][1] - A[i]
        if(abs(dp[i-1][0]+A[i])<abs(dp[i-1][1]+A[i])):
            dp[i][1]=dp[i-1][0]+A[i]
        else:
            dp[i][1]=dp[i - 1][1] + A[i]
    print(dp)
    return abs(min(dp[-1]))
print(solution([1,5,2,-2]))
print(solution([1]))
print(solution([1,5,2,20]))