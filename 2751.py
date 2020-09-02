import sys
n=int(input())
tlist=[0]*10000
for i in range(n):
    t=int(sys.stdin.readline())
    tlist[t-1]+=1
for i in range(10000):
    for j in range(tlist[i]):
        sys.stdout.write(str(i+1)+'\n')