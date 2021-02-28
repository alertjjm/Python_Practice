####9분####
T=int(input())
init=[[1,0],[0,1],[1,1],[1,2]]
numbers=[]
maxnum=0
for i in range(T):
    n=int(input())
    numbers.append(n)
    if(maxnum<n):
        maxnum=n
if(maxnum<=3):
    for n in numbers:
        print(str(init[n][0])+" "+str(init[n][1]))
else:
    memoization=init+[[0,0] for i in range(maxnum)]
    for i in range(4,maxnum+1):
        memoization[i][0]=memoization[i-1][0]+memoization[i-2][0]
        memoization[i][1] = memoization[i - 1][1] + memoization[i - 2][1]
    for n in numbers:
        print(str(memoization[n][0])+" "+str(memoization[n][1]))