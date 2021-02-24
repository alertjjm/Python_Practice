T=int(input())
cases=[25,10,5,1]
resultlist=[]
for i in range(T):
    result=""
    money=int(input())
    for case in cases:
        count=money//case
        money=money%case
        result+=str(count)+" "
    resultlist.append(result[:-1])
for i in resultlist:
    print(i)