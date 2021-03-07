cases=[]
while(True):
    x,y,z=map(int,input().split())
    if(x==0 and y==0 and z==0):
        break
    lines=[x,y,z]
    lines.sort()
    if(lines[2]**2==lines[0]**2+lines[1]**2):
        cases.append("right")
    else:
        cases.append("wrong")
for case in cases:
    print(case)