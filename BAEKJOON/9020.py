T=int(input())
N=10001
numlist=[]
for i in range(T):
    numlist.append(int(input()))
dplist=[True for i in range(N)]
primes=[]
for i in range(2,N):
    if dplist[i]:
        primes.append(i)
        for j in range(2*i,N,i):
            dplist[j]=False
def partition(n):
    a=-1
    b=n+1
    idx=0
    item=primes[idx]
    while item<n:
        if(n-item in primes and abs(item*2-n)<abs(a-b)):
            a=item
            b=n-item
        idx+=1
        if(idx==len(primes)):
            break
        item=primes[idx]
    print(str(a)+" "+str(b))
for num in numlist:
    partition(num)
