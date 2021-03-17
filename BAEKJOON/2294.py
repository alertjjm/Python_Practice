n,k=map(int,input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))
dplist=[999999 for i in range(k+1)]
dplist[0]=0
for i in range(1, k + 1):
    for coin in coins:
        if(coin<=i):
            dplist[i]=min(dplist[i],dplist[i-coin]+1)
if(dplist[k]==999999):
    print(-1)
else:
    print(dplist[k])