N=int(input())
#case 0: x, case 1: l, case 2: r
n=1
r=1
l=1
pn=1
pr=1
pl=1
for i in range(1,N):
    n=pn+pl+pr
    l=pn+pr
    r=pn+pl
    pn=n
    pl=l
    pr=r
print((n+l+r)%9901)