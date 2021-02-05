import math
N,M=map(int, input().split(" "))
grid=[]
for i in range(N):
    tempgrid=input()
    tempgrid=[int(d) for d in tempgrid]
    grid.append(tempgrid)
result=-1
for n in range(N):
    for m in range(M):
        for n_d in range(-N,N):
            for m_d in range(-M,M):
                num=""
                if(n_d==0 and m_d==0):
                    continue
                r=n
                c=m
                while(0<=r<N and 0<=c<M):
                    num+=str(grid[r][c])
                    r+=n_d
                    c+=m_d
                    number=int(num)
                    tempnum=int(math.sqrt(number))
                    if(number==tempnum*tempnum):
                        if(number>result):
                            result=number
print(result)