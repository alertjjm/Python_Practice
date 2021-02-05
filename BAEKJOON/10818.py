n=int(input())
temp=input()
temp=temp.split()
for i in range(len(temp)):
    temp[i]=int(temp[i])
print(min(temp))
print(max(temp))