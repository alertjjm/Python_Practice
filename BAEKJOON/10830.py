N,B=map(int, input().split(' '))
A=[[] for j in range(N)]
for i in range(N):
    A[i]=list(map(int, input().split(' ')))
memoization=[[] for i in range(B+1)]
memoization[1]=A
dpindex=[]
temp=B
while(temp>0):
    dpindex.append(temp)
    temp=temp//2
dpindex=dpindex[1:]
dpindex.sort()
def dot(X,Y):
    answer = [[0 for _ in range(len(X[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(X[0])):
                answer[i][j] += (X[i][k] * Y[k][j])%1000
    return answer
def dp(matrix,pow):
    for i in dpindex:
        memoization[2*i]=dot(memoization[i],memoization[i])
        memoization[2*i+1]=dot(memoization[2*i],matrix)
    return memoization[pow]
result=dp(A,B)
for line in result:
    for item in line:
        print(item%1000,end=' ')
    print()