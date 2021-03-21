T=int(input())
result=[]
for i in range(T):
    a,b=map(int,input().split())
    result.append(a*b)
for r in result:
    print(r)