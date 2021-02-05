temp=input()
temp=temp.split(" ")
for i in range(len(temp)):
    temp[i]=int(temp[i])
if(temp[1]>=temp[2]):
    print("-1")
else:
    print(temp[0]//(temp[2]-temp[1])+1)