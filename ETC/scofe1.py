N=int(input())
starts=[]
ends=[]
for i in range(N):
    start,end=input().split(" ~ ")
    start=int(start[:2])*60+int(start[3:])
    end=int(end[:2])*60+int(end[3:])
    starts.append(start)
    ends.append(end)
starts.sort()
ends.sort()
start=starts.pop()
end=ends[0]
if(end<=start):
    print(-1)
else:
    start=str(start//60).zfill(2)+":"+str(start%60).zfill(2)
    end=str(end//60).zfill(2)+":"+str(end%60).zfill(2)
    print(start+" ~ "+end)