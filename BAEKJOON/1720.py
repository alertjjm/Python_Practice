
N=int(input())
def tilenum(n):
    if(n<=1):
        return 1
    return tilenum(n-2)*2+tilenum(n-1)
if(N%2==1):
    print((tilenum(N)+tilenum(N//2))//2)
else:
    print((tilenum(N)+tilenum(N/2)+tilenum(N/2-1)*2)//2)