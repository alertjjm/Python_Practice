from math import gcd
N=int(input())
nnums=list(map(int,input().split()))
nmul=1
for i in nnums:
    nmul*=i
M=int(input())
mnums=list(map(int,input().split()))
mmul=1
for i in mnums:
    mmul*=i
result=str(gcd(nmul,mmul))
if(len(result)>9):
    print(result[-9:])
else:
    print(result)