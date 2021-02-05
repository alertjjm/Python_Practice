x=int(input())
i=1
sum=1
while(sum<x):
    i += 1
    sum+=i
sum-=i
sum+=1
i-=1
if i%2==0:
    result = [i + 1, 1]
    while (sum != x):
        result[0] -= 1
        result[1] += 1
        sum += 1
else:
    result = [1, i + 1]
    while (sum != x):
        result[1] -= 1
        result[0] += 1
        sum += 1
print(str(result[0])+"/"+str(result[1]))