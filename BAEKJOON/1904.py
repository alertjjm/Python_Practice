N=int(input())
a,b=0,1
for i in range(N):
    a,b=b%15746,(a+b)%15746
print(b)