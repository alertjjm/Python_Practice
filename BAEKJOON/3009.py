xlist={}
ylist={}
for i in range(3):
    x,y=map(int,input().split())
    if(x in xlist):
        xlist[x]+=1
    else:
        xlist[x]=1
    if(y in ylist):
        ylist[y]+=1
    else:
        ylist[y]=1
xkeys=xlist.keys()
ykeys=ylist.keys()
x=-1
y=-1
for key in xkeys:
    if(xlist[key] %2==1):
        x=key
        break
for key in ykeys:
    if(ylist[key] %2==1):
        y=key
        break
print(str(x)+" "+str(y))