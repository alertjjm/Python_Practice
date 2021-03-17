n,k=map(int,input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))
dplist=[0 for i in range(k+1)]
dplist[0]=1

for coin in coins:
    for i in range(1, k + 1):
        if(coin<=i):
            dplist[i]+=dplist[i-coin]
print(dplist[k])