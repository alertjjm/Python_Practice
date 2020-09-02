n=int(input())
m=0
i=0
while(n!=m):
    i+=1
    temp=str(i)
    if temp.find('666') != -1:
        m+=1
print(i)