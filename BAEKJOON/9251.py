str1=input()
str2=input()
len1=len(str1)
len2=len(str2)
dplist=[[0 for i in range(len2+1)]for j in range(len1+1)]
for i in range(len1):
    for j in range(len2):
        if(str1[i]==str2[j]):
            dplist[i+1][j+1]=dplist[i][j]+1
        else:
            dplist[i+1][j+1]=max(dplist[i+1][j],dplist[i][j+1])
'''for line in dplist:
    print(line)'''
print(dplist[len1][len2])