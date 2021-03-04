numlist=[]
dplist=[0 for i in range(101)]
dplist[1]=1
dplist[2]=1
dplist[3]=1
dplist[4]=2
dplist[5]=2
for i in range(6,101):
    dplist[i] = dplist[i-1] + dplist[i-5]
T=int(input())
for i in range(T):
    numlist.append(int(input()))
for num in numlist:
    print(dplist[num])