n=int(input())
temp=input()
temp=list(map(int, temp.split()))
cnt = 0
i=2
while(i<=len(temp)):
    j=0
    while(j<=len(temp)-i):
        k=j
        sum = 0
        while(k<j+i):
            sum+=temp[k]
            if(sum==0):
                temp.insert(k,pow(10,10)+i)
                cnt+=1
            k+=1
        j+=1
    i+=1
i=0
while(i<len(temp)):
    if temp[i]>=pow(10,10):
        number=temp[i]-pow(10,10)
        start=i-number+1
        sum=0
        for j in range(start,i):
            sum+=temp[j]
        sum+=temp[i+1]
        if(sum!=0):
            cnt-=1
            del temp[i]
    i+=1
i=2
while(i<=len(temp)):
    j=0
    while(j<=len(temp)-i):
        k=j
        sum = 0
        while(k<j+i):
            sum+=temp[k]
            if(sum==0):
                temp.insert(k,pow(10,10)+i)
                cnt+=1
            k+=1
        j+=1
    i+=1
i=0
print(cnt)