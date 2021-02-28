###20번###
T=int(input())
numbers=[]
maxnum=0
initlist=[0,1,2,4,7]
for i in range(T):
    n=int(input())
    numbers.append(n)
    if(n>maxnum):
        maxnum=n
if(maxnum<=4):
    for num in numbers:
        print(initlist[num])
else:
    dplist=[0 for i in range(maxnum+1)]
    dplist[1]=1 #1
    dplist[2]=2 #1+1, 2
    dplist[3]=4 #1+1+1 1+2 2+1 3
    dplist[4]=7 #1+1+1+1 1+1+2 1+2+1 2+1+1 2+2 1+3 3+1
    for i in range(4, maxnum+1):
        dplist[i]=dplist[i-3]+dplist[i-2]+dplist[i-1]
    for num in numbers:
        print(dplist[num])