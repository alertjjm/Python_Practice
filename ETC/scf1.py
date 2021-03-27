N,time=input().split()
N=int(N)
time=list(map(int,time.split(':')))
time=time[0]*3600+time[1]*60+time[2]
musiclist=[]
for i in range(N):
    minute,second=map(int,input().split(':'))
    musiclist.append(minute*60+second)
result=0
resultidx=-1
for i in range(N):
    cnt=0
    sumtime=0
    for j in range(i,N):
        sumtime+=musiclist[j]
        cnt+=1
        if(sumtime>=time):
            if(cnt>result):
                result=cnt
                resultidx=i+1
            break
print(result,resultidx)
