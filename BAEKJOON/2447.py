pic=["***","* *","***"]
def recur(n):
    if(n==3):
        return ["***","* *","***"]
    else:
        pic2=recur(n//3)
        pic2=pic2+pic2+pic2
        num=len(pic2)//3
        temp=pic2
        for i in range(num):
            pic2[i]=pic2[i]*3
        for i in range(num,2*num):
            pic2[i]=pic2[i]+" "*num+pic2[i]
        for i in range(2*num, 3*num):
            pic2[i]=pic2[i]*3
        return pic2
n=int(input())
temp=recur(n)
for i in temp:
    print(i)
