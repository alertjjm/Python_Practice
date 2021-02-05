import sys
N,M,K=map(int, input().split())
caseresult=[]
for i in range(N):
    caseresult.append(int(sys.stdin.readline().rstrip()))
result=[]
for i  in range(M+K):
    a,b,c=map(int, sys.stdin.readline().rstrip())
    if(a==1):
        caseresult[b-1]=c
    elif(a==2):
        sum=0
        for j in range(b-1,c):
            sum+=caseresult[j]
        result.append(sum)
for i in result:
    print(i)