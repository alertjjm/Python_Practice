n=int(input())
a=[]
b=[1]*n
for i in range(n):
    temp=input()
    temp=temp.split(" ")
    x=int(temp[0])
    y=int(temp[1])
    a.append((x,y))
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][0]<a[j][0] and a[i][1]<a[j][1]:
            b[i]+=1
string=""
for i in b:
    string+=str(i)+" "
print(string[:-1])