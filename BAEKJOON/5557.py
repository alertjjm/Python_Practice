N=int(input())
numbers=list(map(int,input().split()))
dp=[[0]*21 for i in range(N-1)]
dp[0][numbers[0]]=1
for i in range(1,N-1):
    for j in range(21):
        a=j-numbers[i]
        b=j+numbers[i]
        if(0<=a<=20):
            dp[i][j]+=dp[i-1][j-numbers[i]]
        if(0<=b<=20):
            dp[i][j]+= dp[i - 1][j +numbers[i]]
print(dp[N-2][numbers[-1]])

'''N=int(input())
numbers=list(map(int,input().split()))
def dp(exp,result):
    if(len(exp)==1):
        if(exp[0]==result):
            return 1
        else:
            return 0
    a=result+exp[-1]
    b=result-exp[-1]
    answer=0
    if(a<=20):
        answer+=dp(exp[:-1],a)
    if(b>=0):
        answer+=dp(exp[:-1],b)
    return answer
print(dp(numbers[:-1],numbers[-1]))'''