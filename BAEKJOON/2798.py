temp=input()
temp=temp.split(" ")
n=int(temp[0])
m=int(temp[1])
temp=input()
temp=temp.split(" ")
for i in range(n):
    temp[i]=int(temp[i])
mi=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            s=temp[i]+temp[j]+temp[k]
            if s<=m and s>mi:
                mi=s
print(mi)
