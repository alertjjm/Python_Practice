from functools import cmp_to_key
T=int(input())
result=[]
for test in range(T):
    N,M=map(int, input().split(' '))
    orderlist=[]
    for i in range(M):
        start,end=map(int, input().split(' '))
        orderlist.append([start,end])
    def compare(a,b):
        if(a[1]<b[1]):
            return 1
        elif(a[1]>b[1]):
            return -1
        else:
            if(a[0]>b[0]):
                return 1
            elif(a[0]<b[0]):
                return -1
            else:
                return 0

    orderlist = sorted(orderlist, key=cmp_to_key(compare),reverse=True)
    cnt=0
    booklist=[0 for i in range(N+1)]
    for order in orderlist:
        for i in range(order[0],order[1]+1):
            if(booklist[i]==0):
                booklist[i]=1
                cnt+=1
                break
    result.append(cnt)
for c in result:
    print(c)

