t=int(input())
for i in range(t):
    n=int(input())
    sample=list(map(int,input().split()))
    m=sum(sample)%max(sample)
    for j in range(m,-1,-1):
        if(sample[0]<sample[1]):
            c=sample[1]-sample[0]


