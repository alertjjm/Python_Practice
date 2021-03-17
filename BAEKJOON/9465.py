import sys
T=int(input())
result=[]
for i in range(T):
    n=int(input())
    stickers=[]
    stickers.append(list(map(int,sys.stdin.readline().split())))
    stickers.append(list(map(int,sys.stdin.readline().split())))
    dplist=[[0 for _ in range(len(stickers[0]))] for z in range(2)]
    dplist[0][0]=stickers[0][0]
    dplist[1][0]=stickers[1][0]
    dplist[0][1]=stickers[0][1]+dplist[1][0]
    dplist[1][1]=stickers[1][1]+dplist[0][0]
    for k in range(2,len(stickers[0])):
        dplist[0][k]=max(dplist[1][k-1]+stickers[0][k],dplist[1][k-2]+stickers[0][k])
        dplist[1][k]=max(dplist[0][k-1]+stickers[1][k],dplist[0][k-2]+stickers[1][k])
    result.append(max(dplist[0][n-1],dplist[1][n-1]))
for r in result:
    print(r)