import sys
N=int(input())
points=[]
xsum=0
ysum=0
for i in range(N):
    x,y=map(int,sys.stdin.readline().rstrip().split())
    points.append([x,y])
    xsum+=x
    ysum+=y
middlex,middley=points[0]
area=0.0
for i in range(0,N-1):
    a,b=points[i]
    c,d=points[i+1]
    e,f=middlex,middley
    area+=((b-d)*(e-c)-(a-c)*(f-d))/2
area=abs(area)
area=int(area*10)
print(area/10)