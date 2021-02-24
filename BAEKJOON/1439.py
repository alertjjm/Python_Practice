testcase=input()
greedylist=[]
for i in range(len(testcase)-1):
    if(testcase[i]!=testcase[i+1]):
        greedylist.append(i)
if(len(greedylist)%2==0):
    print(len(greedylist)//2)
else:
    print(len(greedylist)//2+1)