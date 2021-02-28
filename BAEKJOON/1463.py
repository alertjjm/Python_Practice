########[6분]########
N=int(input())
#memoization
#1 0
#2 1
#3 1
#4 2
memoization=[0,0,1,1]
if(N<=3):
    print(memoization[N])
else:
    memoization=[0 for i in range(N+1)]
    memoization[1]=0
    memoization[2]=1
    memoization[3]=1
    for i in range(4, N+1):
        result=[]
        if(i%3==0):
            result.append(memoization[i//3]+1)
        if(i%2==0):
            result.append(memoization[i//2]+1)
        result.append(memoization[i-1]+1)
        memoization[i]=min(result)
    print(memoization[N])