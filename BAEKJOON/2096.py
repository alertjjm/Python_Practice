import sys
N=int(input())
prev=list(map(int, sys.stdin.readline().split()))
now=list()
prevdp=[i for i in prev]
nextdp=[0]*3
minprevdp=[i for i in prev]
minnextdp=[0]*3
for i in range(N-1):
    now=list(map(int, sys.stdin.readline().split()))
    nextdp[0]=max(prevdp[0],prevdp[1])+now[0]
    nextdp[1]=max(prevdp[0],prevdp[1],prevdp[2])+now[1]
    nextdp[2]=max(prevdp[1],prevdp[2])+now[2]
    temp=nextdp
    nextdp=prevdp
    prevdp=temp
    minnextdp[0]=min(minprevdp[0],minprevdp[1])+now[0]
    minnextdp[1]=min(minprevdp[0],minprevdp[1],minprevdp[2])+now[1]
    minnextdp[2]=min(minprevdp[1],minprevdp[2])+now[2]
    temp=minnextdp
    minnextdp=minprevdp
    minprevdp=temp
print(max(prevdp))
print(min(minprevdp))
