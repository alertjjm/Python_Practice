t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    days=[]
    for j in range(m):
        temp=list(map(int,input().split()))
        days.append(temp[1:])
    print(days)
