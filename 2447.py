pic=["***","* *","***"]
def recur(p,n):
    if(n==3):
        return p
    else:
        pic2=recur(p,)
        for i in range(len(pic)):
            pic[i]=pic[i]*3
        temp=[]
        for i in range(len(pic)):



pic=recur(pic,3)
for i in range(3):
    print(pic[i])