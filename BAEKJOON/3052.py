temp=[]
for i in range(10):
    n=int(input())
    temp.append(n%42)
temp=set(temp)
print(len(temp))