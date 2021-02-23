N=int(input())
dplist=[0 for i in range(N+1)]
dplist[0]=1
dplist[1]=2
dplist[2]=7
def sol(n):
    if(n==1 or n==2):
        return
    sum=0
    for i in range(3,N+1):
        sum+=dplist[i-3]
        dplist[i]=dplist[i-2]*3+dplist[i-1]*2+sum*2
sol(N)
print(dplist[N]%1000000007)