str1=list(input())
str2=list(input())
dplist=[[0]*(len(str2)+1) for i in range(len(str1)+1)]
path=[[0]*(len(str2)+1) for i in range(len(str1)+1)]
for i in range(len(str1)):
    for j in range(len(str2)):
        if(str1[i]==str2[j]):
            path[i+1][j+1]=[str1[i],i,j]
            dplist[i+1][j+1]=dplist[i][j]+1
        else:
            if(dplist[i][j+1]>dplist[i+1][j]):
                dplist[i + 1][j + 1]=dplist[i][j+1]
                path[i+1][j+1]=path[i][j+1]
            else:
                dplist[i + 1][j + 1] = dplist[i+1][j]
                path[i + 1][j + 1] = path[i+1][j]
print(dplist[len(str1)][len(str2)])
y,x=len(str1),len(str2)
answer=[]
while(path[y][x]!=0):
    answer.append(path[y][x][0])
    newy=path[y][x][1]
    newx=path[y][x][2]
    y=newy
    x=newx
answer.reverse()
print(''.join(answer))