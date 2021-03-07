N=int(input())
A=list(map(int, input().split()))
ascdplist=[1 for i in range(N)]
descdplist=[1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if(A[i]>A[j] and ascdplist[i]<ascdplist[j]+1):
            ascdplist[i]=ascdplist[j]+1
for i in range(N-1,-1,-1):
    for j in range(i+1,N):
        if (A[i] > A[j] and descdplist[i] < descdplist[j]+1):
            descdplist[i] = descdplist[j]+1
result=-1
for i in range(N):
    if(result<ascdplist[i]+descdplist[i]-1):
        result=ascdplist[i] + descdplist[i] - 1
print(result)