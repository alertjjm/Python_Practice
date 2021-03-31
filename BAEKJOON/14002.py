N=int(input())
A=list(map(int,input().split(' ')))
dplist=[1 for i in range(N+1)]
answer=[i for i in range(N+1)]
for i in range(N):
    mini=0
    for j in range(i):
        if(A[i]>A[j]):
            if(dplist[i]<dplist[j]+1):
                dplist[i]=dplist[j]+1
                answer[i]=j
print(max(dplist))
start=dplist.index(max(dplist))
def backtrack(n):
    if(n==answer[n]):
        print(A[n],end=' ')
        return
    backtrack(answer[n])
    print(A[n],end=' ')
backtrack(start)