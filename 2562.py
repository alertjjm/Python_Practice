temp=[]
for i in range(9):
    n=int(input())
    temp.append(n)
m=max(temp)
i=temp.index(m)
print(m)
print(i+1)