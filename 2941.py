temp=input()
replist=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in replist:
    temp=temp.replace(i,".")
print(len(temp))