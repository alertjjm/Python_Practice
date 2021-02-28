import sys
N,M=map(int,sys.stdin.readline().split())
matrix=[[0 for i in range(N+1)] for j in range(N+1)]
position=[]
dplist=[[0 for i in range(N+1)] for j in range(N+1)]
for i in range(N):
    matrix[i+1]=[0]+list(map(int, sys.stdin.readline().split()))
for i in range(M):
    position.append(list(map(int, sys.stdin.readline().split())))
dplist[1][1]=matrix[1][1]
for i in range(1,N+1):
    for j in range(1,N+1):
        dplist[i][j]=matrix[i][j]+dplist[i-1][j]+dplist[i][j-1]-dplist[i-1][j-1]
result=[]
for pos in position:
    x1,y1,x2,y2=pos
    if(x1==x2 and y1==y2):
        result.append(matrix[x1][y1])
    else:
        result.append(dplist[x2][y2]-dplist[x1-1][y2]-dplist[x2][y1-1]+dplist[x1-1][y1-1])
for r in result:
    print(r)
