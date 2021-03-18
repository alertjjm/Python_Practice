N=int(input())
students=[]
for i in range(N):
    students.append(int(input()))
dplist=[1]*(N)
for i in range(N):
    for j in range(i):
        if(students[j]<students[i]):
            dplist[i]=max(dplist[i],dplist[j]+1)
print(N-max(dplist))