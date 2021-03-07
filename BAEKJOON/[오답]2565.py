N=int(input())
dplist=[1 for i in range(N)]
lines=[]
for i in range(N):
    a,b=map(int,input().split())
    lines.append([a,b])
lines.sort(key=lambda x:x[0])
for i in range(N):
    for j in range(i):
        if(lines[i][1]>lines[j][1] and dplist[i]<dplist[j]+1):
            dplist[i]=dplist[j]+1
print(N-max(dplist))