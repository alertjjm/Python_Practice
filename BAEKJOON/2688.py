T=int(input())
cases=[]
def solution(n):
    dplist = [[0 for i in range(10)] for j in range(n+1)]
    for i in range(10):
        dplist[1][i]=1
    for i in range(2,n+1):
        for j in range(10):
            sum=0
            for k in range(j+1):
                sum+=dplist[i-1][k]
            dplist[i][j]=sum
    sum=0
    for i in range(10):
        sum+=dplist[n][i]
    return sum

for i in range(T):
    cases.append(int(input()))
for case in cases:
    print(solution(case))
