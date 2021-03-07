M,N=map(int,input().split())
dplist=[True for i in range(1000001)]
primes=[]
for i in range(2,N+1):
    if dplist[i]:
        if(M<=i<=N):
            primes.append(i)
        for j in range(2*i,N+1,i):
            dplist[j]=False
for prime in primes:
    print(prime)
