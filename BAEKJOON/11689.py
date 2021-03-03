N=int(input())
num=N
numlist=[]
su = 2
so = set()
while su <= round(num ** 0.5) + 1:
    if num % su == 0:
        while num % su == 0:
            num //= su
        N=N/su
        N=N*(su-1)
    else:
        su += 1
if(num>1):
    N=N/num
    N=N*(num-1)
print(int(N))