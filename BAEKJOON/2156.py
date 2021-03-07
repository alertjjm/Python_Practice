n=int(input())
wines=[]
dplist=[0 for i in range(n+1)]
for i in range(n):
    wines.append(int(input()))
wines=[0]+wines
if(n==1):
    print(wines[1])
elif(n==2):
    print(wines[1]+wines[2])
else:
    dplist[1]=wines[1]
    dplist[2]=wines[1]+wines[2]
    for i in range(3,n+1):
        dplist[i]=max(wines[i]+wines[i-1]+dplist[i-3],wines[i]+dplist[i-2],dplist[i-1])
    print(dplist[n])