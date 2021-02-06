n=int(input())
dplist= {0:0,1:1,2:2}
def squareNum(num):
    for i in range(1,num+1):
        j=1
        min=i
        while j*j<=i:
            temp=1+dplist[i-j*j]
            if min>temp:
                min=temp
            j+=1
        dplist[i]=min
squareNum(n)
print(dplist[n])