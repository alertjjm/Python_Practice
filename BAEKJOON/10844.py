DIV= 1000000000
N=int(input())
dplist=[[0 for i in range(10)] for j in range(N+1)]
dplist[1]=[1 for i in range(10)]
dplist[1][0]=0
for i in range(2,N+1):
    for j in range(10):
        if (j==0):
            dplist[i][j] += dplist[i-1][1] % DIV
        elif (j==9):
            dplist[i][j] += dplist[i-1][8] % DIV
        else:
            dplist[i][j] += (dplist[i-1][j-1]+dplist[i-1][j+1]) %DIV
print(sum(dplist[N])%DIV)

