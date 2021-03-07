numlist=[]
n=-1
while(n!=0):
    n=int(input())
    numlist.append(n)
numlist.pop()
dplist=[True for i in range(500000)]
primes=[]
for i in range(2,400001):
    if dplist[i]:
        primes.append(i)
        for j in range(2*i,400001,i):
            dplist[j]=False
for num in numlist:
    temp=dplist[num+1:num*2+1]
    print(temp.count(True))